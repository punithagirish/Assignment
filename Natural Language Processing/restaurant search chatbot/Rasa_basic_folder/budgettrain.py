import re 
budget = "in range of 300 to 700"
print("The original string : " + budget)   
email = "please send me a mail to jddk2jmd@kdl.com"
temp = re.findall('[a-zA-Z0-9_.+]+@[a-zA-Z]+[.][a-zA-Z0-9-.]+$', email)
print(temp) 
email_pattern = "[A-Z0-9a-z._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,64}"
def  parsePrice(budget):
    temp = re.findall(r'\d+', budget) 
    res = list(map(int, temp))
    return res    

def parseBudget(budget):    
    price = []            
    if budget!=None:
        budget = budget.lower().strip()
    if budget.find("max")>=0 or budget.find("less")>=0 or budget.find("<")>=0 or budget.find("lower")>=0:
        price.insert(0, 0)
        price = price+parsePrice(budget)
    elif budget.find("min")>=0 or budget.find("more")>=0 or budget.find("range")>=0 or budget.find(">")>=0 or budget.find("greater")>=0 or budget.find("high")>=0 or budget.find("between")>=0:
        price = price+parsePrice(budget)  
    elif budget=="1" or budget.find("cheap")>=0 or budget.find("low")>=0 or budget.find("budget") or  budget.find("pocket-friendly")>=0 or budget.find("pocket friendly")>=0:
        price = [0,300]
    elif budget=="2" or budget.find("mid")>=0 or budget.find("moderate")>=0:
        price = [300,700]
    elif budget=="3" or budget.find("costly")>=0:
        price = [700]  
    
    if len(price)==0 and len(parsePrice(budget))>0:
        price = price+parsePrice(budget)
        
    if len(price)==0:
        price = [300,700]
    return price