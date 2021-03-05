from vector import Vector

class Planet(object):
    G = 6.67408 * 10 ** -11

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
            self.velocity = Vector(0,(Planet.G*central_mass/orbital_radius)**0.5)

        # Set-up acceleration and radius
        self.acceleration = Vector(0, 0)
        self.simulated_radius = simulated_radius

    def update_position(self,time_step):
        """
        Method used to update position using Euler integration method
        """
        self.position += self.velocity * time_step

    def update_velocity(self,time_step):
        """
        Method used to update velocity using Euler integration method
        """
        self.velocity += self.acceleration * time_step

    def update_acceleration(self, others):
        """
        Method used to update acceleration by adding the acceleration due to the gravitational force between the different bodies
        """
        #Restart acceleration of the object
        self.acceleration = Vector(0,0)

        #Update acceleration by adding the acceleration due to the gravitational interaction between the body and each of the other bodies.
        for i in range(len(others)):
            planet2 = others[i]
            vector1 = self.position
            vector2 = planet2.position
            distances = Vector.distance(vector1, vector2)
            self.acceleration += (distances/ distances.mdoulus()) * (others[i].mass * Planet.G / (distances.mdoulus()**2)) 
    @staticmethod
    def updatePlanets(planets,time_step):
        """
        Method used to update the position of a list of planets
        """
        kinetic =0 

        #Update acceleration and velocity of all planets from time t-timestep to time t
        for k in range(len(planets)):
            others = planets[:]
            planet = others.pop(k)
            planet.update_acceleration(others)
            planet.update_velocity(time_step)

        #Update position of all planets from time t-timestep to time t
        for k in range(len(planets)):
            others = planets[:]
            planet = others.pop(k)
            planet.update_position(time_step)
            kinetic += planet.mass*0.5*planet.velocity.mdoulus()**2

        print(kinetic)



