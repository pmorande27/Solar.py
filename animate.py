import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import numpy as np
import math
from matplotlib.animation import FuncAnimation
from Planets import Planet



class animation(object):
    """
    Class used to create the animation of Mars, Deimos and Phobos
    """
    def __init__(self, planets,time_step):
        """
        Constructor of the class, it initizalizes the array of planets/celestial bodies
        """
        self.planets = planets
        self.time_step = time_step

    def init(self):
        # initialiser for animator
        return self.patches

    def animate(self, i):
        """
        Main function of the class, it iterates over the planets and it updates the position of all of them, it will add those new positions to the animation (patches)
        """
        Planet.updatePlanets(self.planets,self.time_step)
        # update the position of the circle
        for j in range(len(self.planets)):
            self.patches[j].center = (self.planets[j].position.get_x(), self.planets[j].position.get_y())
        return self.patches

    def plot(self):
        """
        Method used to create the animation and plot it.
        """
        # set up plot
        fig = plt.figure()
        ax = plt.axes()
        xmin = - 4 * 10 ** 7
        xmax = 4 * 10 ** 7
        ymin = - 4 * 10 ** 7
        ymax = 4 * 10 ** 7
        ax.set_xlim(xmin - 1, xmax)
        ax.set_ylim(ymin - 1, ymax)
        self.patches = []
        colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']

        #Get position of the planets and assing it to the circles.
        for planet in range(len(self.planets)):
            a = plt.Circle((self.planets[planet].position.get_x(), self.planets[planet].position.get_y()),
                           self.planets[planet].simulated_radius, color=colors[planet], animated=True)
            self.patches.append(a)

        # add circles to axes
        for i in range(len(self.patches)):
            ax.add_patch(self.patches[i])

        # Create animation
        anim = FuncAnimation(fig, self.animate, init_func=self.init, frames=10000, repeat=False, interval=100, blit=True)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()
