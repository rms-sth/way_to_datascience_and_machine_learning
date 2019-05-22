class Computer:
	def __init__(self):
		self.__maxprice = 900

	def sell(self):
		print("Selling price: {}".format(self.__maxprice))

	def setMaxPrice(self, price):
		self.__maxprice = price


c = Computer()
c.sell()

#changing the price directly
c.__maxprice = 1100
c.sell()

#changing through method
c.setMaxPrice(1100)
c.sell()