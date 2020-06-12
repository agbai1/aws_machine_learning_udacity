from shirt_class import Shirt

shirt_one = Shirt('red', 'S', 'long-sleeve', 45)
shirt_two = Shirt('orange', 'L', 'short-sleeve', 30)

print(shirt_one.get_price())
print(shirt_one.get_color())

shirt_two.set_price(45)
print(shirt_two.get_price())


total = shirt_one.get_price() + shirt_two.get_price()

total_discount = shirt_one.discount(.14) + shirt_two.discount(.06)
