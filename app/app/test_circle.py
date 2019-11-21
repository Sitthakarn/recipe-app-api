from django.test import TestCase
from math import pi
from app.area import circle_area

class AreaTest(TestCase):
    
    def test_circle_area(self):
        """Test that the reduis>=0"""
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), pi*2.1**2)

    def test_values(self):
        # Make sure value errors are raised when necessary
        self.assertRaises(ValueError, circle_area, -2)

    def test_types(self):
        # Test the errors are raised if not number
        self.assertRaises(TypeError, circle_area, 3+5j)
        self.assertRaises(TypeError, circle_area, "radius")
        self.assertRaises(TypeError, circle_area, True)