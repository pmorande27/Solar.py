import matplotlib.pyplot as plt
import math
import numpy as np


class Planet(object):
    G = 6.67408 * 10 ** -11

    def __init__(self, name, mass, orbital_radius, simulated_radius, type_of_object, central_mass, vRelative):
        """Constructor of the class used to initsile important fields such as the mass, the position, acceleration and velocity of the object.
        Args:
            name (string): Name of the Celestial body
            mass (float): mass of the Celestial body
            orbital_radius (float): orbital radius of Celestial body (assumed)
            simulated_radius (int): radius of the circle that represent such body in the animation
            type_of_object (string): type of Celestial body, can be star, planet or probe
            central_mass (float): mass for the centras potential approximation to calculate the initial variables.
            vRelative (float): relativ velocity, only used for the probe case.
        """
        self.time = 0
        self.name = name
        self.mass = mass
        self.type_of_object = type_of_object
        self.orbital_radius = orbital_radius

        # Case the object is supposed to be at the centre at the start
        if type_of_object == "Star":
            self.position = np.array([0.0,0.0])
            self.velocity = np.array([0.0,0.0])
            print(self.position)

        # Case for orbiting objects
        elif type_of_object == "Planet":
            self.position = np.array([orbital_radius, 0.0])
            velocity =(Planet.G * central_mass / orbital_radius) ** 0.5
            self.velocity =np.array([0.0,math.sqrt(Planet.G * central_mass / orbital_radius)])
            self.sign = 1
            print(self.velocity)
        # Case for the Probe
        elif type_of_object == "Probe":
            self.position = np.array([orbital_radius, 6.02 * 10 ** 6])
            self.velocity = np.array([0.0, 29.8 * 10 ** 3 + vRelative])
        # Set-up acceleration and radius
        self.acceleration = np.array([0.0,0.0])
        self.acceleration_prev = np.array([0.0,0.0])
        self.simulated_radius = simulated_radius
    
    def getInitialVelocity(self,position,velocity):
        """Method used to get the correct tangential velocity of an object orbiting. This is calculated by
        taking the perpendicular vector to the position (constained in the orbit's plane) and multiply it by the
        modulus (norm) of the velocity.

        Args:
            position ([float]): Numpy Array containing the position of the object
            velocity (float): modulus of the velocity.

        Returns:
            [float]: returns the new velocity vector tangent to the orbit's trajectory.
        """
        unit_vector = position/np.linalg.norm(position)
        unit_tangent = np.array([-unit_vector[1], unit_vector[0]])
        return velocity*unit_tangent

    def update_position_euler(self, time_step):
        """Method used to ipdate the position of a Celestial Body using Euler-Crommer's method.

        Args:
            time_step (float): time between updates.
        """
        self.position += self.velocity * time_step

    def update_velocity_euler(self, time_step):
        """Method used to ipdate the velocity  of a Celestial Body  using Euler-Crommer's method.

        Args:
            time_step (float): time between updates.
        """
        self.velocity += self.acceleration * time_step

    def update_position_beeman(self, time_step):
        """Method used to ipdate the position  of a Celestial Body  using Beeman's method.

        Args:
            time_step (float): time between updates.
        """
        self.position += self.velocity * time_step + (
                    self.acceleration * 4 - self.acceleration_prev) * time_step * time_step / 6

        if self.type_of_object == "Planet":
            previous = self.sign
            self.sign = self.get_y_sign()
            if previous < self.sign:
                time = self.time / (3600 * 24)
                print("Orbital Period of " + self.name + " is " + str(time) + " days")
                self.time = 0
            else:
                self.time += time_step

    def update_velocity_beeman(self, time_step, others):
        """Method used to ipdate the velocity of a Celestial Body  using Beeman's method.

        Args:
            time_step (float): time between updates.
        """
        acceleration_current = np.copy(self.acceleration)
        self.update_acceleration(others)
        a = (self.acceleration * 2 + acceleration_current * 5 - self.acceleration_prev) * time_step / 6
        self.velocity += a
        self.acceleration_prev = acceleration_current

    def update_acceleration(self, others):
        """Method used to update the acceleration of a body taking into account the gravitational pull of the other
        bodies in the system.

        Args:
            others ([Planet]): other Celestial Bodies that influence the total acceleration of the given body.
        """
        # Restart acceleration of the object
        self.acceleration = np.array([0.0, 0.0])
        # Update acceleration by adding the acceleration due to the gravitational interaction between the body and
        # each of the other bodies.
        for i in range(len(others)):
            #print("hola")
            planet2 = others[i]
            vector1 = self.position
            vector2 = planet2.position
            #print(vector1)
            #print(vector2)
            distances =  vector2-vector1
            self.acceleration += (distances / np.linalg.norm(distances)) * (
                        others[i].mass * Planet.G / (np.linalg.norm(distances) ** 2))

    def get_y_sign(self):
        """Method used to get the sign of the y-position of a planet, useful to calculate the orbital period of the planets
        during the simulation.

        Returns:
            int: 1 if the sign is positive and -1 if it is negative
        """
        if self.position[1] >= 0:
            return 1
        else:
            return -1

    @staticmethod
    def angleBetweenPlanets(planet_A, planet_B):
        """Static Method used to find the angle between two planets (using the postion vector)

        Args:
            planet_A (Planet): Body A
            planet_B (Planet): Body B 

        Returns:
            float: anlge between the two position vectors.
        """
        pass