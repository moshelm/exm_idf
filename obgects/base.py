from obgects.dorm import Dorm
from obgects.solidrs import Solider
class Base:
    def __init__(self,name = 'The Seven Harvests', dorms = 2):
        self.name = name
        self.dorms = [Dorm(f'{i}') for i in range(1,dorms+1)]

    def add_dorm(self, dorm):
        self.dorms.append(dorm)

    def get_info_dorms(self) -> list[tuple]:
        info_dorms = []
        for dorm in self.dorms:
            dorm_info = dorm.rooms_full(), dorm.rooms_empty(), dorm.rooms_middel()
            info_dorms.append(dorm_info)
        return info_dorms

    def get_info_rooms(self) -> tuple[int]:
        info = self.get_info_dorms()
        num_rooms_empty = 0
        num_rooms_full = 0
        num_rooms_middel = 0
        for i in range(len(info)):
            num_rooms_full += info[i][0][0]
            num_rooms_empty += info[i][1][0]
            num_rooms_middel += info[i][2][0]
        return num_rooms_full, num_rooms_empty, num_rooms_middel

    def add_tenant(self, tenant:Solider, specific_dorm = None):
        dorm = None if specific_dorm is None else self.find_dorm(specific_dorm)
        if dorm:
            if not dorm.is_dorm_full():
                dorm.add_tenant(tenant)
            else:
                print('this dorm full')
        else:
            optional_dorm = self.returning_dorm_vacant()
            if optional_dorm:
                number_dorm ,dorm = optional_dorm
                dorm.add_tenant(tenant)

            else:
                print('the base full')

    def returning_dorm_vacant(self):
        for number_dorm , dorm in enumerate(self.dorms):
            if not dorm.is_dorm_full():
                return number_dorm, dorm
        return None

    def find_dorm(self, number_dorm:int):
        for dorm in self.dorms:
            if dorm.number_dorm == number_dorm:
                return dorm
        return None

    def is_base_full(self):
        return all([dorm.is_dorm_full() for dorm in self.dorms ])