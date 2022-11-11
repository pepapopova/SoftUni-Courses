from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred


class HorseFactory:

    horse_types = {
        'Appaloosa': Appaloosa,
        'Thoroughbred': Thoroughbred
    }

    def create_horse(self, horse_type: str, horse_name: str, speed: int):
        if horse_type not in self.horse_types:
            raise RuntimeError('Invalid Horse Name')
        return self.horse_types[horse_type](horse_name, speed)