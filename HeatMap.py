import ssl
from pygame import *
import os
from pymongo import MongoClient

# Setting MongoDB
password = os.getenv("mongoPass")
client = MongoClient("mongodb+srv://Armaan:" + password + "@cluster-1-dnqxb.mongodb.net/test?retryWrites=true&w=majority", ssl_cert_reqs=ssl.CERT_NONE)
db = client.Twitter
hashtagCollection = db.Hashtags
# Getting coordinates
coordinateDict = hashtagCollection.find_one({})
coordinates = []
num = 1
while True:
    try:
        line = coordinateDict[str(num)]
        firstBracket = line.find('[')
        lastBracket = line.find(']')
        coordinates.append(line[firstBracket+1:lastBracket])
        num += 1
        print(coordinates)
    except:
        break
os.environ['SDL_VIDEO_CENTERED'] = '1'  # Centering the screen
init()  # Starting up pygame
size = width, height = 1000, 600
screen = display.set_mode(size)
map = transform.scale(image.load("map.jpg"),(1000,600))
running = True


while running:
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False
    screen.blit(map,(0,0))
    display.flip()