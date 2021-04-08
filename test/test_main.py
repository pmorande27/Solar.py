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
    @mock.patch.object(SolarSystem,"update_beeman")
    def test_velocity_update(self,mock):
        main.searchVelocityToMars(100,10,10)
        self.assertEqual(100*10,mock.call_count)
    @mock.patch.object(SolarSystem,"distance_to_mars")
    def test_velocity_distance(self,mock):
        mock.return_value = 0
        main.searchVelocityToMars(100,10,10)
        self.assertEqual(2.5*100*10+1,mock.call_count)

    @mock.patch.object(Animation,"scatter_plot")
    def test_main(self,mock):
        main.main()
        mock.assert_called_once()


    
    
    
