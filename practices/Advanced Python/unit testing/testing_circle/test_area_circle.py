from area_circle import area
from math import pi
import unittest

class TestCircle(unittest.TestCase):
	def test_area_circle(self):
		self.assertAlmostEqual(area(1),pi*1**2)
		self.assertAlmostEqual(area(0),0)
		self.assertAlmostEqual(area(2.8),pi*2.8**2)

	def test_values(self):
		self.assertRaises(ValueError,area, -2)

	def test_types(self):
		self.assertRaises(TypeError, area, False)
		self.assertRaises(TypeError, area, "Ramesh")
		self.assertRaises(TypeError, area, 4+5j)