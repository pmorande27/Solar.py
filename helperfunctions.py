from Planets import Planet
import json
def writeFile():
    sun = Planet("Sun",1.989 * 10**30,0,3*500000000,"Star",0)
    mercury = Planet("Mercury",3.285 * 10**23,58*10**9,2*500000000,"Planet",1.989 * 10**30)
    Venus = Planet("Venus",4.867 *10**24 ,108200000*10**3,2*500000000,"Planet",1.989 * 10**30)
    earth = Planet("Earth",5.972 *10**24,149597870.691*10**3,2*500000000,"Planet",1.989 * 10**30)
    mars = Planet("Mars",6.39 *10**23,228 *10**9,2*500000000,"Planet",1.989 * 10**30)
    d =[sun,mercury,Venus,earth,mars]
    data = {}
    data['Star'] = []
    data['Star'].append({ "Name" : "Sun",
            "mass" :str(sun.mass),
            "orbital_radius" : "0",
            "simulated_radius" : str(sun.simulated_radius),
            "type": sun.type_of_object,
            })
    data['Planets'] = []
    for i in range(1,len(d)):
        planet = d[i]
        data['Planets'].append({ "Name" : planet.name,
            "mass" :str(planet.mass),
            "orbital_radius" : str(planet.orbital_radius),
            "simulated_radius" : str(planet.simulated_radius),
            "type": planet.type_of_object,
            })
    with open("CelestialObjects", "w") as outfile:
        json.dump(data, outfile)
def add_planet():
    planet_name = input("Planet's name")
    planet_mass = float(input("Planet's mass"))
    planet_orbital_radius = float(input("Planet's orbital radius"))
    simulated_radius = float(input("simulated radius"))
    data = {}
    with open("CelestialObjects") as json_file:
            data = json.load(json_file)
            data['Planet'].append({
            "Name" : planet_name,
            "mass" :str(planet_mass),
            "orbital_radius" : str(planet_orbital_radius),
            "simulated_radius" : str(simulated_radius),
            "type": "Planet"
            })
    with open("CelestialObjects", "w") as outfile:
        json.dump(data, outfile)