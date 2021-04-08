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
def periods_graph(updates):
    system = SolarSystem(3600, 10.175 * 10 ** 3, Options.NORMAL_RUN,"CelestialObjects")
    values = []
    for i in range(updates):
        system.update_beeman()
    l = 0
    actual_values = [88.0,224.7,365.2,687.0	]
    for j in system.celestial_bodies:

        if j.name != "Sun":
            period = sum(j.periods)/(len(j.periods))
            l+=1
            values.append(period)
    fig, ax = plt.subplots()
    width = 0.35       # the width of the bars: can also be len(x) sequence
    labels = ["Mercury","Venus","Earth","Mars"]
 
# Text on the top of each bar  
    rects1 = ax.bar(labels, values, width)
    ax.set_ylabel('Days')
    ax.set_title('Average Orbital Periods')
    ax.bar_label(rects1, padding=3)
    plt.show()




def EnergyGraphComparisson(updates):
    """Function used to generate a comparison graph between Euler's method and Beeman's 
    to show conservation (or not conservation) of energy in both methods
    """
    system = SolarSystem(3600, 10.175 * 10 ** 3, Options.NORMAL_RUN,"CelestialObjects")
    energy_1 = []
    system2 = SolarSystem(3600, 10.175 * 10 ** 3, Options.NORMAL_RUN,"CelestialObjects")
    energy_2 = [system2.getEnergy()]
    iterate = updates
    iterations = [(i+1)*3600 for i in range(iterate)]
    for i in range(iterate):
        energy_1.append(system.update_beeman())
        energy_2.append(system2.update_euler())
    plt.xlabel('time(s)')
    plt.ylabel('Energy [J]')
    plt.plot(iterations,energy_1,label="System With Beeman Updates")
    plt.legend(loc="upper left")
    plt.show()


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
