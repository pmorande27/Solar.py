import json
from Planet import Planet
from vector import Vector


class SolarSystem(object):
    """Class used to represent the Solar System and mock its behaviour.
    """
    G = 6.67408 * 10 ** -11

    def __init__(self, time_step, vRelative):
        """Constructor of the class SolarSytem, used to initialise all the planets (position, velocity
         and acceleration).

        Args:
            time_step (float): interval between updates (in seconds).
            vRelative (float): speed of the probe relative to the Earth.
        """
        self.vRelative = vRelative
        self.celestial_bodies = self.inputFiles()
        self.time_step = time_step
        self.update_initial_acceleration()
        self.file = open("energy", "w")
        self.file.write(str(self.getEnergy()) + "\n")
        self.mini = Vector.distance(self.celestial_bodies[len(self.celestial_bodies) - 1].position,
                                    self.celestial_bodies[4].position).mdoulus()
        self.updates = 0

    def __del__(self):
        """Deconstructor of the class, used to close the file.
        """
        self.file.close()

    def inputFiles(self):
        """Function used to read all the planets information from the supplied file (CelestialObjecs.txt).

        Returns:
            [Planet]: list of all the planets (object type Planet)
        """
        planets = []
        with open("CelestialObjects") as json_file:
            data = json.load(json_file)
            for star in data['Star']:
                planets.append(Planet(star['Name'], float(star['mass']), float(star['orbital_radius']),
                                      float(star['simulated_radius']), star['type'], 0, self.vRelative))
            for planet in data['Planets']:
                planets.append(Planet(planet['Name'], float(planet['mass']), float(planet['orbital_radius']),
                                      float(planet['simulated_radius']), planet['type'], float(star['mass']),
                                      self.vRelative))
        return planets

    def getKineticenergy(self):
        """Function used to obtain the kinetic energy of the system at a given time.
        Returns:
            float: Value of the kinetic energy of the system
        """
        kinetic = 0
        for k in range(len(self.celestial_bodies)):
            planet = self.celestial_bodies[k]
            kinetic += planet.mass * 0.5 * planet.velocity.mdoulus() ** 2
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
        Beeman's methods


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
            # if planet.name == "Probe":
            # print(planet.velocity.value_y)
            kinetic += planet.mass * 0.5 * planet.velocity.mdoulus() ** 2
        # print(self.distanceToMars())
        energy = self.getEnergy()
        # print(energy)
        # self.file.write(str(energy)+"\n")
        return energy

    def distanceToMars(self):
        """function used to calculate the distance from the probe to mars at a given time.

        Returns:
            float: distance from the probe to mars
        """
        return Vector.distance(self.celestial_bodies[len(self.celestial_bodies) - 1].position,
                               self.celestial_bodies[4].position).mdoulus()

    def update_euler(self):
        """Method used to update the position, velocity and acceleration of a list of planets
        using Euler-Crommer Method.

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
            kinetic += planet.mass * 0.5 * planet.velocity.mdoulus() ** 2
        energy = self.getEnergy()
        # print(energy)
        # self.file.write(str(energy)+"\n")
        return energy

    def update_initial_acceleration(self):
        """Function use to set the acceleration of the planets as t=0.
        """
        for k in range(len(self.celestial_bodies)):
            others = self.celestial_bodies[:]
            planet = others.pop(k)
            # if (planet.name == "Probe"):
            # print(planet.velocity.value_x)
            planet.update_acceleration(others)
            planet.acceleration_prev = planet.acceleration

    def getPotentialEnergy(self):
        """Function used to get the value of the potential energy of the system at a given time.

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
                distances = Vector.distance(vector1, vector2)
                distance = distances.mdoulus()
                potential += -SolarSystem.G * body_one.mass * body_two.mass / distance
        return potential

