import datetime, time
import urllib.request
import random
myurl = "https://api.thingspeak.com/update?api_key=A54Y2MHH6JNRH7JP&field1="

for i in range(20):
   url = myurl + str(random.randint(20, 80))
    f = urllib.request.urlopen(url)
    data = str(f.read())
    print("Got", data)
    time.sleep(15)
