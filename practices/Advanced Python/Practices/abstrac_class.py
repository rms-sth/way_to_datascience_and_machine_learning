from abc import ABC, abstractmethod

class MyAbstractMethod(ABC):

	def __init__(self, first_no, second_no):
		self.first_no = first_no
		self.second_no = second_no

	@abstractmethod
	def do_something(self):
		pass


class AddNumber(MyAbstractMethod):

	def do_something(self):
		return self.first_no + self.second_no


class MultiplyNumber(MyAbstractMethod):

	def do_something(self):
		return self.first_no * self.second_no


a = AddNumber(3,5)
print(a.do_something())

b = MultiplyNumber(4,6)
print(b.do_something())