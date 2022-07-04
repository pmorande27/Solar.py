import unittest
import sys
import os
sys.path.append('./src')
from solar_system import SolarSystem
from options import Options
import numpy as np
import math
from celestial_bodies import CelestialBody
class TestSolarSystem(unittest.TestCase):
    def setUp(self):
        """Method that is executed begore each test and that loads all the systems used
        """
        self.system_probe = SolarSystem(3600,10000,Options.PROBE_RUN,"CelestialObjects3")
        self.system = SolarSystem(3600,10000,Options.NORMAL_RUN,"CelestialObjects3")
        self.system_simple = SolarSystem(3600,10000,Options.NORMAL_RUN,"CelestialObjects3")
        planetA = CelestialBody("B",1,1,1,"Planet",1,10000,"blue")
        star = CelestialBody("A",1,1,1,"Star",0,10000,"blue")
        planets = [star,planetA]
        self.system_simple.celestial_bodies = planets
        self.system_simple.update_initial_acceleration()
    def test_initial_accelerations(self):
        """Test used to check that the initial accelerations of the bodies of the systems are
        not zero.
        """
        for planet in self.system.celestial_bodies:
            self.assertNotEqual(0.0,planet.acceleration[0])
            self.assertEqual(0.0,planet.acceleration[1],planet.name)
        for planet in self.system.celestial_bodies:
            self.assertNotEqual(0.0,planet.acceleration[0])
            if (planet.name!="Mars" and planet.name != "Probe"):
                self.assertEqual(0.0,planet.acceleration[1],planet.name)
    def test_potential_energy_simple(self):
        """Test used to check that the value of the potential energy for a siple system is calculated
        correctly.
        """
        expected_value = -CelestialBody.G
        self.assertEqual(expected_value,self.system_simple.get_potential_energy())
    def test_kinetic_energy_simple(self):
        """Test used to check that the value of the kinetic energy for a siple system is calculated
        correctly.
        """
        expected_value = 1/2 * 1 * CelestialBody.G
        self.assertEqual(expected_value,self.system_simple.get_kinetic_energy())
    def test_kinetic_energy(self):
        """Test used to check that the value of the kinetic energy of a system is calculated
        correctly.
        """
        expected_value = 0
        for body in self.system.celestial_bodies:
            expected_value+= 1/2 *body.mass * np.linalg.norm(body.velocity)**2
        self.assertEqual(expected_value,self.system.get_kinetic_energy())
    def test_potential_energy(self):
        """Test used to check that the value of the potential energy of a system is calculated
        correctly.
        """
        expected_value = 0
        for bodyA in self.system.celestial_bodies:
            for bodyB in self.system.celestial_bodies:
                if bodyA.name != bodyB.name:
                    expected_value += -CelestialBody.G * bodyB.mass*0.5 *bodyA.mass/(np.linalg.norm(bodyB.position-bodyA.position))
        self.assertEqual(expected_value,self.system.get_potential_energy())
    def test_total_energy(self):
        """Test used to check that the value of the total energy of a system is calculated
        correctly.
        """
        potential = 0
        for bodyA in self.system.celestial_bodies:
            for bodyB in self.system.celestial_bodies:
                if bodyA.name != bodyB.name:
                    potential += -CelestialBody.G * bodyB.mass*0.5 *bodyA.mass/(np.linalg.norm(bodyB.position-bodyA.position))
        kinetic_energy = 0
        for body in self.system.celestial_bodies:
            kinetic_energy+= 1/2 *body.mass * np.linalg.norm(body.velocity)**2
        self.assertEqual(potential+kinetic_energy,self.system.get_energy())
    def test_distance_to_earth(self):
        """Test used to check that the initial distance between the probe and the Earth is correctly set
        """
        expected_value = 6.371*10**6
        self.assertEqual(expected_value,self.system_probe.distance_to_earth())
    def test_euler(self):
        """Test used to check that Euler's method works appropiatley.
        """
        planetA = CelestialBody("B",1,1,1,"Planet",1,10000,"blue")
        star = CelestialBody("A",1,1,1,"Star",0,10000,"blue")
        planetB = CelestialBody("B",1,2,1,"Planet",1,10000,"blue")
        planetB.position = np.array([-1.0,0.0])
        planetB.velocity = np.array([0.0,-planetA.velocity[1]])
        system = SolarSystem(3600,1000,Options.NORMAL_RUN,"CelestialObjects")
        system.celestial_bodies = [star,planetA,planetB]
        system.update_initial_acceleration()
        for i in range(100):
            system.update_euler()
        self.assertEqual(0.0,star.acceleration[0])
        self.assertEqual(0.0,star.acceleration[1])
    def test_beeman(self):
        """Test used to check that Beeman's method works appropiatley.
        """
        planetA = CelestialBody("B",1,1,1,"Planet",1,10000,"blue")
        star = CelestialBody("A",1,1,1,"Star",0,10000,"blue")
        planetB = CelestialBody("B",1,2,1,"Planet",1,10000,"blue")
        planetB.position = np.array([-1.0,0.0])
        planetB.velocity = np.array([0.0,-planetA.velocity[1]])
        system = SolarSystem(3600,1000,Options.NORMAL_RUN,"CelestialObjects")
        system.celestial_bodies = [star,planetA,planetB]
        system.update_initial_acceleration()
        for i in range(100):
            system.update_beeman()
        self.assertEqual(0.0,star.acceleration[0])
        self.assertEqual(0.0,star.acceleration[1])
    def test_timeStep(self):
        """Test used to check that the variable time step is implemented.
        """
        self.system_probe.update_beeman()
        self.assertEqual(self.system_probe.time_step,20)
        for i in range(1000):
            self.system_probe.update_beeman()
        self.assertEqual(self.system_probe.time_step,3600)
    def test_search(self):
        for body in self.system.celestial_bodies:
            self.assertEqual(self.system.search_body(body.name).name,body.name)
    def test_exception_search(self):
        with self.assertRaises(ValueError) as context:
            self.system.search_body("Probe")   
        self.assertTrue("The given name is not in the actual list of bodies" in str(context.exception))
    def test_variable_time_step(self):
        self.assertEqual(self.system_probe.time_step, 20)
        self.system_probe.initial = False
        self.system_probe.search_body("Probe").position = np.array([1000.0,0.0])
        self.system_probe.update_beeman()
        self.assertEqual(self.system_probe.time_step, 3600)





    
