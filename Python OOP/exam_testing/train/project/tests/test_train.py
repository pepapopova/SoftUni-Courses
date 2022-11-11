from unittest import TestCase

from project.train.train import Train


class TestTrain(TestCase):
    NAME = 'Express'
    CAPACITY = 3

    def setUp(self) -> None:
        self.train = Train(self.NAME, self.CAPACITY)

    def test_innit_works_properly(self):
        self.assertEqual(self.NAME, self.train.name)
        self.assertEqual(self.CAPACITY, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_add_if_capacity_is_full(self):
        self.train.passengers = ['pesho', 'gosho', 'galya']
        with self.assertRaises(ValueError) as error:
            self.train.add('Tancheto')
        self.assertEqual("Train is full", str(error.exception))
        self.assertFalse('Tancheto' in self.train.passengers
                         )
    def test_add_if_name_already_a_passenger(self):
        self.train.passengers = ['pesho', 'gosho']
        passenger = 'gosho'
        with self.assertRaises(ValueError) as error:
            self.train.add(passenger)
        self.assertEqual(f"Passenger {passenger} Exists", str(error.exception))

    def test_add_passenger(self):
        passenger = 'Pepa'
        result = self.train.add(passenger)
        self.assertEqual(f"Added passenger {passenger}", result)
        self.assertTrue(passenger in self.train.passengers)

    def test_remove_raises_error_when_passenger_not_in_train(self):
        with self.assertRaises(ValueError) as error:
            self.train.remove('Pepa')
        self.assertEqual("Passenger Not Found", str(error.exception))
        self.assertEqual([], self.train.passengers)

    def test_removes_passenger_when_in_train(self):
        passenger = 'nona'
        self.train.add(passenger)
        result = self.train.remove(passenger)
        self.assertEqual(f"Removed {passenger}", result)
        self.assertEqual([], self.train.passengers)