# test_mymodule.py

import unittest
import mymodule

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        result = mymodule.add(3, 5)
        self.assertEqual(result, 8)


    def test_subtract(self):
        result = mymodule.subtract(10, 4)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()
