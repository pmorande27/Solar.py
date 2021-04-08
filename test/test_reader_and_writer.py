import unittest
import sys
import os
sys.path.append('./src/utils')
from writer import Writer
sys.path.append('./src')
from solar_system import SolarSystem
from options import Options


class TestReader(unittest.TestCase):
    """Testing class that contians the tests for the file helperfunctions.py in 
    ./utils
    """

    def setUp(self):
        self.write = Writer()
        """Initializes before each test the file "test.txt"
        """
        self.write.write_file("test")


    def tearDown(self):
        """After each test removes the file
        """
        os.remove("./data/test")

    
    def test_WrittingFile(self):
        """Test used to check that the method write_file works correctly.
        """
        system = SolarSystem(1,1,Options.PROBE_RUN,"test")
        self.assertEqual(len(system.celestial_bodies),6)
    
    def test_Adding_Planet(self):
        """Test used to check that the method add_planet can add a planet correctly into a system.
        """
        self.write.add_planet("test",1,1,1,"blue","test")
        system = SolarSystem(1,1,Options.PROBE_RUN,"test")
        self.assertEqual(len(system.celestial_bodies),7)
        self.assertEqual(system.celestial_bodies[len(system.celestial_bodies)-1].name,"test")
        self.assertEqual(system.celestial_bodies[len(system.celestial_bodies)-1].mass,1)
        self.assertEqual(system.celestial_bodies[len(system.celestial_bodies)-1].orbital_radius,1)
        self.assertEqual(system.celestial_bodies[len(system.celestial_bodies)-1].type_of_object,"Planet")
    


if __name__ == "__main__":
    unittest.main()
