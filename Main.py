from animate import animation
from Planets import Planet
import numpy as np
def inputFiles(nameofFile):
    planets = []
    file = open(nameofFile,"r")
    for line in file:
        parsedInfo = line.split(",")
        planet = Planet(parsedInfo[0],float(parsedInfo[1]),float(parsedInfo[2]),float(parsedInfo[3]),parsedInfo[4],float(parsedInfo[5]))
        planets.append(planet)
    return planets
def main():

    b = Planet("marte", 6.4185*10**23,0, 500000,"Planet",0)
    e = Planet("phobos",1.06*10**16,9377300.0,500000,"Moon",6.4185*10**23)
    f = Planet("deimos",1.8*10**15,23.463*10**6,500000,"Moon",6.4185*10**23)
    d =inputFiles("CelestialObjects")
    a = animation(d)
    a.plot()
main()

