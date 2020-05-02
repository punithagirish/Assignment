from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet, AllSlotsReset, Restarted
import re
import requests
import logging
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings()
import zomatopy
import json
import smtplib, ssl
import re 

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

from cityUtil import City
from utils import get_soundex
logger = logging.getLogger(__name__)
def parsePrice(budget):
    temp = re.findall(r'\d+', budget) 
    res = list(map(int, temp))
    return res    

def parsebudget_txt(budget_txt):
	price_list = []   
	try:             
	    if budget_txt!=None:
	        budget_txt = budget_txt.lower().strip()
	    temp = re.findall(r'\d+', budget_txt) 
	    val = list(map(int, temp))
	    if budget_txt.find("max")>=0 or budget_txt.find("less")>=0 or budget_txt.find("<")>=0 or budget_txt.find("lower")>=0:
	        price_list.insert(0, 0)
	        price_list.extend(val)
	    elif budget_txt.find("min")>=0 or budget_txt.find("more")>=0 or budget_txt.find("range")>=0 or budget_txt.find(">")>=0 or budget_txt.find("greater")>=0 or budget_txt.find("high")>=0 or budget_txt.find("between")>=0:
	        price_list.extend(val) 
	    elif budget_txt=="1" or budget_txt.find("cheap")>=0 or budget_txt.find("low")>=0 or budget_txt.find("budget")>=0 or  budget_txt.find("pocket-friendly")>=0 or budget_txt.find("pocket friendly")>=0:
	        price_list = [0,300]
	    elif budget_txt=="2" or budget_txt.find("mid")>=0 or budget_txt.find("moderate")>=0:
	        price_list = [300,700]
	    elif budget_txt=="3" or budget_txt.find("costly")>=0 or budget_txt.find("expensive")>=0:
	        price_list = [700]  
	    
	    if len(price_list)==0 and len(val)>0:
	        price_list.extend(val)	        
	    if len(price_list)==0:
	        price_list = [300,700]
	except Exception as e:
		logger.exception(e)
	
	return price_list
   
class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_restaurant'
		
	def run(self, dispatcher, tracker, domain):
		logger.info("in ActionSearchRestaurants")
		try:
			noresults = True
			config={ "user_key":"e44f0277d2d63ad4f712b4670cbb04d5"}
			zomato = zomatopy.initialize_app(config)
			loc = tracker.get_slot('location')
			if not loc:				
				dispatcher.utter_template("utter_ask_location", tracker)
				return []
			
			cuisine = tracker.get_slot('cuisine')
			if not cuisine:				
				dispatcher.utter_template("utter_ask_cuisine", tracker)
				return []
			price=tracker.get_slot('price')
			if len(price)==0 and  tracker.get_slot('budget')==None:
				dispatcher.utter_template("utter_ask_price", tracker)
				return []
					
			cuisines=['chinese','mexican','italian','american','south indian','north indian']
			
			soundex_dct={get_soundex(value):value for value in cuisines}
			
			if cuisine and get_soundex(cuisine) in soundex_dct.keys():
				cuisine=soundex_dct[get_soundex(cuisine)]
			
			if loc == None or cuisine==None:
				dispatcher.utter_template("utter_noresults", tracker)
				return [SlotSet('noresults',True)] 
			if tracker.get_slot('location_type')==False:
				dispatcher.utter_template("utter_nontier", tracker)
				return [] 
				
			price=tracker.get_slot('price')
			if len(price)==0 and tracker.get_slot('budget')!=None:
				budget_val = tracker.get_slot('budget')
				price= parsebudget_txt(budget_val)
				SlotSet('price',price)	 
				 
			location_detail=zomato.get_location(loc, 1)
			d1 = json.loads(location_detail)
			try:
				lat=d1["location_suggestions"][0]["latitude"]
				lon=d1["location_suggestions"][0]["longitude"]
				cuisines_dict={'american':1,'chinese':25,'mexican':73,'italian':55,'north indian':50,'south indian':85}
				lst = []
				results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)))
				logger.debug(results)
				d = json.loads(results)
				for restaurant in d['restaurants']:
					lst.append((restaurant['restaurant']['name'],restaurant['restaurant']['location']['address'],float(restaurant['restaurant']['average_cost_for_two']),float(restaurant['restaurant']['user_rating']['aggregate_rating'])))
				
				if len(price)==1:
					if not int(price[0])>=700:
						price.insert(0, 0)
								
				price=list(map(int,price))
				price=sorted(price)
				logger.debug(price)
				lst1=list(sorted(lst,key=lambda x:x[-2],reverse=True))
				logger.debug(lst1)
				if len(price)==0:
					dispatcher.utter_template("utter_noresults", tracker)
					return [SlotSet('noresults',True)] 
				if len(price)==1:
					logger.debug("i am here")
					final_lst=list(filter(lambda x:x[-2]>=price[0],lst1))
				else:
					logger.debug("i am here1213")
					final_lst=list(filter(lambda x:x[-2]>=price[0] and x[-2]<=price[1],lst1))
				
				final_lst=list(sorted(final_lst,key=lambda x:x[-1],reverse=True))[:10]
				response_5=""
				response_10=""
				
				if len(final_lst) == 0:
					response_5= "no results"
					noresults = True
				else:
					counter=1
					for restaurant in final_lst[:5]:
						response_5 += str(counter) + ". " + restaurant[0]+ " in "+ " ".join(restaurant[1:-2])+" has been rated "+str(restaurant[-1])+"\n"
						noresults = False
						counter+=1	
					restaurant_final_list=final_lst[:10]
			
					counter=1
					for restaurant in restaurant_final_list:
						text_respose = str(counter)+". Restaurant Name: "+restaurant[0]+"\n Restaurant locality address: "+" ".join(restaurant[1:-2])+"\n Average budget for two people: "+str(restaurant[-2])+"\n Zomato user rating: "+str(restaurant[-1])+"\n\n" 
						response_10 += text_respose  
						noresults = False
						counter+=1		
					file=open("email_restarunt_search.txt","w")
					file.write(response_10)
					file.close()
					
			except Exception as e:
				logger.exception(e)
				response_5="no results"
				response_10="no results"
			if noresults:
				dispatcher.utter_template("utter_noresults", tracker)
			else:
				dispatcher.utter_message(response_5)
		except Exception as e:
			logger.exception(e)
		return [SlotSet('noresults',noresults)]


