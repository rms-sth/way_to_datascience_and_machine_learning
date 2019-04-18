# Every class in Python is derived from the class object. It is the most base type in Python.
# So technically, all other class, either built-in or user-defines, are derived classes 
# and all objects are instances of object class.

# In the multiple inheritance scenario, any specified attribute 
# is searched first in the current class. 
# If not found, the search continues into parent classes 
# in depth-first, left-right fashion without searching same class twice.

class Polygon:
	def __init__(self, no_of_sides):
		self.n = no_of_sides
		self.side_value = [0 for i in range(no_of_sides)]

	def putSideInfo(self):
		self.side_value = [float(input("Enter the {} : ".format(i+1))) for i in range(self.n)]

	def getSideInfo(self):
		for i in range(self.n):
			print("The value of side {} is : {}".format(i+1, self.side_value[i]))


class Triangle(Polygon):
	def __init__(self):
		super().__init__(3)


	def findArea(self):
		a,b,c = self.side_value
		s = (a+b+c)/2
		area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
		print("The area of Triange is : {}".format(area))

	def findPerimeter(self):
		a,b,c = self.side_value
		perimeter = a+b+c
		print("The perimeter of Triange is {}".format(perimeter))


class Rectangle(Polygon):
	def __init__(self):
		Polygon.__init__(self,2)

	def findArea(self):
		l,b = self.side_value
		area = l*b
		print("Area of Rectangle is : {} ".format(area))

	def findPerimeter(self):
		l,b = self.side_value
		perimeter = 2*(l+b)
		print("The perimeter of Rectangle is {}".format(perimeter))


def do_all(obj):
	obj.putSideInfo()
	obj.getSideInfo()
	obj.findArea()
	obj.findPerimeter()



t = Triangle()
do_all(t)
# t.putSideInfo()
# t.getSideInfo()
# t.findArea()

r = Rectangle()
do_all(r)
# r.putSideInfo()
# r.getSideInfo()
# r.findArea()
print("Is t is instance of Triangle?: Ans =>", isinstance(t,Triangle))
print("Is t is instance of Polygon?: Ans =>", isinstance(t,Polygon))
print("Is t is instance of Rectangle?: Ans =>", isinstance(t,Rectangle))
print("Is Polygon is subclass of Triangle?: Ans =>", issubclass(Polygon,Triangle))
print("Is Triangle is subclass of Polygon?: Ans =>", issubclass(Triangle,Polygon))


