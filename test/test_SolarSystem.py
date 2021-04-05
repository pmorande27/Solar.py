import unittest
import sys
import os
sys.path.append('../src')
from SolarSystem import SolarSystem
sys.path.append('../src/utils')
import helperfunctions
from Options import Options
import numpy as np
import math
from Planet import Planet
class TestSolarSystem(unittest.TestCase):
    def setUp(self):
        self.system_probe = SolarSystem(3600,10000,Options.PROBE_RUN,"CelestialObjects")
        self.system = SolarSystem(3600,10000,Options.NORMAL_RUN,"CelestialObjects")
        self.system_simple = SolarSystem(3600,10000,Options.NORMAL_RUN,"CelestialObjects")
        planetA = Planet("B",1,1,1,"Planet",1,10000)
        star = Planet("A",1,1,1,"Star",0,10000)
        planets = [star,planetA]
        self.system_simple.celestial_bodies = planets
        self.system_simple.update_initial_acceleration()
    def tearDown(self):
        pass
    def test_initial_accelerations(self):
        for planet in self.system.celestial_bodies:
            self.assertNotEqual(0.0,planet.acceleration[0])
            self.assertEqual(0.0,planet.acceleration[1],planet.name)
        for planet in self.system.celestial_bodies:
            self.assertNotEqual(0.0,planet.acceleration[0])
            if (planet.name!="Mars" and planet.name != "Probe"):
                self.assertEqual(0.0,planet.acceleration[1],planet.name)
    def test_potential_energy_simple(self):
        expected_value = -Planet.G
        self.assertEqual(expected_value,self.system_simple.getPotentialEnergy())
    def test_kinetic_energy_simple(self):
        expected_value = 1/2 * 1 * Planet.G
        self.assertEqual(expected_value,self.system_simple.getKineticenergy())
    def test_kinetic_energy(self):
        expected_value = 0
        for body in self.system.celestial_bodies:
            expected_value+= 1/2 *body.mass * np.linalg.norm(body.velocity)**2
        self.assertEqual(expected_value,self.system.getKineticenergy())
    def test_potential_energy(self):
        expected_value = 0
        for bodyA in self.system.celestial_bodies:
            for bodyB in self.system.celestial_bodies:
                if bodyA.name != bodyB.name:
                    expected_value += -Planet.G * bodyB.mass*0.5 *bodyA.mass/(np.linalg.norm(bodyB.position-bodyA.position))
        self.assertEqual(expected_value,self.system.getPotentialEnergy())
    def test_total_energy(self):
        potential = 0
        for bodyA in self.system.celestial_bodies:
            for bodyB in self.system.celestial_bodies:
                if bodyA.name != bodyB.name:
                    potential += -Planet.G * bodyB.mass*0.5 *bodyA.mass/(np.linalg.norm(bodyB.position-bodyA.position))
        kinetic_energy = 0
        for body in self.system.celestial_bodies:
            kinetic_energy+= 1/2 *body.mass * np.linalg.norm(body.velocity)**2
        self.assertEqual(potential+kinetic_energy,self.system.getEnergy())
    def test_distance_to_earth(self):
        expected_value = 6.371*10**6
        self.assertEqual(expected_value,self.system_probe.distanceToEarth())

        




