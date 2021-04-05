import unittest
import sys
import os
sys.path.append('../src/utils')
import helperfunctions
sys.path.append('../src')
from SolarSystem import SolarSystem
from Options import Options


class TestReader(unittest.TestCase):
    
    def test_WrittingFile(self):
        helperfunctions.writeFile("test")
        system = SolarSystem(1,1,Options.PROBE_RUN,"test")
        self.assertEqual(len(system.celestial_bodies),6)
        os.remove("../data/test")
    
    def test_Adding_Planet(self):
        helperfunctions.writeFile("test")
        helperfunctions.add_planet("test",1,1,1,"test")
        system = SolarSystem(1,1,Options.PROBE_RUN,"test")
        self.assertEqual(len(system.celestial_bodies),7)
        self.assertEqual(system.celestial_bodies[len(system.celestial_bodies)-1].name,"test")
        self.assertEqual(system.celestial_bodies[len(system.celestial_bodies)-1].mass,1)
        helperfunctions.writeFile("test")
        os.remove("../data/test")

if __name__ == "__main__":
    unittest.main()