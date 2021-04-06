import sys
sys.path.append("./src")
import Main
from animate import animation
from SolarSystem import SolarSystem
from Options import Options
import unittest
import unittest.mock as mock
import matplotlib

class MainTest(unittest.TestCase):
    @mock.patch.object(matplotlib.pyplot,"show")
    def test_energy_graph_show(self,mock):
        Main.EnergyGraphComparisson(100)
        mock.assert_called_once()
    @mock.patch.object(matplotlib.pyplot,"plot")
    @mock.patch.object(SolarSystem,"update_beeman")
    @mock.patch.object(SolarSystem,"update_euler")
    def test_energy_graph_update(self,mock,mock2,mock3):
        Main.EnergyGraphComparisson(100)
        self.assertEqual(100,mock.call_count)
        self.assertEqual(100,mock2.call_count)
        mock3.assert_called_once()
    @mock.patch.object(SolarSystem,"update_beeman")
    def test_velocity_update(self,mock):
        Main.searchVelocityToMars(100,10)
        self.assertEqual(100*10,mock.call_count)
    @mock.patch.object(SolarSystem,"distanceToMars")
    def test_velocity_distance(self,mock):
        mock.return_value = 0
        Main.searchVelocityToMars(100,10)
        self.assertEqual(2*100*10+1,mock.call_count)
    @mock.patch.object(animation,"scatterplot")
    def test_main(self,mock):
        Main.main()
        mock.assert_called_once()


    
    
    