from project.animals.mammals import Tiger, Cat
from project.food import Vegetable, Fruit, Meat

cat = Cat("Johny", 10, 'dessert')
veg = Vegetable(3)
fruit = Fruit(5)
meat = Meat(1)
print(cat)
print(cat.make_sound())
print(cat.feed(veg))
print(cat.feed(fruit))
print(cat.feed(meat))
print(cat)