from bs4 import BeautifulSoup
import urllib3
import requests
import re
from utils import get_soundex

class City(type):
    """
    Define an Instance operation that lets clients access its unique
    instance.
    """    
    def getTier2Cities():
        try:
            url="https://en.wikipedia.org/wiki/Classification_of_Indian_cities"
            r = requests.get(url,verify=False)
            soup = BeautifulSoup(r.text, "html.parser")
            tier_cities=list(map(lambda x:x.text.lower(),soup.find('table',class_='wikitable').find_all('a')))
        except:
            tier_cities = ["Bangalore", "Chennai", "Delhi", "Hyderabad", "Kolkata", "Mumbai", "Ahmedabad", "Pune", "Agra", "Ajmer", "Aligarh", 
                           "Amravati", "Amritsar", "Asansol", "Aurangabad", "Bareilly", "Belgaum", "Bhavnagar", "Bhiwandi", "Bhopal", "Bhubaneswar", 
                           "Bikaner", "Bilaspur", "Bokaro Steel City", "Chandigarh", "Coimbatore Nagpur", "Cuttack", "Dehradun", "Dhanbad", "Bhilai", 
                           "Durgapur", "Erode", "Faridabad", "Firozabad", "Ghaziabad", "Gorakhpur", "Gulbarga", "Guntur", "Gwalior", "Gurgaon", 
                           "Guwahati", "Hubli", "Dharwad", "Indore", "Jabalpur", "Jaipur", "Jalandhar", "Jammu", "Jamnagar", "Jamshedpur", "Jhansi", 
                           "Jodhpur", "Kakinada", "Kannur", "Kanpur", "Kochi", "Kottayam", "Kolhapur", "Kollam", "Kota", "Kozhikode", "Kurnool", 
                           "Ludhiana", "Lucknow", "Madurai", "Malappuram", "Mathura", "Goa", "Mangalore", "Meerut", "Moradabad", "Mysore", "Nanded", 
                           "Nashik", "Nellore", "Noida", "Palakkad", "Patna", "Pondicherry", "Purulia Allahabad", "Raipur", "Rajkot", "Rajahmundry", 
                           "Ranchi", "Rourkela", "Salem", "Sangli", "Siliguri", "Solapur", "Srinagar", "Thiruvananthapuram", "Thrissur", 
                           "Tiruchirappalli", "Tirupati", "Tirunelveli", "Tiruppur", "Tiruvannamalai", "Ujjain", "Bijapur", "Vadodara", "Varanasi", 
                           "Vasai-Virar City", "Vijayawada", "Vellore", "Warangal", "Surat", "Visakhapatnam"]
        return tier_cities
    
    def getCityAlias():
        synonym_names = {}
        try:
            r=requests.get('https://www.scoopwhoop.com/news/whats-in-a-name/#.45rdcz1m2',verify=False)
            containers=BeautifulSoup(r.text,'html.parser').find('div',class_='article-body').find_all('h2')
            
            for container in containers:
                if re.search(r'^[0-9]{1,2}.+',container.text.strip()):
                    synonym_names[container.text.strip().split()[1].lower()]=container.text.strip().split()[-1].lower()
        except:
            synonym_names = {'trichinapoly': 'tiruchirapalli', 'baroda': 'vadodara', 'trivandrum': 'thiruvananthapuram', 'bombay': 'mumbai', 'madras': 'chennai', 'cochin': 'kochi', 'calcutta': 'kolkata', 'pondicherry': 'puducherry', 'cawnpore': 'kanpur', 'belgaum': 'belagavi', 'indhur': 'indore', 'panjim': 'panaji', 'poona': 'pune', 'simla': 'shimla', 'benares': 'varanasi', 'waltair': 'visakhapatnam', 'tanjore': 'thanjavur', 'jubbulpore': 'jabalpur', 'ootacamund': 'udhagamandalam', 'calicut': 'kozhikode', 'gauhati': 'guwahati', 'allepey': 'alappuzha', 'mysore': 'mysuru', 'mangalore': 'mangaluru', 'bangalore': 'bengaluru'}
        return synonym_names
    
    
    tier_cities = getTier2Cities()
    synonym_names=getCityAlias()
    
    @staticmethod
    def getCities():
        return City.tier_cities
    
    @staticmethod
    def checkCityOperationStatus(loc):
        if loc in City.tier_cities:
            return True
        if loc in City.synonym_names.keys() or loc in City.synonym_names.values():
            return True
        soundex_dict_tier={get_soundex(name):name for name in City.tier_cities}
        soundex_dict_syn={get_soundex(key):value for key,value in City.synonym_names.items()}
                
        loc_soundex=get_soundex(loc)
        
        
        if loc_soundex in soundex_dict_tier.keys():
            return True
        if loc_soundex in soundex_dict_syn.keys():
            return True
        return False
        
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
            
        return cls._instance
    