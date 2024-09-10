import urllib.request
import urllib.parse
from dotenv import load_dotenv
import os
load_dotenv()
apikey= os.getenv('apiKey')
def sendSMS(apikey, numbers, sender, message):
    data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers, 
                                    'message' : message, 'sender': 'Kanye'})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.txtlocal.com/send/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return(fr)
 
resp =  sendSMS(apikey, '3475171648', 'Kanye', 'This is your message')
print (resp)