from django.test import TestCase
from app.calc import add, substact, multiply, devide

class calcTests(TestCase):

    def test_add_number(self):
        """Test to add two numbers together"""
        self.assertEqual(add(3, 5,), 8)
    
    def test_substact_number(self):
        """Test that substact 2 numbers and return the result"""
        self.assertEqual(substact(5,11), 6)

    def test_multiply_number(self):
        """Test that multiply 2 numbers and return the result"""
        self.assertEqual(multiply(3, 4), 12)

    def test_devide_number(self):
        """Test that devide the numbers"""
        self.assertEqual(devide(6,2), 3)
    
    def test_devide_number_by_zero(self):
        """Test that devide the number by zero"""
        self.assertEqual(devide(6,0), "division by zero")