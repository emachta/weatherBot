#Created by Ennis Machta - 06/20/18


import urllib.request
import json
import string
import re




cityre = input("Enter a city name for the current temperature: ")
city = re.sub(r"(\b[a-z])",lambda x: x.group(1).upper(),cityre)

#If you want to use ID instead of city name, use this function
'''
def getid() -> str:
    cityopen = open('city.json', 'rb')
    citydata = json.load(cityopen)
    for item in citydata:
        if item["name"] == city:
            return str(item["id"])

'''
#my basic membership app id
appid = "fc26b5f258ff608cf50fcac2179898ad"
url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&APPID=" + appid 

data = urllib.request.urlopen(url)
actualdata = json.load(data)

temp = actualdata["main"]["temp"]
    
result = float(temp)

dF = result * 9 / 5 - 459.67


print("\n\n\n")
print("The weather in {} is: {:.0f}°F".format(city,dF))
    

