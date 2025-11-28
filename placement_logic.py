from obgects.solidrs import Solider
from obgects.base import Base

class ControlUnit:
    def __init__(self):
        self.base = Base()
        self.soldiers : list[Solider] = []
        self.waiting_list = []
        self.num_placements = 0

    def new_group_to_place(self,group):
        self.soldiers = group

    def find(self):
        self.soldiers.sort(reverse=True,key=lambda sol:sol.distance_base)

    def do_it(self):
        self.find()
        for sol in self.soldiers:
            if not self.base.is_base_full():
                self.base.add_tenant(sol)
                sol.is_placed = True
                self.num_placements += 1
            else:
                self.waiting_list.append(sol)



