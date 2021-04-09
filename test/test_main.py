import sys
sys.path.append("./src")
import main
from animate import Animation
from solar_system import SolarSystem
from options import Options
import unittest
import unittest.mock as mock
import matplotlib

class MainTest(unittest.TestCase):
    """Test class which contains the tests for main.py
    """
    @mock.patch.object(SolarSystem,"update_beeman")
    def test_velocity_update(self,mock):
        """Test used to check that the method update_beeman
        is called the right amount of times within the method
        search_velocities_to_mars.
        """
        main.search_velocity_to_mars(100,10,10)
        self.assertEqual(100*10,mock.call_count)
    @mock.patch.object(SolarSystem,"distance_to_mars")
    def test_velocity_distance(self,mock):
        """Test used to check that the method distance_to_mars
        is called the right amount of times within the method
        search_velocities_to_mars.
        """
        mock.return_value = 0
        main.search_velocity_to_mars(100,10,10)
        self.assertEqual(2.5*100*10+1,mock.call_count)



    
    
    
