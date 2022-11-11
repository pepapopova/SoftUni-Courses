from project.pet_shop import PetShop

from unittest import TestCase


class PetShopTest(TestCase):
    NAME = 'Pet Shop'

    def setUp(self) -> None:
        self.pet_shop = PetShop(self.NAME)

    def test_if_innit_works_properly(self):
        self.assertEqual(self.NAME, self.pet_shop.name)
        self.assertEqual({}, self.pet_shop.food)
        self.assertEqual([], self.pet_shop.pets)

    def test_add_food_raises_error_when_food_is_equal_or_lt_zero(self):
        with self.assertRaises(ValueError) as error:
            self.pet_shop.add_food('can', 0)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(error.exception))

    def test_add_food_works_properly(self):
        result = self.pet_shop.add_food('canned food', 100)
        self.assertEqual(f"Successfully added 100.00 grams of canned food.", result)
        self.assertEqual({'canned food': 100}, self.pet_shop.food)

    def test_add_pet_properly(self):
        pet = 'cat'
        result = self.pet_shop.add_pet(pet)
        self.assertEqual(f"Successfully added {pet}.", result)
        self.assertTrue(pet in self.pet_shop.pets)
        self.assertEqual([pet], self.pet_shop.pets)

    def test_add_pet_raises_exception_when_pet_is_already_added(self):
        pet = 'cat'
        self.pet_shop.add_pet(pet)
        with self.assertRaises(Exception) as error:
            self.pet_shop.add_pet(pet)
        self.assertEqual("Cannot add a pet with the same name", str(error.exception))
        self.assertEqual([pet], self.pet_shop.pets)

    def test_feed_pet_raises_exception_when_pet_is_not_in_pets_list(self):
        with self.assertRaises(Exception) as error:
            self.pet_shop.feed_pet('canned food', 'cat')
        self.assertEqual("Please insert a valid pet name", str(error.exception))

    def test_feed_pet_when_food_is_not_present(self):
        self.pet_shop.add_pet('cat')
        result = self.pet_shop.feed_pet('canned food', 'cat')
        self.assertEqual('You do not have canned food', result)

    def test_feed_pet_when_food_is_below_100(self):
        self.pet_shop.add_pet('cat')
        self.pet_shop.food['canned food'] = 99
        result = self.pet_shop.feed_pet('canned food', 'cat')
        self.assertEqual("Adding food...", result)
        self.assertEqual(1099, self.pet_shop.food['canned food'])

    def test_feed_pet_properly(self):
        self.pet_shop.add_pet('cat')
        self.pet_shop.food['canned food'] = 100
        result = self.pet_shop.feed_pet('canned food', 'cat')
        self.assertEqual("cat was successfully fed", result)
        self.assertEqual(0, self.pet_shop.food['canned food'])

    def test_repr_gives_proper_result(self):
        self.pet_shop.add_pet('cat')
        self.pet_shop.add_pet('dog')
        expected_result = f'Shop {self.NAME}:\n' \
                          f'Pets: cat, dog'
        self.assertEqual(expected_result, repr(self.pet_shop))
