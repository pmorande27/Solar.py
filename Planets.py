from vector import Vector
import matplotlib.pyplot as plt
import math


class Planet(object):
    G = 6.67408 * 10 ** -11

    def __init__(self, name, mass, orbital_radius, simulated_radius, type_of_object, central_mass, vRelative):
        """
        Constructor of the class used to initziled important fields such as the mass, the position, acceleration and velocity of the object.
        """
        self.time = 0
        self.name = name
        self.mass = mass
        self.type_of_object = type_of_object
        self.orbital_radius = orbital_radius

        # Case the object is supposed to be at the centre at the start
        if type_of_object == "Star":
            self.position = Vector(0, 0)
            self.velocity = Vector(0, 0)

        # Case for orbiting objects
        elif type_of_object == "Planet":
            self.position = Vector(orbital_radius, 0)
            self.velocity = Vector(0, (Planet.G * central_mass / orbital_radius) ** 0.5)
            self.sign = 1
        # Set-up acceleration and radius
        elif type_of_object == "Probe":
            self.position = Vector(orbital_radius, 6.02 * 10 ** 6)
            self.velocity = Vector(0, 29.8 * 10 ** 3 + vRelative)
        self.acceleration = Vector(0, 0)
        self.acceleration_prev = Vector(0, 0)
        self.simulated_radius = simulated_radius

    def update_position_euler(self, time_step):
        """
        Method used to update position using Euler integration method
        """
        self.position += self.velocity * time_step

    def update_velocity_euler(self, time_step):
        """
        Method used to update velocity using Euler integration method
        """
        self.velocity += self.acceleration * time_step

    def update_position_beeman(self, time_step):
        """
        Method used to update position using Euler integration method
        """

        if self.type_of_object == "Planet":
            previous = self.sign

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
        """
        Method used to update velocity using Beeman integration method
        """
        acceleration_current = self.acceleration.__copy__()
        self.update_acceleration(others)
        c = self.acceleration * 2
        d = acceleration_current * 5
        f = self.acceleration_prev * -1
        a = (self.acceleration * 2 + acceleration_current * 5 - self.acceleration_prev) * time_step / 6
        self.velocity += a
        self.acceleration_prev = acceleration_current

    def update_acceleration(self, others):
        """
        Method used to update acceleration by adding the acceleration due to the gravitational force between the different bodies
        """
        # Restart acceleration of the object
        self.acceleration = Vector(0, 0)
        # Update acceleration by adding the acceleration due to the gravitational interaction between the body and
        # each of the other bodies.
        for i in range(len(others)):
            planet2 = others[i]
            vector1 = self.position
            vector2 = planet2.position
            distances = Vector.distance(vector1, vector2)
            self.acceleration += (distances / distances.mdoulus()) * (
                        others[i].mass * Planet.G / (distances.mdoulus() ** 2))

    def get_y_sign(self):
        if self.position.get_y() >= 0:
            return 1
        else:
            return -1

    @staticmethod
    def angleBetweenPlanets(planet_A, planet_B):
        position_A = planet_A.position
        position_B = planet_B.position
        angle_in_radians = math.acos(Vector.scalar_product(position_A, position_B) / (position_A.mdoulus() * position_B.mdoulus()))
        return angle_in_radians*360/(2*math.pi)