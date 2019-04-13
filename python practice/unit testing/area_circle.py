from math import pi
def area_circle(r):
	if type(r) not in [int, float]:
		raise TypeError("Radius must be non-negative real number")
	if r < 0:
		raise ValueError("The value cannot be negative")
	return pi * (r**2)

#Test function
# radii = [1, 0, -2, 5+6j, True, "ramesh"]
# message = "The area of circle with r = {radius} is {area}."
# for r in radii:
# 	a = area_circle(r)
# 	print(message.format(radius=r, area=a))
