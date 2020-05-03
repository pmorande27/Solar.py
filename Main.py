from animate import animation
from Planets import Planet


def main():

    b = Planet("marte", 6.4*10**23, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 500000)
    e = Planet("phonos",10600000000000000.0,9377300.0,0,0,2133,0,0,0,500000)
    d = [b, e]
    a = animation(d)
    a.plot()


main()
