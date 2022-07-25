#chatbot
from datetime import datetime
import webbrowser
import os,glob
import random
msg = input("Enter Message : ")
helloIntent = ["hi","hey","hello","hie","wassup"]
byeIntent = ["bye","tata","see you later","see you","ttyl"]
dateIntent = ["show me date","date please","date"]
timeIntent = ["show me time","time please","time"]
musicIntent = ["music","play music","song","play song"]
if msg in helloIntent:
    print("Hello")
elif msg in byeIntent:
    print("Bye")
elif msg in dateIntent:
    dt = datetime.now()
    print(dt.strftime("%d/%m/%y,%a"))
elif msg in timeIntent:
    pass
elif msg.startswith("open"):
    url = msg.split()[-1]+".com"
    webbrowser.open(url)

elif msg in musicIntent:
     files= glob.glob("*.mp3")
     song=random.choice(files)
     os.startfile(song)
     
