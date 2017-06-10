import util
import ACO
import random
from pprint import pprint

ambient = util.getAmbient("RNP.json")
request = util.getRandomRequest(len(ambient['servers'],5))
antColony = ACO.antColony(15,request)

ACO.ACO(antColony,ambient,0.1)