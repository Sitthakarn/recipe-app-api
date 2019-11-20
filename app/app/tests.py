from django.test import TestCase
from app.calc import add, substact, devide

class CalcTest(TestCase):

    def test_add_number(self):
        """Test that add 2 numbers"""
        self.assertEqual(add(3,8), 11)

    def test_substact_number(self):
        """Test that substact 2 numbers and return the result"""
        self.assertEqual(substact(5,11), 6)
        
    def test_divide_number(self):
        """Test devide the numbers"""
        self.assertEqual(devide(8, 2), 4)
        self.assertEqual(devide(8, 0), "division by zero")

