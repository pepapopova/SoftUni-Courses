from unittest import TestCase

from project.factory.paint_factory import PaintFactory


class TestPaintFactory(TestCase):

    NAME = 'Color factory'
    CAPACITY = 10
    VALID_INGREDIENTS = ["white", "yellow", "blue", "green", "red"]

    def setUp(self) -> None:
        self.factory = PaintFactory(self.NAME, self.CAPACITY)

    def test_if_innit_works_properly(self):
        self.assertEqual(self.NAME, self.factory.name)
        self.assertEqual(self.CAPACITY, self.factory.capacity)
        self.assertEqual({}, self.factory.ingredients)
        self.assertEqual(self.VALID_INGREDIENTS, self.factory.valid_ingredients)
        self.assertEqual({}, self.factory.products)

    def test_add_ingredient_raises_error_when_ingredient_not_in_valid_ingredients(self):
        self.factory.valid_ingredients = self.VALID_INGREDIENTS
        with self.assertRaises(TypeError) as error:
            self.factory.add_ingredient('pink', 10)
        self.assertEqual(f"Ingredient of type pink not allowed in PaintFactory", str(error.exception))
        self.assertTrue('pink' not in self.factory.ingredients)

    def test_add_ingredient_when_capacity_is_reached(self):
        self.factory.ingredients = {'white': 2, 'blue': 3}
        with self.assertRaises(ValueError) as error:
            self.factory.add_ingredient('white', 6)
        self.assertEqual("Not enough space in factory", str(error.exception))

    def test_add_ingredient_when_capacity_is_just_enough(self):
        self.factory.ingredients = {'white': 2, 'blue': 3}
        self.factory.add_ingredient('white', 5)
        self.assertEqual({'white': 7, 'blue': 3}, self.factory.ingredients)
        self.assertEqual(7, self.factory.ingredients['white'])

    def test_removes_ingredient_raises_error_when_no_such_ingredient_is_present(self):
        with self.assertRaises(KeyError) as error:
            self.factory.remove_ingredient('pink', 2)
        self.assertEqual("No such ingredient in the factory", str(error.exception))

    def test_removes_raises_error_when_quantity_is_less_than_0(self):
        self.factory.ingredients = {'white': 2, 'blue': 3}
        with self.assertRaises(ValueError) as error:
            self.factory.remove_ingredient('blue', 4)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(error.exception))

    def test_removes_when_we_have_the_needed_quantity(self):
        self.factory.ingredients = {'white': 2, 'blue': 3}
        self.factory.remove_ingredient('blue', 3)
        self.assertEqual(0, self.factory.ingredients['blue'])
        self.assertEqual({'white': 2, 'blue': 0}, self.factory.ingredients)

    def test_property_products(self):
        self.factory.ingredients = {'white': 2, 'blue': 3}
        self.assertEqual({'white': 2, 'blue': 3}, self.factory.products)
        self.assertEqual(self.factory.ingredients, self.factory.products)

    def test_repr_works_properly(self):
        self.factory.ingredients = {'white': 2, 'blue': 3}
        expected_result = f"Factory name: {self.NAME} with capacity {self.CAPACITY}.\n" \
                          f"white: 2\n" \
                          f"blue: 3\n"
        self.assertEqual(expected_result, str(self.factory))