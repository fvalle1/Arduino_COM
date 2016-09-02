import serial #serial communication
import time
import requests #API requests
import serial.tools.list_ports

print(list(serial.tools.list_ports.comports()))

trigger='<event_name>'
IFTTTkey='<key>'
url='https://maker.ifttt.com/trigger/'+trigger+'/with/key/'+IFTTTkey+'?value1=running%20python'
response=requests.get(url)

#open serial port
#change this!
try:
    port = serial.Serial('/dev/tty.usbmodem641',9600)
except:
    port = serial.Serial('/dev/tty.usbmodem441',9600)

#wait Arduino to reset
time.sleep(3)

token='bot123:loremipsum'
id='<chat_id>'
message='Hello IoT!'
#useful to get chat_id
response=requests.get('https://api.telegram.org/'+token+'/getUpdates?limit=5')
url='https://api.telegram.org/'+token+'/sendMessage?chat_id='+id+'&text='+message

port.write('begins')

while True:
    read= port.readline() #read Arduino's Serial port
    print type(read)
    print read
    try:
        intread=int(read)
        if intread==1:
            print 'sent'
            response=requests.get(url)
            print response
            break
    except:
        print read
