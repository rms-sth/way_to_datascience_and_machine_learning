from math import pi
def area(r):
	if type(r) not in [int, float]:
		raise TypeError("Not valid type")
	if r<0:
		raise ValueError("Negative Number encountered")
	return pi*r**2

#Testing function
# radii = [1, 0, -2, 3+6j, True, "Ramesh"]
# message = "The area of circle with r = {radius} is : {area}"
# for r in radii:
# 	print(message.format(radius=r, area = area(r)))