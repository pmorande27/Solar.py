from animate import animation
from Planet import Planet
from SolarSystem import SolarSystem
import numpy as np
import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from helperfunctions import writeFile


def main():
    """
    Main function
    """
    """
    writeFile()
    system = SolarSystem(1000,10.5013*10**3)
    animate = animation(system)
    """
    system = SolarSystem(100, 10.175 * 10 ** 3)
    animate = animation(system)
    # animate.plot()
    animate.scatterplot(10000 * 30)
    # EnergyGraphComparisson()


def EnergyGraphComparisson():
    """Function used to generate a comparison graph between Euler's method and Beeman's 
    to show conservation (or not conservation) of energy in both methods
    """
    system = SolarSystem(3600, 10.175 * 10 ** 3)
    energy_1 = []
    system2 = SolarSystem(3600, 10.175 * 10 ** 3)
    energy_2 = []
    iterate = 10000
    iterations = [i for i in range(iterate)]
    for i in range(iterate):
        print(i)
        energy_1.append(system.update_beeman())
        energy_2.append(system2.update_euler())
    plt.plot(iterations, energy_1, iterations, energy_2)
    plt.show()


def searchVelocityToMars():
    """Function used to searc for the optimal velocity for the probe to approach mars
    it will do it by try and error over different values.

    Returns:
        (float,float): tuple of distance the minimum distance found and the speed needed to
        accomplish it.
    """
    tries = 100
    updates = 10000 * 40
    start_velocity = 10.175 * 10 ** 3
    system = SolarSystem(100, start_velocity)
    min_v = 0
    increment = 0.001
    minimum = system.distanceToMars()
    print(minimum)
    for i in range(tries):
        print(i)
        system = SolarSystem(240, start_velocity + i * increment)
        for i in range(updates):
            system.update_beeman()
            if minimum > system.distanceToMars():
                minimum = system.distanceToMars()
                min_v = start_velocity + i * increment
                print(minimum)
    return (minimum, min_v)

if __name__ == "__main__":
    main()
