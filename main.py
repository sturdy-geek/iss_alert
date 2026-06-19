import requests
from datetime import datetime
from email.mime.text import MIMEText
import smtplib
import time
import os
response=requests.get(url="http://api.open-notify.org/iss-now.json")
if  response.status_code == 404:
    raise Exception("That resource does not exist.")
elif response.status_code == 402:
    raise Exception("You are not authorised to access this data.")
#
response.raise_for_status()
data =response.json()
iss_longitude=data["iss_position"]["longitude"]
iss_latitude=data["iss_position"]["latitude"]
MYLAT=6.524379
MYLONG=3.379206
MYPASSWORD=os.environ.get("MYPASSWORD")
MYEMAIL=os.environ.get("MYEMAIL")
MYPOS=(MYLAT,MYLONG)
parameters={
    "lat":MYLAT,
    "lng":MYLONG,
    "formatted":0,
}

response=requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data=response.json()
sunrise=int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset=int(data["results"]["sunset"].split("T")[1].split(":")[0])
time_now=datetime.now()
hour=time_now.hour
def is_iss_above(iss_latitude,hour,sunset,sunrise):
    while True:
        time.sleep(60)
        if MYLAT-5<=float(iss_latitude)<=MYLAT+5 and hour>=sunset or hour<=sunrise:
            message=MIMEText("The ISS have arrived , LOOK UP! ")
            message["from"]=MYEMAIL
            message["to"]=MYEMAIL
            connection = smtplib.SMTP("smtp.gmail.com")
            connection.starttls()
            connection.login(MYEMAIL, MYPASSWORD)
            connection.sendmail(
                from_addr=MYEMAIL,
                to_addrs=MYEMAIL,
                msg=message.as_string()

            )
       


is_iss_above(iss_latitude,hour,sunset,sunrise)
