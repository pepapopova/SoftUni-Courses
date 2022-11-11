from project.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):
    @property
    def fish_type(self):
        return 'FreshwaterFish'

    def __init__(self, name: str):
        super().__init__(name, 50)



