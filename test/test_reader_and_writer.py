import unittest
import sys
sys.path.append('../src/utils')
import helperfunctions

class TestReader(unittest.TestCase):

    def test_add(self):
        self.assertEqual(1,1)

if __name__ == "__main__":
    unittest.main()