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
    """Test class used to contain the tests for animate.py and Animation class.
    """

    @mock.patch.object(matplotlib.pyplot,"show")
    def test_scatterplot_show(self,mock):
        """Test used to prove that plt.show() is called once in scatter_plot method
        uses mocking
        """
        self.system_probe = SolarSystem(3600,10000,Options.PROBE_RUN,"CelestialObjects")
        animate = Animation(self.system_probe)
        animate.scatter_plot(100)
        mock.assert_called_once()
    @mock.patch.object(matplotlib.pyplot,"show")
    @mock.patch.object(SolarSystem,"update_beeman")
    def test_scatterplot_update(self,mock,mock2):
        """Test used to prove that update_beeman() is called 100 times in scatter_plot method
        if the parameter passed to scatter_plot is 100.
        uses mocking
        """
        self.system_probe = SolarSystem(3600,10000,Options.PROBE_RUN,"CelestialObjects")
        animate = Animation(self.system_probe)
        animate.scatter_plot(100)
        mock.assert_called()
        self.assertEqual(mock.call_count,100)
    @mock.patch.object(matplotlib.pyplot,"show")
    def test_plot_show(self,mock):
        """Test to prove that plt.show is called in plot() method.
        Uses mocking
        """
        self.system_probe = SolarSystem(3600,10000,Options.PROBE_RUN,"CelestialObjects")
        animate = Animation(self.system_probe)
        animate.plot()
        mock.assert_called()
    @mock.patch.object(matplotlib.pyplot,"show")
    @mock.patch.object(SolarSystem,"update_beeman")
    def test_animate_update(self,mock,mock2):
        """Test used to prove that update beeman is calld in the animate method
        Uses mocking.
        """
        self.system_probe = SolarSystem(3600,10000,Options.PROBE_RUN,"CelestialObjects")
        animate = Animation(self.system_probe)
        animate.plot()
        animate.init()
        animate.animate(0)
        mock.assert_called()
    @mock.patch.object(matplotlib.pyplot,"show")
    @mock.patch.object(matplotlib.animation.FuncAnimation,"__init__")
    def test_plot_animate(self,mock,mock2):
        """Test used to check that a FunCAnimator is used in plot()
        Uses mocking

        """
        mock.return_value = None 
        self.system_probe = SolarSystem(3600,10000,Options.PROBE_RUN,"CelestialObjects")
        animate = Animation(self.system_probe)
        animate.plot()
        mock.assert_called()
    @mock.patch.object(matplotlib.pyplot,"show")
    def test_energy_graph_show(self,mock):
        """Test used to check that plt.show is called within the energy_graph method
        Uses mocking

        """
        Animation.energy_graph_comparisson(100)
        mock.assert_called_once()
    @mock.patch.object(matplotlib.pyplot,"show")
    @mock.patch.object(matplotlib.pyplot,"plot")
    @mock.patch.object(SolarSystem,"update_beeman")
    @mock.patch.object(SolarSystem,"update_euler")
    def test_energy_graph_update(self,mock,mock2,mock3,mock4):
        """Test used to verify thst the methods update_beeman and
        update euler are called the right number of times in the energy_graph
        method.
        Uses mocking
        """
        Animation.energy_graph_comparisson(100)
        self.assertEqual(100,mock.call_count)
        self.assertEqual(100,mock2.call_count)
        mock3.assert_called_once()
    

    

    
    

