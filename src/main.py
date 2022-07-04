"""File to hold the main of the project
"""
from animate import Animation
from solar_system import SolarSystem
from options import Options


def main():
    """
    Main function
    """
   
    system = SolarSystem(3600, 11.5517 * 10 ** 3,Options.PROBE_RUN,"CelestialObjects")
    animate = Animation(system)
    #animate.plot()
    #Animation.periods_graph(10000*2,SolarSystem(3600, 11.5517 * 10 ** 3,Options.NORMAL_RUN,"CelestialObjects"))
    animate.scatter_plot(100000*2)
    #print(search_velocity_to_mars(10000,1,11.5517 * 10 ** 3))
    #Animation.energy_graph_comparisson(10000*2)


def search_velocity_to_mars(updates,tries,velocity):
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
    minimum = system.distance_to_mars()
    for i in range(tries):
        system = SolarSystem(3600, start_velocity + i * increment,
                            Options.PROBE_RUN,"CelestialObjects")
        for j in range(updates):
            system.update_beeman()
            if minimum >= system.distance_to_mars():
                minimum = system.distance_to_mars()
                min_v = start_velocity + i * increment
    return (minimum, min_v)

if __name__ == "__main__":
    main()
