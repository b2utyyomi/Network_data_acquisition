class Product:
	def __init__(self, description, price, quantity):
		self.__description = description
		self.__price = price
		self.__inventory = quantity
	def set_description(self, description):
		self.__description = description
	def get_description(self):
		return self.__description
	description = property(get_description, set_description)
	def set_price(self, price):
		self.__price = price
	def get_price(self):
		return self.__price
	#price = property(get_price, set_price)
	def set_inventory(self, inventory):
		self.__inventory = inventory
	def get_inventory(self):
		return self.__inventory
	inventory = property(get_inventory, set_inventory)
	
	def buy_Product(self, amount):
		self.__inventory = self.__inventory - amount
	
	def __str__(self):
		return '{0} - price: ${1:.2f}, inventory:{2:d}'.format(self.__description, self.__price, self.__inventory)
	
	
