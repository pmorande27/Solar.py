from animate import Animation
from Planet import Planet
from solar_system import SolarSystem
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from options import Options
import matplotlib


def main():
    """
    Main function
    """
    """
    writeFile()
    system = SolarSystem(1000,10.5013*10**3)
    animate = animation(system)
    """
    system = SolarSystem(3600, 11.5517 * 10 ** 3,Options.PROBE_RUN,"CelestialObjects")
    animate = Animation(system)
    #11.56
    #animate.plot()
    #periods_graph(10000*2)
    animate.scatterplot(10000*2)
    #print(searchVelocityToMars(10000,1,11.551 * 10 ** 3))
    #EnergyGraphComparisson(10000*2)


def searchVelocityToMars(updates,tries,velocity):
    """Function used to searc for the optimal velocity for the probe to approach mars
    it will do it by try and error over different values.

    Returns:
        (float,float): tuple of distance the minimum distance found and the speed needed to
        accomplish it.
    """
    start_velocity = velocity
    system = SolarSystem(3600, start_velocity, Options.PROBE_RUN,"CelestialObjects")
    min_v = 0
    increment = 0.001
    minimum = system.distanceToMars()
    for i in range(tries):
        system = SolarSystem(3600, start_velocity + i * increment, Options.PROBE_RUN,"CelestialObjects")
        for j in range(updates):
            system.update_beeman()
            if minimum >= system.distanceToMars():
                minimum = system.distanceToMars()
                min_v = start_velocity + i * increment
    return (minimum, min_v)

if __name__ == "__main__":
    main()
