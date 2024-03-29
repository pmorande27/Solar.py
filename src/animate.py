"""File to hold the Animation class
"""
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
from solar_system import SolarSystem
from options import Options
class Animation():
    """Class used to create the animation of the solar System and to plot any needed graph
    """
    def __init__(self, solar_system):
        """Constructor of the class, it initizalizes the array of planets/celestial bodies
        Args:
            SolarSystem (SolarSystem): Solar System to animate
        """
        self.system = solar_system
        self.updates = 0
    def scatter_plot(self,max_updates):
        """Method used to generate the plot of the orbits generated by updating
        the system a fixed number of times.
        Args:
            maxUpdates (int): number of iterations
        """
        positions = [[] for x in range(len(self.system.celestial_bodies))]
        axis = plt.axes()
        xmin = -10 * 10 ** 11
        xmax = 10 * 10 ** 11
        ymin = - 10 * 10 ** 11
        ymax = 10 * 10 ** 11
        axis.set_xlim(xmin - 1, xmax)
        axis.set_ylim(ymin - 1, ymax)
        for updates in range(max_updates):
            self.system.update_beeman()
            planets = self.system.celestial_bodies
            for i in range(len(planets)):
                positions[i].append((planets[i].position[0],planets[i].position[1]))
        for j in range(len(positions)):
            position_x,position_y = zip(*positions[j])
            plt.plot(position_x,position_y,color=self.system.celestial_bodies[j].colour,
                    label =self.system.celestial_bodies[j].name )
        plt.legend(loc="upper left")
        plt.xlabel('x[m]')
        plt.ylabel('y[m]')
        plt.show()


    def init(self):
        """initialiser for animator
        """
        # initialiser for animator
        return self.patches

    def animate(self, i):
        """Main function of the class, it iterates over the planets and it updates the position
        of all of them, it will add those new positions to the animation (patches)
        Args:
            i (int): number of update

        Returns:
            Patches: patches
        """
        self.system.update_beeman()
        self.updates+=1
        #print(self.updates)
        planets = self.system.celestial_bodies
        # update the position of the circle
        for j in range(len( planets)):
            self.patches[j].center = (planets[j].position[0], planets[j].position[1])
        return self.patches

    def plot(self):
        """Method used to create the animation and plot it.

        """
        # set up plot
        fig = plt.figure()
        axis = plt.axes()
        xmin = - 10 * 10 ** 11
        xmax = 10 * 10 ** 11
        ymin = - 10 * 10 ** 11
        ymax = 10 * 10 ** 11
        axis.set_xlim(xmin - 1, xmax)
        axis.set_ylim(ymin - 1, ymax)
        self.patches = []
        planets = self.system.celestial_bodies
        #Get position of the planets and assing it to the circles.
        for planet in range(len(planets)):
            body = plt.Circle((planets[planet].position[0], planets[planet].position[1]),
                           planets[planet].simulated_radius, color=planets[planet].colour,
                           animated=True)
            self.patches.append(body)

        # add circles to axes
        for i in range(len(self.patches)):
            axis.add_patch(self.patches[i])

        # Create animation
        anim = FuncAnimation(fig, self.animate, init_func=self.init, frames=10000000,
                            repeat=False, interval=0, blit=True)
        plt.xlabel('x[m]')
        plt.ylabel('y[m]')
        plt.show()
    @staticmethod
    def periods_graph(updates,system):
        """Method used to generate a graph with the average values of the orbital 
        periods of the different planets on the Solar System.

        Args:
            updates (int): number of updates to the system, must be a hight number to allow
            mars to complete its period.
        """
        values = []
        for i in range(updates):
            system.update_beeman()
        for j in system.celestial_bodies:

            if j.name != "Sun":
                period = sum(j.periods)/(len(j.periods))
                values.append(period)
        figure, axis= plt.subplots()
        width = 0.35       # the width of the bars: can also be len(x) sequence
        labels = ["Mercury","Venus","Earth","Mars"]
        # Text on the top of each bar
        rects1 = axis.bar(labels, values, width)
        axis.set_ylabel('Days')
        axis.set_title('Average Orbital Periods')
        axis.bar_label(rects1, padding=3)
        plt.show()
    @staticmethod
    def energy_graph_comparisson(updates):
        """Function used to generate a comparison graph between Euler's method and Beeman's
        to show conservation (or not conservation) of energy in both methods
        """
        system = SolarSystem(3600, 10.175 * 10 ** 3, Options.NORMAL_RUN,"CelestialObjects")
        energy_1 = [system.get_energy()]
        system2 = SolarSystem(3600, 10.175 * 10 ** 3, Options.NORMAL_RUN,"CelestialObjects")
        energy_2 = [system2.get_energy()]
        iterate = updates
        iterations = [i*3600 for i in range(iterate+1)]
        for i in range(iterate):
            energy_1.append(system.update_beeman())
            energy_2.append(system2.update_euler())
        plt.xlabel('time(s)')
        plt.ylabel('Energy [J]')
        plt.plot(iterations, energy_1, iterations, energy_2)
        plt.show()
