class Parrot:
	'''Parrot Class for checking polymorphism'''
	def fly(self):
		print("Parrot can fly")

	def swim(self):
		print("Parrot cannot swim")

class Penguin:
	'''Penguin class for checking polymorphism'''
	def fly(self):
		print("Penguin cannot fly")

	def swim(self):
		print("Penguim can swim")



def flyingTest(bird):
	print(bird.__doc__)
	bird.fly()


def swimingTest(bird):
	bird.swim()



pa1 = Parrot()
pe1 = Penguin()

flyingTest(pa1)
flyingTest(pe1)

swimingTest(pa1)
swimingTest(pe1)

