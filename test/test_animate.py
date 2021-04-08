import sys
sys.path.append("./src")
from solar_system import SolarSystem
from animate import Animation
from solar_system import SolarSystem
from options import Options
import matplotlib
import unittest
import unittest.mock as mock



class AnimateTest(unittest.TestCase):

    @mock.patch.object(matplotlib.pyplot,"show")
    def test_scatterplot_show(self,mock):
        self.system_probe = SolarSystem(3600,10000,Options.PROBE_RUN,"CelestialObjects")
        animate = Animation(self.system_probe)
        animate.scatter_plot(100)
        mock.assert_called_once()
    @mock.patch.object(matplotlib.pyplot,"show")
    @mock.patch.object(SolarSystem,"update_beeman")
    def test_scatterplot_update(self,mock,mock2):
        self.system_probe = SolarSystem(3600,10000,Options.PROBE_RUN,"CelestialObjects")
        animate = Animation(self.system_probe)
        animate.scatter_plot(100)
        mock.assert_called()
        self.assertEqual(mock.call_count,100)
    @mock.patch.object(matplotlib.pyplot,"show")
    def test_plot_show(self,mock):
        self.system_probe = SolarSystem(3600,10000,Options.PROBE_RUN,"CelestialObjects")
        animate = Animation(self.system_probe)
        animate.plot()
        mock.assert_called()
    @mock.patch.object(matplotlib.pyplot,"show")
    @mock.patch.object(SolarSystem,"update_beeman")
    def test_animate_update(self,mock,mock2):
        self.system_probe = SolarSystem(3600,10000,Options.PROBE_RUN,"CelestialObjects")
        animate = Animation(self.system_probe)
        animate.plot()
        animate.init()
        animate.animate(0)
        mock.assert_called()
    @mock.patch.object(matplotlib.pyplot,"show")
    @mock.patch.object(matplotlib.animation.FuncAnimation,"__init__")
    def test_plot_animate(self,mock,mock2):
        mock.return_value = None 
        self.system_probe = SolarSystem(3600,10000,Options.PROBE_RUN,"CelestialObjects")
        animate = Animation(self.system_probe)
        animate.plot()
        mock.assert_called()
    @mock.patch.object(matplotlib.pyplot,"show")
    def test_energy_graph_show(self,mock):
        Animation.EnergyGraphComparisson(100)
        mock.assert_called_once()
    @mock.patch.object(matplotlib.pyplot,"show")
    @mock.patch.object(matplotlib.pyplot,"plot")
    @mock.patch.object(SolarSystem,"update_beeman")
    @mock.patch.object(SolarSystem,"update_euler")
    def test_energy_graph_update(self,mock,mock2,mock3,mock4):
        Animation.EnergyGraphComparisson(100)
        self.assertEqual(100,mock.call_count)
        self.assertEqual(100,mock2.call_count)
        mock3.assert_called_once()
    

    

    
    

