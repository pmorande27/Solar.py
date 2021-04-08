import unittest
import sys
import os
sys.path.append('./src')
from Planet import Planet
from options import Options
import numpy as np
import math
class TestPlanets(unittest.TestCase):
    """Test class that holds the tests for planets.py
    """

    def setUp(self):
        """Function that set ups the environment for the tests
        it will be called before each test and will create three planets
        used in them.
        """
        self.planetA = Planet("A",1,1,1,"Planet",1,1,"blue")
        self.planetB = Planet("B",1,2,1,"Planet",1,1,"blue")
        self.planetC = Planet("B",1,3,1,"Planet",1,1,"blue")

    def test_velocities_initial(self):
        """Test that cheks that the velcoicites of the planets
        at t = 0 are initialized correctly
        """
        planets = [self.planetA,self.planetB,self.planetC]
        for i in range(len(planets)):
            velocity = [0,math.sqrt(Planet.G/(i+1))]
            self.assertEqual(velocity[0],planets[i].velocity[0])
            self.assertEqual(velocity[1],planets[i].velocity[1])
    def test_sign_start(self):
        """Test that cheks that the y-position of the planets
        at t = 0 are initialized correctly
        """

        planets = [self.planetA,self.planetB,self.planetC]
        for planet in planets:
            self.assertEqual(planet.get_y_sign(),1)
    def test_sign_on_change(self):
        """Test to check if the y sign of the position of a planet can
        be retrieved correclty.
        """
        self.planetA.position = np.array([0,-1])
        self.assertEqual(self.planetA.get_y_sign(),-1)
    def test_acceleration_initial(self):
        """ Test that cheks that the velcoicites of the planets
        at t = 0 are initialized correctly. They should be zero as 
        it is the system class which updates this values on the constructor
        of that class.
        """
        expected_value = np.array([0.0,0.0])
        planets = [self.planetA,self.planetB,self.planetC]
        for i in range(len(planets)):
            self.assertEqual(expected_value[0],planets[i].acceleration[0])
            self.assertEqual(expected_value[1],planets[i].acceleration[1])
            self.assertEqual(expected_value[0],planets[i].acceleration_prev[0])
            self.assertEqual(expected_value[1],planets[i].acceleration_prev[1])
    def test_acceleration_exception(self):
        """Test used to check that an exception is raised if the position
        of two planets is the same.
        """
        planetD = Planet("D",1,1,1,"Planet",1,1,"blue")
        others = [planetD]
        with self.assertRaises(ValueError) as context:
             self.planetA.update_acceleration(others)   
        self.assertTrue('Division by Zero' in str(context.exception))
    def test_acceleration_update_identity(self):
        """Test used to check that updating the acceleration of a central body with two 
        oppisite bodies (same mass) in a line produces an acceleration of zero for the central body.
        """
        initial = np.copy(self.planetA.acceleration)
        others = [self.planetB,self.planetC]
        self.planetC.position = np.array([0,0])
        self.planetA.update_acceleration(others)
        self.assertEqual(initial[0],self.planetA.acceleration[0])
        self.assertEqual(initial[1],self.planetA.acceleration[1])
    def test_acceleration_update(self):
        """Test used to check that the acceleration of a planet is updated correctly.
        """
        others = [self.planetB,self.planetC]
        expected_value = [Planet.G+Planet.G/4,0.0]
        self.planetA.update_acceleration(others)
        self.assertEqual(expected_value[0],self.planetA.acceleration[0])
        self.assertEqual(expected_value[1],self.planetA.acceleration[1])
    def test_Euler_identity(self):
        """Test used to check that euler's algorithm with 0 initial velocity does not affect
        the position.
        """
        self.planetA.velocity = np.array([0.0,0.0])
        initial_position = np.copy(self.planetA.position)
        self.planetA.update_position_euler(1)
        self.assertEqual(initial_position[0],self.planetA.position[0])
        self.assertEqual(initial_position[1],self.planetA.position[1])
    def test_Beeman_identity(self):
        """Test used to check that Beemnas's algorithm with 0 initial velocity and accelerations
        does not affect
        the position.
        """
        self.planetA.velocity =np.array([0.0,0.0])
        initial_position = np.copy(self.planetA.position)
        self.planetA.update_position_beeman(1)
        self.assertEqual(initial_position[0],self.planetA.position[0])
        self.assertEqual(initial_position[1],self.planetA.position[1])
    
    def test_update_position_equivalence(self):
        """Test used to check that the two algorithms are equal if the accelerations are zero.
        """
        initial_position = np.copy(self.planetA.position)
        self.planetA.update_position_euler(1)
        position_euler =np.copy(self.planetA.position)
        self.planetA.position = np.copy(initial_position)
        self.planetA.update_position_beeman(1)
        position_beeman =np.copy(self.planetA.position)
        self.assertEqual(position_beeman[0],position_euler[0])
        self.assertEqual(position_beeman[1],position_euler[1])
    def test_update_velocity_euler(self):
        """Test used to check that the update in the velocity using Euler's algorithms
        is correct.
        """
        others = [self.planetC,self.planetB]
        self.planetA.update_acceleration(others)
        acceleratation = [Planet.G+Planet.G/4,0.0]
        self.planetA.update_velocity_euler(100)
        expected_value = np.array([0,math.sqrt(Planet.G/(1))]) + np.array([Planet.G+Planet.G/4,0.0])*100
        self.assertEqual(expected_value[0],self.planetA.velocity[0])
        self.assertEqual(expected_value[1],self.planetA.velocity[1])
    def test_update_velocity_beeman(self):
        """Test used to check that the update in the velocity using Euler's algorithms
        is correct.
        """
        others = [self.planetC,self.planetB]
        acceleratation = [Planet.G+Planet.G/4,0.0]
        self.planetA.update_velocity_beeman(100,others)
        expected_value = np.array([0,math.sqrt(Planet.G/(1))]) + np.array([Planet.G+Planet.G/4,0.0])*100*2/6
        self.assertEqual(expected_value[0],self.planetA.velocity[0])
        self.assertEqual(expected_value[1],self.planetA.velocity[1])
    def test_update_position_euler(self):
        """Test used to check that the update in the position using Euler's algorithms
        is correct.
        """
        initial_position = np.copy(self.planetA.position)
        expected_value = np.array([1.0,0.0]) + np.array([0,math.sqrt(Planet.G/(1))])*100
        self.planetA.update_position_euler(100)
        self.assertEqual(expected_value[0],self.planetA.position[0])
        self.assertEqual(expected_value[1],self.planetA.position[1])
    def test_update_position_beeman(self):
        """Test used to check that the update in the position using Beeman's algorithms
        is correct.
        """
        self.planetA.acceleration =np.array([-1.0,0.0])
        self.planetA.acceleration_prev = np.array([2.0,1.0])
        expected_value = np.array([1.0,0.0]) + np.array([0,math.sqrt(Planet.G/(1))])*100 + (
                    np.array([-1.0,0.0]) * 4 - np.array([2.0,1.0])) * 100 * 100 / 6
        self.planetA.update_position_beeman(100)
        self.assertEqual(expected_value[0],self.planetA.position[0])
        self.assertEqual(expected_value[1],self.planetA.position[1])


if __name__ == "__main__":
    unittest.main()
