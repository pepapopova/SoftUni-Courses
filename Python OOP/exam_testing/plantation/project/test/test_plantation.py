from unittest import TestCase

from project.plantation import Plantation


class PlantationTest(TestCase):
    SIZE = 100

    def setUp(self) -> None:
        self.plantation = Plantation(self.SIZE)

    def test_innit(self):
        self.assertEqual(self.SIZE, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_raises_error_when_size_is_below_zero(self):
        with self.assertRaises(ValueError) as error:
            Plantation(-2)
        self.assertEqual("Size must be positive number!", str(error.exception))

    def test_hire_worker_when_worker_is_already_hired(self):
        self.plantation.workers = ['Ivan']
        with self.assertRaises(ValueError) as error:
            self.plantation.hire_worker('Ivan')
        self.assertEqual("Worker already hired!", str(error.exception))
        self.assertEqual(['Ivan'], self.plantation.workers)

    def test_hire_worker_when_worker_is_not_hired(self):
        worker = 'Pena'
        result = self.plantation.hire_worker(worker)
        self.assertEqual(f"{worker} successfully hired.", result)
        self.assertIn(worker, self.plantation.workers)
        self.assertEqual(['Pena'], self.plantation.workers)

    def test_if_len_works_when_zero(self):
        self.assertEqual(0, len(self.plantation))

    def test_if_len_works_properly_and_more_than_zero(self):
        self.plantation.plants = {'Ivan': 'Daisy', 'Pesho': 'Rose'}
        result = len(self.plantation)
        expected_result = len('Daisy') + len('Rose')
        self.assertEqual(expected_result, result)

    def test_plant__raises_error_if_worker_is_not_in_hired_workers(self):
        worker = 'Ivan'
        self.plantation.hire_worker('Pena')
        with self.assertRaises(ValueError) as error:
            self.plantation.planting(worker, 'Daisy')
        self.assertEqual(f"Worker with name {worker} is not hired!", str(error.exception))
        self.assertNotIn(worker, self.plantation.workers)

    def test_plant_raises_error_if_plantation_is_full(self):
        plantation = Plantation(2)
        plantation.workers.append('Ivan')
        plantation.workers.append('Pesho')
        plantation.plants = {'Ivan': 'Daisy', 'Pesho': 'Rose'}
        with self.assertRaises(ValueError) as error:
            plantation.planting('Ivan', 'Gerber')
        self.assertEqual("The plantation is full!", str(error.exception))

    def test_plant_adds_plant_when_worker_in_plants_dict(self):
        plantation = Plantation(10)
        plantation.workers.append('Ivan')
        plantation.workers.append('Pesho')
        plantation.plants = {'Ivan': [], 'Pesho': []}
        worker = 'Ivan'
        plant = 'Gerber'
        result = plantation.planting(worker, plant)
        self.assertEqual(f"{worker} planted {plant}.", result)
        self.assertEqual([plant], plantation.plants[worker])

    def test_plant_adds_plant_when_worker_is_not_in_plants_dict(self):
        plantation = Plantation(10)
        plantation.workers.append('Ivan')
        plantation.workers.append('Pesho')
        plantation.plants = {'Pesho': []}
        worker = 'Ivan'
        plant = 'Gerber'
        result = plantation.planting(worker, plant)
        self.assertEqual(f"{worker} planted it's first {plant}.", result)
        self.assertEqual([plant], plantation.plants[worker])

    def test_if_str_gives_proper_result(self):
        plantation = Plantation(3)
        plantation_workers = ['Ivan', 'Pesho']
        plantation.workers = plantation_workers
        plantation_plants = {'Pesho': ['Daisy']}
        plantation.plants = plantation_plants
        expected_result = [f"Plantation size: {3}"]
        expected_result.append(f'{", ".join(plantation_workers)}')
        for worker, plants in plantation_plants.items():
            expected_result.append(f"{worker} planted: {', '.join(plants)}")
        expected_result = '\n'.join(expected_result)
        self.assertEqual(expected_result, str(plantation))

    def test_if_repr_gives_proper_result(self):
        plantation = Plantation(3)
        plantation_workers = ['Ivan', 'Pesho']
        plantation.workers = plantation_workers
        plantation_plants = {'Pesho': ['Daisy']}
        plantation.plants = plantation_plants
        result = ''
        result += f'Size: {3}\n'
        result += f'Workers: {", ".join(plantation_workers)}'
        self.assertEqual(result, repr(plantation))
