import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import numpy as np
import math
from matplotlib.animation import FuncAnimation
from Planets import Planet

class animation(object):
    def __init__(self, planets):
        self.planets = planets
        self.kinetic = 0

    def init(self):
        # initialiser for animator
        return self.patches

    def animate(self, i):
        self.kinetic =0 

        for k in range(len(self.planets)):
            others = self.planets[:]
            self.planet = others.pop(k)
            self.planet.update_acceleration(others)
            self.planet.update_velocity()

        for k in range(len(self.planets)):
            others = self.planets[:]
            self.planet = others.pop(k)
            self.planet.update_position()
            self.kinetic += self.planet.mass*0.5*self.planet.velocity.mdoulus()**2
            # update the position of the circle
        print(self.kinetic)
        for j in range(len(self.planets)):
            self.patches[j].center = (self.planets[j].position.get_x(), self.planets[j].position.get_y())
        return self.patches

    def plot(self):

        # set up plot
        fig = plt.figure()
        ax = plt.axes()

        xmin = - 4 * 10 ** 7
        xmax = 4 * 10 ** 7
        ymin = - 4 * 10 ** 7
        ymax = 4 * 10 ** 7

        ax.axis('scaled')
        ax.set_xlim(xmin - 1, xmax)
        ax.set_ylim(ymin - 1, ymax)

        self.patches = []

        colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
        for planet in range(len(self.planets)):
            a = plt.Circle((self.planets[planet].position.get_x(), self.planets[planet].position.get_y()),
                           self.planets[planet].simulated_radius, color=colors[planet], animated=True)
            self.patches.append(a)

        # add circles to axes
        for i in range(len(self.patches)):
            ax.add_patch(self.patches[i])

        anim = FuncAnimation(fig, self.animate, init_func=self.init, frames=10000, repeat=False, interval=50, blit=True)

        plt.show()
