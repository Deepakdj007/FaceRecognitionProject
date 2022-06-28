#create virtual environment: virtualenv pywhatsapp
#activate virtual environment: pywhatsapp\Scripts\activate.bat

from urllib import response
import pandas as pd
from twilio.rest import Client
from . import low_attendance_list as lal
import dataframe_image as dfi
import requests
import base64
import json

def remove(string):
    return "".join(string.split())

account_sid = 'ACab5110bbba2f494759676b42f487af56'
auth_token = '545ecbb8095b8e7abf014fc19b585288'
client = Client(account_sid, auth_token)

def whatsapp_message(Class_name):
    names,email,df = lal.low_attendance(Class_name)
    
    dff = df[["RETID", "Name", "Phone_no", "Subject_1", "Subject_2", "Subject_3", "Subject_4", "Subject_5"]]

    for i in dff["RETID"]:
        R = pd.DataFrame(dff.loc[dff["RETID"] == i])
        dfi.export(R,"details.png")
        with open("details.png", "rb") as file:
            url = "https://api.imgbb.com/1/upload"
            payload = {
                "key": "0198d1e832eed2cd0f5114e0552745ec",
                "image": base64.b64encode(file.read()),
            }
            result = requests.post(url, payload)
            response = json.loads(result.text)
            media = "{}".format(response["data"]["url"]) 
        pno = str(''.join([n for n in R["Phone_no"] if n.isdigit()]))
        cpno = "+91"+pno
        rcpno = remove(cpno)
        message = client.messages.create(
                                body="You have low attendance score in the following subject(s):",
                                media_url= media,
                                from_='whatsapp:+14155238886',
                                to= remove('whatsapp:'+rcpno)
                            )
    """   print(message.sid)"""