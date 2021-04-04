import json
from Planet import Planet
import numpy as np
from Options import Options


class SolarSystem(object):
    """Class used to represent the Solar System and mock its behaviour.
    """
    G = 6.67408 * 10 ** -11

    def __init__(self, time_step, vRelative, options):
        """Constructor of the class SolarSytem, used to initialise all the planets with the information supplied from a file.

        Args:
            time_step (float): interval between updates (in seconds).
            vRelative (float): speed of the probe relative to the Earth.
            options (Options): Enum used to decide which type of simulation should be launched.
        """
        self.vRelative = vRelative
        self.celestial_bodies = self.inputFiles(options)
        self.time_step = time_step
        self.update_initial_acceleration()
        if (options ==Options.NORMAL_RUN):
            self.initial_time_step = time_step
            self.initial = False
        else:
            self.initial_time_step = 1
            self.initial = False
        self.time = 0
        self.file = open("../data/energy", "w")
        self.file.write(str(self.getEnergy()) + "\n")
        self.updates = 0

    def __del__(self):
        """Deconstructor of the class, used to close the file.
        """
        self.file.close()

    def inputFiles(self, option):
        """Function used to read all the planets information from the supplied file (CelestialObjecs.txt).
        It will intiatialize all the planets with the required information and it will append them to a list.

        Returns:
            [Planet]: list of all the planets (object type Planet)
        """
        planets = []
        with open("../data/CelestialObjects") as json_file:
            data = json.load(json_file)
            for star in data['Star']:
                planets.append(Planet(star['Name'], float(star['mass']), float(star['orbital_radius']),
                                      float(star['simulated_radius']), star['type'], 0, self.vRelative))
            for planet in data['Planets']:
                if(option == Options.NORMAL_RUN and planet['Name'] =="Probe"):
                    continue
                planets.append(Planet(planet['Name'], float(planet['mass']), float(planet['orbital_radius']),
                                      float(planet['simulated_radius']), planet['type'], float(star['mass']),
                                      self.vRelative))
        return planets

    def getKineticenergy(self):
        """Function used to obtain the kinetic energy of the system at a given time.
        The Kinetic energy of the system is calculated by iterating through all the bodies on a system and
        adding the individual contributions by the usual formaula, K = 1/2mv^2.

        Returns:
            float: Value of the kinetic energy of the system
        """
        kinetic = 0
        for k in range(len(self.celestial_bodies)):
            planet = self.celestial_bodies[k]
            kinetic += planet.mass * 0.5 * np.linalg.norm(planet.velocity)** 2
        return kinetic

    def getEnergy(self):
        """Function used to get the total energy of the system, which is the sum of the kinetic energy and potential 
        energy at a given time

        Returns:
            float: value of the total energy.
        """
        return self.getPotentialEnergy() + self.getKineticenergy()

    def update_beeman(self):
        """Method used to update the position, velocity and acceleration of a list of planets using 
        Beeman's methods. First the positions of all the planets are updated, then the velocities of all of them, which
        also updates the accelerations. TO obtain good results it is important to do it in these 'blocks', otherwise the
        update on the position of one planet could affect the update on the position of another planet (if the updates were done in only one block)-

        Returns:
            int: Energy of the system after the update
        """
        kinetic = 0
        self.updates += 1

        # Update acceleration and velocity of all planets from time t-timestep to time t
        for k in range(len(self.celestial_bodies)):
            others = self.celestial_bodies[:]
            planet = others.pop(k)
            planet.update_position_beeman(self.time_step)

        # Update position of all planets from time t-timestep to time t
        for k in range(len(self.celestial_bodies)):
            others = self.celestial_bodies[:]
            planet = others.pop(k)
            planet.update_velocity_beeman(self.time_step, others)
        energy = self.getEnergy()
        self.file.write(str(energy)+"\n")
        return energy

    def distanceToMars(self):
        """function used to calculate the distance from the probe to mars at a given time.
        The Probe's position it is assumed to be the last in the list and mars the 5th one.

        Returns:
            float: distance from the probe to mars
        """
        return  np.linalg.norm(self.celestial_bodies[len(self.celestial_bodies) - 1].position,
                               self.celestial_bodies[4].position)

    def update_euler(self):
        """Method used to update the position, velocity and acceleration of a list of planets
        using Euler-Crommer Method. The accelerations are updated to time t, then all the velcoities are updated to 
        time t + dt and finally all the positions are updated at time t+dt.

        Returns:
            int : returns the energy of the system after the update.
        """
        kinetic = 0

        # Update acceleration and velocity of all planets from time t-timestep to time t
        for k in range(len(self.celestial_bodies)):
            others = self.celestial_bodies[:]
            planet = others.pop(k)
            planet.update_acceleration(others)
            planet.update_velocity_euler(self.time_step)

        # Update position of all planets from time t-timestep to time t
        for k in range(len(self.celestial_bodies)):
            others = self.celestial_bodies[:]
            planet = others.pop(k)
            planet.update_position_euler(self.time_step)
        energy = self.getEnergy()
        return energy

    def update_initial_acceleration(self):
        """Function used to set the acceleration of the planets as t=0. This is important for the Beeman's Method.
        """
        for k in range(len(self.celestial_bodies)):
            others = self.celestial_bodies[:]
            planet = others.pop(k)
            planet.update_acceleration(others)
            planet.acceleration_prev = planet.acceleration

    def getPotentialEnergy(self):
        """Function used to get the value of the potential energy of the system at a given time.
        The energy is given by the sum of the individual contributions, each pair of bodies contribute whith
        -GmM/r^2.

        Returns:
            float: Potential Energy of the system.
        """
        potential = 0
        for i in range(len(self.celestial_bodies) - 1):
            for j in range(i + 1, len(self.celestial_bodies)):
                body_one = self.celestial_bodies[i]
                body_two = self.celestial_bodies[j]
                vector1 = body_one.position
                vector2 = body_two.position
                distances =  vector2-vector1
                distance = np.linalg.norm(distances)
                potential += -SolarSystem.G * body_one.mass * body_two.mass / distance
        return potential

