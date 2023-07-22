import unittest

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

class MathOp(unittest.TestCase):
    def test_add(self):
        result = add(3, 4)
        self.assertEqual(result, 7)

    def test_subtract(self):
        result = subtract(10, 4)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()
