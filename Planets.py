from vector import Vector
G = 6.67408 * 10 ** -11
time_step = 100
class Planet(object):

    def __init__(self, name, mass, orbital_radius, simulated_radius,type_of_object,central_mass):
        """
        Constructor of the class used to initziled important fields such as the mass, the position, acceleration and velocity of the object.
        """
        self.name = name
        self.mass = mass

        # Case the object is supposed to be at the centre at the start
        if type_of_object == "Planet":
            self.position = Vector(0,0)
            self.velocity = Vector(0,0)

        # Case for orbiting objects
        elif type_of_object == "Moon":
            self.position = Vector(orbital_radius,0)
            self.velocity = Vector(0,(G*central_mass/orbital_radius)**0.5)

        # Set-up acceleration and radius
        self.acceleration = Vector(0, 0)
        self.simulated_radius = simulated_radius

    def update_position(self):
        """
        Method used to update position using 
        """
        self.position += self.velocity * time_step

    def update_velocity(self):
        self.velocity += self.acceleration * time_step

    def update_acceleration(self, others):
        self.acceleration = Vector(0,0)
        for i in range(len(others)):
            planet2 = others[i]
            vector1 = self.position
            vector2 = planet2.position
            distances = Vector.distance(vector1, vector2)
            self.acceleration += (distances/ distances.mdoulus()) * (others[i].mass * G / (distances.mdoulus()**2)) 




