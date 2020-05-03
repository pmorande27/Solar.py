def magnitude(vector):
    result = (vector[0] ** 2 + vector[1] ** 2) ** 0.5
    return result


def distance(vector1, vector2):
    result = [vector2[0] - vector1[0], vector2[1] - vector1[1]]
    return result


G = 6.67 * 10 ** -11
time_step = 100


class Planet(object):

    def __init__(self, name, mass, position_x, position_y, velocity_x, velocity_y, acceleration_x, acceleration_y,
                 orbital_radius, simulated_radius):
        self.name = name
        self.mass = mass
        self.position = [position_x, position_y]
        self.velocity = [velocity_x, velocity_y]
        self.acceleration = [acceleration_x, acceleration_y]
        self.orbital_radius = orbital_radius
        self.simulated_radius = simulated_radius

    def update_position(self, others):
        self.update_acceleration(others)
        for i in range(2):
            self.velocity[i] += self.acceleration[i] * time_step
            self.position[i] += self.velocity[i] * time_step
        print(self.velocity)

    def update_acceleration(self, others):
        self.acceleration = [0, 0]
        for i in range(len(others)):
            planet2 = others[i]
            for j in range(2):
                vector1 = self.position
                vector2 = planet2.position
                distances = distance(vector1, vector2)
                self.acceleration[j] += (others[i].mass * G / magnitude(distances) ** 2) * (
                        distances[j] / magnitude(distances))