class ActionSearchCity(Action):
	def name(self):
		return 'action_city'
	
	def run(self, dispatcher, tracker, domain):
		logger.info("in ActionSearchCity")
		logger.debug(tracker.get_slot('location'))
		loc = tracker.get_slot('location')
		location_type = True
		if not City.checkCityOperationStatus(loc):
			dispatcher.utter_template("utter_nontier", tracker)
			location_type = False
			loc = None
			SlotSet('location',loc)
		return [SlotSet('location_type',location_type)]

class ActionGetCuisineSlection(Action):
	def name(self):
		return 'action_get_cuisine'
	
	def run(self,dispatcher,tracker,domain):		
		logger.info("in ActionGetCuisineSlection")
		val=tracker.get_slot('option')
		cuisines=['chinese','mexican','italian','american','south indian','north indian']
		
		return [SlotSet('cuisine',cuisines[int(val)-1])]

class ActionGetBudgetSelection(Action):
	def name(self):
		return 'action_get_budget'
	
	def run(self,dispatcher,tracker,domain):	
		logger.info("in ActionGetBudgetSelection")	
		price= []
		try:	
			val=tracker.get_slot('budget')
			if not val and tracker.get_slot('option'):
				val=tracker.get_slot('option')
			logger.debug(val)
			price = parsebudget_txt(val)
		except Exception as e:
			logger.exception(e)
		
		return [SlotSet('budget',val),SlotSet('price',price)]
			
	
class ActionSendMail(Action):
	def name(self):
		return 'action_send_mail'
	
	def run(self,dispatcher,tracker,domain):
		logger.info("in ActionSendMail")		
		gmail_user="ml7.foodie@gmail.com"
		gmail_password="Upgrad@123"
		gmail_port = 587  # For SSL
		gmail_smtp_server = "smtp.gmail.com"
		receiver_email = tracker.get_slot("email")
		logger.info("in receiver_email")
		
		subject=" Restaurant recommendations in "+tracker.get_slot("location")
		
		try:  
			context = ssl.create_default_context()
			ssl._create_default_https_context = ssl._create_unverified_context
			with smtplib.SMTP(gmail_smtp_server, gmail_port) as server:
			    server.ehlo()
			    server.starttls()
			    server.ehlo()
			    server.login(gmail_user, gmail_password)
			    search_response=""
			    file=open('email_restarunt_search.txt','r')
			    for line in file.readlines():
			    	search_response+=line
			    file.close()
			    msg = MIMEMultipart()
			    msg['From'] = gmail_user
			    msg['To'] = receiver_email
			    msg['Subject'] = subject
			    body = search_response
			    msg.attach(MIMEText(body,'plain'))
			    logger.debug(msg.as_string())
			    server.sendmail(gmail_user,receiver_email,msg.as_string())
			    server.close()
			logger.debug("sending utter_email_sent")
			dispatcher.utter_template("utter_email_sent", tracker)
			
		except Exception as e:		
			logger.exception(e)
			logger.debug("sending utter_email_error")
			dispatcher.utter_template("utter_email_error", tracker)
			
		return []

class ActionResetSlots(Action):
	def name(self):
		return 'action_reset'
		
	def run(self, dispatcher, tracker, domain):
		#AllSlotsReset()
		return [AllSlotsReset()]

class ActionRestarted(Action): 	
    def name(self): 		
        return 'action_restarted' 	
    def run(self, dispatcher, tracker, domain): 
        return[Restarted()] 