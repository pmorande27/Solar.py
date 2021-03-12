from animate import animation
from Planets import Planet
from SolarSystem import SolarSystem
import numpy as np
import matplotlib.pyplot as plt


def main():
    """
    Main function
    """
    system = SolarSystem(1000)
    animate = animation(system)
    animate.plot()
    #EnergyGraphComparisson()

def EnergyGraphComparisson():
    system = SolarSystem(1000)
    energy_1 = [system.getEnergy()]
    system2 = SolarSystem(1000)
    energy_2 = [system2.getEnergy()]
    iterate = 100000
    iterations = [i for i in range(iterate+1)]
    for i in range(iterate):
        print(i)
        energy_1.append(system.update_beeman())
        energy_2.append(system2.update_euler())
    plt.plot(iterations,energy_1,iterations,energy_2)
    plt.show()


main()

