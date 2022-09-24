
# unit tests
import unittest
import classes

class TestStringMethods(unittest.TestCase):
    # test function to test equality of two value
    def test_negative(self):
        firstValue = "geeks"
        secondValue = "gfg"
        # error message in case if test case got failed
        message = "First value and second value are not equal !"
        # assertEqual() to check equality of first & second value
        self.assertEqual(firstValue, secondValue, message)


assert_equals(calculate_damage("fire", "water", 100, 100), 25)

if __name__ == '__main__':
    unittest.main()