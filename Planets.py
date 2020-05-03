class Planets(object):
    G = 6.67 * 10 ** (-11)
    timestep = 100
    def __init__(self,name,mass, positionX, positionY,velocityX,velocityY,orbitalRadius,simulatedRadius, accelerationX,accelerationY);
        self.name = name
        self.positionX = positionX
        self.mass = mass
        self.positionY = positionY
        self.position = [positionX,positionY]
        self.velocity = [velocityX,velocityY]
        self.orbitalRadius = orbitalRadius
        self.simulatedRadius =simulatedRadius
        self.accelerationX = accelerationX
        self.accelerationY = accelerationY
    def __magnitude(vector):
        result =0
        for i in range(len(vector)):
            result += vector[i]**2
        return result**0.5
    def distance(vector1,vector2):
        result = [vector2[1]-vector1[1]), (vector2[2]-vector1[2])]
    def accelearion (self, otherplanets):
        for i in range(2):    
            for j in range(len(otherplanets)):
                planet2 = otherplanets[j]
                vector1 = [self.positionX,self.positionY]
                vector2 = [planet2.positionX, planet2.positionY]
                distance = distance(vector1,vector2)
                
                acceleration[j] =acceleration[j] (G*planet2.mass/(magnitude(distance))**2) * (distance[i]/magnitude(distance))
        return acceleration
    def updateposition(self, otherplanets,):
        acceleration = self.accelaration(otherplanets)
        for i in range(2):
            self.velocity[i] =velocity[i] +  acceleration[i]*timestep
            self.position[i] = position[i] + velocity[i]*timestep
            

            


