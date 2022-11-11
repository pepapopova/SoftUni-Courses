class Mother:
    GENDER = 'Female'

    def __init__(self, name):
        self.name = name


class Dauhter(Mother):
    pass


child = Dauhter('Pepa')
print(child.GENDER)