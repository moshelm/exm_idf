from dorm import Dorm

class Base:
    def __init__(self,name = 'The Seven Harvests', dorms = 2):
        self.name = name
        self.dorms = [Dorm(f'{i}') for i in range(dorms)]

    def add_dorm(self, dorm):
        self.dorms.append(dorm)

    def is_base_full(self):
        return all([dorm.is_dorm_full() for dorm in self.dorms ])