"""File that contains the SolarSystem class

"""
import json
import math
import numpy as np
from celestial_bodies import CelestialBody
from options import Options


class SolarSystem():
    """Class used to represent the Solar System and mock its behaviour.
    """
    G = 6.67408 * 10 ** -11

    def __init__(self, time_step, v_relative, options,filename):
        """Constructor of the class SolarSytem, used to initialise all
        the planets with the information supplied from a file.

        Args:
            time_step (float): interval between updates (in seconds).
            vRelative (float): speed of the probe relative to the Earth.
            options (Options): Enum used to decide which type of simulation should be launched.
        """
        self.v_relative = v_relative
        self.celestial_bodies = self.input_files(options,filename)
        self.update_initial_acceleration()
        self.options = options
        if options !=Options.PROBE_RUN:
            self.time_step = time_step
            self.initial = False
        else:
            self.set_up_mars()
            self.time_step = 20
            self.real_time_step = time_step
            self.initial = True
        self.time = 0
        self.file = open("./data/energy", "w")
        self.traj = open('./data/traj.xyz','w')
        self.file.write(str(self.get_energy()) + "\n")
        self.updates = 0
        self.centre_of_mass_corrections()
    def  centre_of_mass_corrections(self):
        c_m_momentum = sum([body.mass*body.velocity for body in self.celestial_bodies])
        correction = c_m_momentum/(sum([body.mass for body in self.celestial_bodies]))
        print(correction)
        for body in self.celestial_bodies:
            body.velocity-= correction


    def __del__(self):
        """Deconstructor of the class, used to close the file.
        """
        self.file.close()
    def set_up_mars(self):
        """Sets mars to an appropriate angle for a Hohmann transfer orbit, 44 degrees. (Only used when options is
        PROBE.RUN)
        This will affect the first period of Mars on the simulation which should not be taken into account.
        """

        mars = self.search_body("Mars")
        angle = 44*math.pi*2/360
        x_pos = math.cos(angle)
        y_pos = math.sin(angle)
        mars.position = np.array([x_pos*mars.orbital_radius,y_pos*mars.orbital_radius])
        velocity = np.linalg.norm(mars.velocity)
        mars.velocity = mars.get_initial_velocity(mars.position,velocity)

    def distance_to_earth(self):
        """function used to calculate the distance from the probe to Earth at a given time.
        The Probe's position it is assumed to be the last in the list and Earth the 4th one.

        Returns:
            float: distance from the probe to Earth
        """
        earth = self.search_body("Earth")
        probe = self.search_body("Probe")
        return  np.linalg.norm(-probe.position + earth.position)


    def input_files(self, option,filename):
        """Function used to read all the boides information from the supplied file
        (CelestialObjecs.txt). It will intiatialize all the bodies with the
        required information and it will append them to a list.

        Returns:
            [CelestialBody]: list of all the boidies (object type CelestialBody)
        """
        planets = []
        path = "./data/"+filename
        with open(path) as json_file:
            data = json.load(json_file)
            for star in data['Star']:
                planets.append(CelestialBody(star['Name'], float(star['mass']),
                float(star['orbital_radius']),float(star['simulated_radius']), star['type'],
                0, self.v_relative,star['colour']))
            for planet in data['Planets']:
                if option != Options.PROBE_RUN and planet['Name'] =="Probe":
                    continue
                planets.append(CelestialBody(planet['Name'], float(planet['mass']),
                float(planet['orbital_radius']),float(planet['simulated_radius']),
                 planet['type'], float(star['mass']),
                self.v_relative,planet['colour']))
        return planets
    def write_positions(self,iteration):
        self.traj.write(str(len(self.celestial_bodies))+ "\n")
        self.traj.write("Point = "+str(iteration)+ "\n")
        for body in self.celestial_bodies:
            phrase = "Fr" + " " + str(body.position[0]/(1.496*10**11)) + " " + str(body.position[1]/(1.496*10**11)) + " 0"
            self.traj.write(phrase+"\n")


        pass
    def get_kinetic_energy(self):
        """Function used to obtain the kinetic energy of the system at a given time.
        The Kinetic energy of the system is calculated by iterating through all the bodies
        on a system and adding the individual contributions by the usual formaula,
        K = 1/2mv^2.

        Returns:
            float: Value of the kinetic energy of the system
        """
        kinetic = 0
        for k in range(len(self.celestial_bodies)):
            body = self.celestial_bodies[k]
            kinetic += body.mass * 0.5 * np.linalg.norm(body.velocity)** 2
        return kinetic

    def get_energy(self):
        """Function used to get the total energy of the system, which is the sum of the
        kinetic energy and potential energy at a given time

        Returns:
            float: value of the total energy.
        """
        return self.get_potential_energy() + self.get_kinetic_energy()

    def update_beeman(self):
        """Method used to update the position, velocity and acceleration of a list of CelestialBodies using
        Beeman's methods. First the positions of all the bodies are updated, then the velocities
        of all of them, which also updates the accelerations. TO obtain good results it is
        important to do it in these 'blocks', otherwise the update on the position of one
        body could affect the update on the position of another body
        (if the updates were done in only one block)
        Returns:
            int: Energy of the system after the update
        """
        # Variable Time-Step
        if self.options==Options.PROBE_RUN:
            # Time-Step small at launch
            if self.initial:
                if self.distance_to_earth() >= 10**8:
                    self.initial = False
                    self.time_step = self.real_time_step
            # Time-step small when approaching Mars
            elif self.distance_to_mars() >= 10**8 and not self.initial:
                self.time_step = self.real_time_step
            else:
                self.time_step = 50
        self.updates += 1

        # Update positions of all planets from time t-timestep to time t
        for k in range(len(self.celestial_bodies)):
            others = self.celestial_bodies[:]
            planet = others.pop(k)
            planet.update_position_beeman(self.time_step)

        # Update velocities of all planets from time t-timestep to time t
        for k in range(len(self.celestial_bodies)):
            others = self.celestial_bodies[:]
            planet = others.pop(k)
            planet.update_velocity_beeman(self.time_step, others)
        
        energy = self.get_energy()
        self.file.write(str(energy)+"\n")
        self.time += self.time_step
        self.write_positions(self.updates)
        return energy

    def distance_to_mars(self):
        """function used to calculate the distance from the probe to mars at a given time.
        The Probe's position it is assumed to be the last in the list and mars the 5th one.

        Returns:
            float: distance from the probe to mars
        """
        mars = self.search_body("Mars")
        probe = self.search_body("Probe")
        return  np.linalg.norm(probe.position-
                               mars.position)
    def search_body(self,name):
        for body in self.celestial_bodies:
            if body.name == name:
                return body
        raise ValueError("The given name is not in the actual list of bodies")
    def update_euler(self):
        """Method used to update the position, velocity and acceleration of a list of bodies
        using Euler-Crommer Method. The accelerations are updated to time t,
        then all the velcoities are updated to time t + dt and finally all
        the positions are updated at time t+dt.

        Returns:
            int : returns the energy of the system after the update.
        """
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
        energy = self.get_energy()
        return energy

    def update_initial_acceleration(self):
        """Function used to set the acceleration of the planets as t=0.
        This is important for the Beeman's Method.
        """
        for k in range(len(self.celestial_bodies)):
            others = self.celestial_bodies[:]
            planet = others.pop(k)
            planet.update_acceleration(others)
            planet.acceleration_prev = planet.acceleration

    def get_potential_energy(self):
        """Function used to get the value of the potential energy of
        the system at a given time. The energy is given by the sum of the individual
        contributions, each pair of bodies contributes whith -GmM/r^2.

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
