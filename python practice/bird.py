class Bird:
	def __init__(self):
		print("Bird is ready")

	def whoIsThis(self):
		print("I am Bird")

	def swim(self):
		print("Swim Faster")


class Penguin(Bird):
	def __init__(self):
		super().__init__()
		print("Penguin is ready")

	def whoIsThis(self):
		print("I am Penguin")

	def run(self):
		print("Run faster")

p1 = Penguin()
p1.whoIsThis()
p1.run()
p1.swim()