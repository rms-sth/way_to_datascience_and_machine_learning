
class Parrot:
	species = "bird"

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def sing(self, song):
		return "{} sings {}".format(self.name, song)

	def dance(self):
		return "{} is now dancing".format(self.name)



p1 = Parrot("Bijesh", 23)
p2 = Parrot("Bhuwan", 24)

print("{} and {} are both {}s".format(p1.name, p2.name, p1.__class__.species))
print("{} is {} years old". format(p1.name, p1.age))
print("{} is {} years old". format(p2.name, p2.age))

print("{}".format(p1.sing("Twinkle Twinkle")))
print("{}".format(p2.sing("Baby ko base pasand hein")))
print(p1.dance())
print(p2.dance())