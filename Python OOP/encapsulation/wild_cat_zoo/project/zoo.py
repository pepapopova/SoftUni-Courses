from project.animal import Animal

from encapsulation.wild_cat_zoo.project.cheetah import Cheetah
from encapsulation.wild_cat_zoo.project.lion import Lion
from encapsulation.wild_cat_zoo.project.tiger import Tiger


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget < price:
            return "Not enough budget"
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        money_needed = 0
        for worker in self.workers:
            money_needed += worker.salary
        # money_needed = sum(w.salary for w in self.workers)
        if money_needed <= self.__budget:
            self.__budget -= money_needed
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        money_needed = 0
        for animal in self.animals:
            money_needed += animal.money_for_care
        # money_needed = sum(a.money_for_care for a in self.animals)
        if money_needed <= self.__budget:
            self.__budget -= money_needed
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        # result += self.__get_entity_details(self.animals, 'Lion')
        # result += self.__get_entity_details(self.animals, 'Tiger')
        # result += self.__get_entity_details(self.animals, 'Cheetah')
        lions = [repr(a) for a in self.animals if isinstance(a, Lion)]
        result += f'-----{len(lions)} Lions:\n' + '\n'.join(lions) + '\n'
        tigers = [repr(a) for a in self.animals if isinstance(a, Tiger)]
        result += f'-----{len(tigers)} Tigers:\n' + '\n'.join(tigers) + '\n'
        cheetahs = [repr(a) for a in self.animals if isinstance(a, Cheetah)]
        result += f'-----{len(lions)} Cheetahs:\n' + '\n'.join(cheetahs) + '\n'
        return result.strip()

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        result += self.__get_entity_details(self.workers, 'Keeper')
        result += self.__get_entity_details(self.workers, 'Caretaker')
        result += self.__get_entity_details(self.workers, 'Vet')

        return result.strip()

    def __get_entity_details(self, entities, entity_type):
        counter = 0
        result = ''
        for entity in entities:
            if entity.__class__.__name__ == entity_type:
                counter += 1
                result += repr(entity) + '\n'
        return f'----- {counter} {entity_type}s:\n' + result





