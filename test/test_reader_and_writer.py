import unittest
import sys
import os
sys.path.append('./src/utils')
import helperfunctions
sys.path.append('./src')
from SolarSystem import SolarSystem
from options import Options


class TestReader(unittest.TestCase):

    def setUp(self):
        helperfunctions.writeFile("test")


    def tearDown(self):
        os.remove("./data/test")

    
    def test_WrittingFile(self):
        system = SolarSystem(1,1,Options.PROBE_RUN,"test")
        self.assertEqual(len(system.celestial_bodies),6)
    
    def test_Adding_Planet(self):
        helperfunctions.add_planet("test",1,1,1,"test")
        system = SolarSystem(1,1,Options.PROBE_RUN,"test")
        self.assertEqual(len(system.celestial_bodies),7)
        self.assertEqual(system.celestial_bodies[len(system.celestial_bodies)-1].name,"test")
        self.assertEqual(system.celestial_bodies[len(system.celestial_bodies)-1].mass,1)
        self.assertEqual(system.celestial_bodies[len(system.celestial_bodies)-1].orbital_radius,1)
        self.assertEqual(system.celestial_bodies[len(system.celestial_bodies)-1].type_of_object,"Planet")
    


if __name__ == "__main__":
    unittest.main()
