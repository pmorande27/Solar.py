import unittest
import sys
import os
sys.path.append('../src')
from Planet import Planet
from Options import Options
import numpy as np
import math
class TestPlanets(unittest.TestCase):

    def setUp(self):
        self.planetA = Planet("A",1,1,1,"Planet",1,1)
        self.planetB = Planet("B",1,2,1,"Planet",1,1)
        self.planetC = Planet("B",1,3,1,"Planet",1,1)
        


    def tearDown(self):
        pass

    def test_velocities_initial(self):
        planets = [self.planetA,self.planetB,self.planetC]
        for i in range(len(planets)):
            velocity = [0,math.sqrt(Planet.G/(i+1))]
            self.assertEqual(velocity[0],planets[i].velocity[0])
            self.assertEqual(velocity[1],planets[i].velocity[1])
    def test_sign_start(self):
        planets = [self.planetA,self.planetB,self.planetC]
        for planet in planets:
            self.assertEqual(planet.get_y_sign(),1)
    def test_sign_on_change(self):
        self.planetA.position = np.array([0,-1])
        self.assertEqual(self.planetA.get_y_sign(),-1)
    def test_acceleration_initial(self):
        expected_value = np.array([0.0,0.0])
        planets = [self.planetA,self.planetB,self.planetC]
        for i in range(len(planets)):
            self.assertEqual(expected_value[0],planets[i].acceleration[0])
            self.assertEqual(expected_value[1],planets[i].acceleration[1])
            self.assertEqual(expected_value[0],planets[i].acceleration_prev[0])
            self.assertEqual(expected_value[1],planets[i].acceleration_prev[1])
    def test_acceleration_exception(self):
        planetD = Planet("D",1,1,1,"Planet",1,1)
        others = [planetD]
        with self.assertRaises(ValueError) as context:
             self.planetA.update_acceleration(others)   
        self.assertTrue('Division by Zero' in str(context.exception))
    def test_acceleration_update_identity(self):
        initial = np.copy(self.planetA.acceleration)
        others = [self.planetB,self.planetC]
        self.planetC.position = np.array([0,0])
        self.planetA.update_acceleration(others)
        self.assertEqual(initial[0],self.planetA.acceleration[0])
        self.assertEqual(initial[1],self.planetA.acceleration[1])
    def test_Euler_identity(self):
        self.planetA.velocity = np.array([0.0,0.0])
        initial_position = np.copy(self.planetA.position)
        self.planetA.update_position_euler(1)
        self.assertEqual(initial_position[0],self.planetA.position[0])
        self.assertEqual(initial_position[1],self.planetA.position[1])
    def test_Beeman_identity(self):
        self.planetA.velocity =np.array([0.0,0.0])
        initial_position = np.copy(self.planetA.position)
        self.planetA.update_position_beeman(1)
        self.assertEqual(initial_position[0],self.planetA.position[0])
        self.assertEqual(initial_position[1],self.planetA.position[1])
    


if __name__ == "__main__":
    unittest.main()