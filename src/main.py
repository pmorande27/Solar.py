from animate import Animation
from Planet import Planet
from solar_system import SolarSystem
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from options import Options


def main():
    """
    Main function
    """
    """
    writeFile()
    system = SolarSystem(1000,10.5013*10**3)
    animate = animation(system)
    """
    system = SolarSystem(10000, 11.5605 * 10 ** 3,Options.PROBE_RUN,"CelestialObjects")
    animate = Animation(system)
    #animate.plot()
    animate.scatterplot(10000*5)
    #print(searchVelocityToMars(10000*2,1,11.56 * 10 ** 3))
    # EnergyGraphComparisson()


def EnergyGraphComparisson(updates):
    """Function used to generate a comparison graph between Euler's method and Beeman's 
    to show conservation (or not conservation) of energy in both methods
    """
    system = SolarSystem(3600, 10.175 * 10 ** 3, Options.NORMAL_RUN,"CelestialObjects")
    energy_1 = []
    system2 = SolarSystem(3600, 10.175 * 10 ** 3, Options.NORMAL_RUN,"CelestialObjects")
    energy_2 = []
    iterate = updates
    iterations = [i for i in range(iterate)]
    for i in range(iterate):
        energy_1.append(system.update_beeman())
        energy_2.append(system2.update_euler())
    plt.plot(iterations, energy_1, iterations, energy_2)
    plt.show()


def searchVelocityToMars(updates,tries,velocity):
    """Function used to searc for the optimal velocity for the probe to approach mars
    it will do it by try and error over different values.

    Returns:
        (float,float): tuple of distance the minimum distance found and the speed needed to
        accomplish it.
    """
    start_velocity = velocity
    system = SolarSystem(10000, start_velocity, Options.PROBE_RUN,"CelestialObjects")
    min_v = 0
    increment = 0.001
    minimum = system.distanceToMars()
    for i in range(tries):
        system = SolarSystem(10000, start_velocity + i * increment, Options.PROBE_RUN,"CelestialObjects")
        for j in range(updates):
            system.update_beeman()
            if minimum >= system.distanceToMars():
                minimum = system.distanceToMars()
                min_v = start_velocity + i * increment
    return (minimum, min_v)

if __name__ == "__main__":
    main()
