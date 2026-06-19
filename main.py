import requests
from datetime import datetime
MY_LAT=6.487680
MY_LONG=4.417650
#
# response=requests.get(url='http://api.open-notify.org/iss-now.json')
# # if response.status_code == 404:
# #     raise Exception("That resource does not exist. ")
# # elif response.status_code== 300:
# #     raise Exception("You are not meant to access this data.")
# response.raise_for_status()
# data=response.json()
# longitude=data['iss_position']["longitude"]
# latitude=data['iss_position']["latitude"]
# print((longitude,latitude))
#
parameters={
    "lat":MY_LAT,
"lng":MY_LONG,
"formatted":0
}
response=requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data=response.json()
sunrise=data['results']['sunrise'].split("T")[1].split(":")[0]
sunset=data['results']['sunset'].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

time_now=datetime.now()
print(time_now.hour)

