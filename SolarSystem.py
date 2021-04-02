import json
from Planets import Planet
from vector import Vector


class SolarSystem(object):
    G = 6.67408 * 10 ** -11

    def __init__(self, time_step, vRelative):
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
        self.file.close()

    def inputFiles(self):
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
        kinetic = 0
        for k in range(len(self.celestial_bodies)):
            planet = self.celestial_bodies[k]
            kinetic += planet.mass * 0.5 * planet.velocity.mdoulus() ** 2
        return kinetic

    def getEnergy(self):
        return self.getPotentialEnergy() + self.getKineticenergy()

    def update_beeman(self):
        """
        Method used to update the position of a list of planets
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
        return Vector.distance(self.celestial_bodies[len(self.celestial_bodies) - 1].position,
                               self.celestial_bodies[4].position).mdoulus()

    def update_euler(self):
        """
        Method used to update the position of a list of planets
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
        for k in range(len(self.celestial_bodies)):
            others = self.celestial_bodies[:]
            planet = others.pop(k)
            # if (planet.name == "Probe"):
            # print(planet.velocity.value_x)
            planet.update_acceleration(others)
            planet.acceleration_prev = planet.acceleration

    def getPotentialEnergy(self):
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

