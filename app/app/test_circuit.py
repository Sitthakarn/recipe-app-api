from django.test import TestCase
from math import pi
from app.area import circle_area

class AreaTest(TestCase):
    
    def test_circle_area(self):
        """Test that the positive reduis"""
        self.assertAlmostEqual(circle_area(1), pi)


