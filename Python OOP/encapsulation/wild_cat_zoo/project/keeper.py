from project.worker import Worker


class Keeper(Worker):
    def __int__(self, name, age, salary):
        super().__init__(name, age, salary)


