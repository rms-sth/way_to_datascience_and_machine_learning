class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age



class Student(Person):
	def __init__(self, college, level):
		# super().__init__()
		self.college = college
		self.level = level

	def getStudentInfo(self):
		print("\nName:{}\nAge:{}\nCollege:{}\nLevel:{}".format(self.name,self.age,self.college,self.level))



class Employee(Person):
	def __init__(self, salary, company_name):
		super().__init__()
		self.salary = salary
		self.company_name = company_name

	
p1 = Person("Ramesh Pradhna", 23)
s1 = Student("Nagarjuna College of IT", "Bachelor")
print(s1.getStudentInfo())

# print("{} and {} are both {}s".format(p1.name, p2.name, p1.__class__.species))
# print("{} is {} years old". format(p1.name, p1.age))
# print("{} is {} years old". format(p2.name, p2.age))

# print("{}".format(p1.sing("Twinkle Twinkle")))
# print("{}".format(p2.sing("Baby ko base pasand hein")))
# print(p1.dance())
# print(p2.dance())