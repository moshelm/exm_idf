from obgects.solidrs import Solider
from obgects.base import Base

class ControlUnit:
    def __init__(self, info:list[Solider]):
        self.soldiers = info
        self.waiting_list = []
        self.num_placements = 0

    def not_placed_yet(self):
        return [soldier for soldier in self.soldiers if not soldier.is_placed]

    def placement_soldiers(self,base:Base):
        while True:
            farthest = self.find_farthest()
            for sol in self.soldiers:

                if farthest:
                    if farthest == sol:
                        if not base.is_base_full():
                            base.add_tenant(farthest)
                            self.num_placements += 1
                            sol.is_placed = True
                        else:
                            self.waiting_list.extend(self.soldiers)
                            return self.soldiers
                else:
                    return self.soldiers


    def find_farthest(self):
        if self.soldiers:
            farthest_location = max([sol.distance_base for sol in self.soldiers if not sol.is_placed])
            farthest = None
            for soldier in self.soldiers:
                if soldier.distance_base == farthest_location :
                    farthest = soldier
            return farthest
        else:
            return None

