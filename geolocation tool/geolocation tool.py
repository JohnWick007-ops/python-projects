import requests
print("Let's find the geollocation detail of a Ip")
target = input("what is the target IP (if Ip is yous ,type nothing ,just press enter) : ")
if(target == ""):
    url = f"http://ip-api.com/json"
else:
    url = f"http://ip-api.com/json/{target}"

response = requests.get(url)
data = response.json()
try:
    if(data["status"]== "success"):
       print(f"the country is {data["country"]}")
       print(f"the country code is {data["countryCode"]}")
       print(f"the region is {data["region"]}")
       print(f"the region name is {data["regionName"]}")
       print(f"the city is {data["city"]}")
       print(f"the zip code is {data["zip"]}")
       print(f"the lat detail is {data["lat"]}")
       print(f"the lon detail is {data["lon"]}")
       print(f"the timezone is {data["timezone"]}")
       print(f"the internet service provider is {data["isp"]}")
       print(f"the org is {data["org"]}")
       print(f"the Autonomous System is {data["as"]}")
       print(f"the query is {data["query"]}")   
    else:
        print("the ip is not found")
except Exception as e:    
    print(f"couldn't find data , error in {e}")