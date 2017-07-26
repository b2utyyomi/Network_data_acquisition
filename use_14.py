from product import Product

prod1 = Product('carrot', 1.25, 10)
print(prod1)
print('Buying 4 carrots...')
prod1.buy_Product(4)
print(prod1)
print('Changing the price to $1.50...')
#prod1.price = 1.50
prod1.set_price(1.50)
print(prod1)
