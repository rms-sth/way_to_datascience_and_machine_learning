import unittest
from area_circle import area_circle
from math import pi

class TestCircleArea(unittest.TestCase):
	def test_area_circle(self):
		#Test the area when radius>=0
		self.assertAlmostEqual(area_circle(1),pi*1**2)
		self.assertAlmostEqual(area_circle(0),0)
		self.assertAlmostEqual(area_circle(3.1), pi*3.1**2)

	def test_values(self):
		#Make sure value errors are raised when necesssary
		self.assertRaises(ValueError, area_circle, -2)


	def test_types(self):
		#Make sure type errors are raised when necessary
		self.assertRaises(TypeError, area_circle, 5+7j)
		self.assertRaises(TypeError, area_circle, True)
		self.assertRaises(TypeError, area_circle, "Ramesh")

