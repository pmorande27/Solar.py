"""File to hold the helper functions
"""
import json
import sys
sys.path.append('../src')
from celestial_bodies import CelestialBody
class Writer():
    def __init__(self):
        pass

    def write_file(self,filename="CelestialObjects"):
        """Method used to write in the files the usual planets used in the project
        """
        path = './data/'+filename
        sun = CelestialBody("Sun",1.989 * 10**30,0,3*500000000,"Star",0,0,"yellow")
        mercury = CelestialBody("Mercury",3.285 * 10**23,58*10**9,2*500000000,"Planet"
                        ,1.989 * 10**30,0,"orange")
        venus = CelestialBody("Venus",4.867 *10**24 ,108200000*10**3,2*500000000,"Planet"
                        ,1.989 * 10**30,0,"brown")
        earth = CelestialBody("Earth",5.972 *10**24,149597870.691*10**3,2*500000000,"Planet"
                        ,1.989 * 10**30,0,"blue")
        mars = CelestialBody("Mars",6.39 *10**23,228 *10**9,2*500000000,"Planet",1.989 * 10**30,0,"red")
        jupiter =  CelestialBody("Jupiter",1.899*10**27,778412026*10**3,2*500000000,"Planet",1.989 * 10**30,0,"green")
        probe = CelestialBody("Probe",1,149597870.691*10**3,2*500000000,"Probe",1.989 * 10**30,0,"black")
        list_of_bodies =[sun,mercury,venus,earth,mars,probe]
        data = {}
        data['Star'] = []
        data['Star'].append({ "Name" : "Sun",
                "mass" :str(sun.mass),
                "orbital_radius" : "0",
                "simulated_radius" : str(sun.simulated_radius),
                "type": sun.type_of_object,
                "colour":sun.colour
                })
        data['Planets'] = []
        for i in range(1,len(list_of_bodies)):
            planet = list_of_bodies[i]
            data['Planets'].append({ "Name" : planet.name,
                "mass" :str(planet.mass),
                "orbital_radius" : str(planet.orbital_radius),
                "simulated_radius" : str(planet.simulated_radius),
                "type": planet.type_of_object,
                "colour":planet.colour
                })
        with open(path, "w") as outfile:
            json.dump(data, outfile)
    def add_planet(self,name,mass,orbital_radius,sim_radius,colour,filename = "CelestialObjects"):
        """Method used to add a new Celestial Body to the file of CelestialBodies.txt
        in the correct json format.
        """
        planet_name = name
        planet_mass = mass
        planet_orbital_radius = orbital_radius
        simulated_radius = sim_radius
        data = {}
        path = './data/'+filename
        with open(path,"r") as json_file:
            data = json.load(json_file)
            data['Planets'].append({
            "Name" : planet_name,
            "mass" :str(planet_mass),
            "orbital_radius" : str(planet_orbital_radius),
            "simulated_radius" : str(simulated_radius),
            "type": "Planet",
            "colour":colour
            })
        with open(path, "w") as outfile:
            json.dump(data, outfile)
