import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import numpy as np
import math
from matplotlib.animation import FuncAnimation
class animation(object):
    """
    Class used to create the animation of Mars, Deimos and Phobos
    """
    def __init__(self, SolarSystem):
        """
        Constructor of the class, it initizalizes the array of planets/celestial bodies
        """
        self.System = SolarSystem
        self.updates = 0
    def scatterplot(self,maxUpdates):
        positions = [[] for x in range(len(self.System.celestial_bodies))]
        ax = plt.axes()
        xmin = - 3 * 10 ** 11
        xmax = 3 * 10 ** 11
        ymin = - 3 * 10 ** 11
        ymax = 3 * 10 ** 11
        ax.set_xlim(xmin - 1, xmax)
        ax.set_ylim(ymin - 1, ymax)
        for updates in range(maxUpdates):
            self.System.update_beeman()
            planets = self.System.celestial_bodies
            for i in range(len(planets)):
                positions[i].append((planets[i].position.get_x(),planets[i].position.get_y()))
        for j in range(len(positions)):
            position_x,position_y = zip(*positions[j])
            plt.plot(position_x,position_y)
        plt.show()


    def init(self):
        # initialiser for animator
        return self.patches

    def animate(self, i):
        """
        Main function of the class, it iterates over the planets and it updates the position of all of them, it will add those new positions to the animation (patches)
        """
        self.System.update_beeman()
        self.updates+=1
        #print(self.updates)
        planets = self.System.celestial_bodies
        # update the position of the circle
        for j in range(len( planets)):
            self.patches[j].center = (planets[j].position.get_x(), planets[j].position.get_y())
        return self.patches

    def plot(self):
        """
        Method used to create the animation and plot it.
        """
        # set up plot
        fig = plt.figure()
        ax = plt.axes()
        xmin = - 4 * 10 ** 11
        xmax = 4 * 10 ** 11
        ymin = - 4 * 10 ** 11
        ymax = 4 * 10 ** 11
        ax.set_xlim(xmin - 1, xmax)
        ax.set_ylim(ymin - 1, ymax)
        self.patches = []
        colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
        planets = self.System.celestial_bodies
        #Get position of the planets and assing it to the circles.
        for planet in range(len(planets)):
            a = plt.Circle((planets[planet].position.get_x(), planets[planet].position.get_y()),
                           planets[planet].simulated_radius, color=colors[planet], animated=True)
            self.patches.append(a)

        # add circles to axes
        for i in range(len(self.patches)):
            ax.add_patch(self.patches[i])

        # Create animation
        anim = FuncAnimation(fig, self.animate, init_func=self.init, frames=10000000, repeat=False, interval=0, blit=True)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()
