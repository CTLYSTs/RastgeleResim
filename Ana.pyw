import requests
import random
firstno = str(random.randint(100,1200))
secondno = str(random.randint(100,1200))
try:
    create = open(firstno+secondno+".jpg", "x")
    create.close()
except:
    pass
myfile = open(firstno+secondno+".jpg", "wb")
response = requests.get("https://picsum.photos/"+firstno+"/"+secondno)
myfile.write(response.content)
myfile.close()