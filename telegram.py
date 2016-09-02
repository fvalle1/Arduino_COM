import serial
import requests
import time

token='bot<token>/'
method='getMe'
url='https://api.telegram.org/'+token
off =0
payload={}

newupdate=False

r=requests.get(url+method,params=payload)
print r.url

print r.json()

r=requests.get(url+'getUpdates',params=payload)
while True:
    data = r.json()
    try:
        off=data['result'][0]['update_id']
        message=data['result'][0]['message']['text']
        messageid=data['result'][0]['message']['message_id']
        chatid= data['result'][0]['message']['from']['id']
        name= data['result'][0]['message']['from']['first_name']
        method='getUpdates'
        newupdate=True
        print data
        print message
    except:
        print
    payload={'offset':off+1}
    r=requests.get(url+method,params=payload) 
    if newupdate:
        newupdate=False
        answer='Ciao '+name+', sono contento se mi scrivi'
        payload={'chat_id':chatid,'text':answer,'reply_to_message_id':messageid}
        a=requests.get(url+'sendMessage',params=payload)
    time.sleep(5)
        
