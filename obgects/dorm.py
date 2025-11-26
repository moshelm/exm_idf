
from obgects.room import Room
from obgects.solidrs import Solider


class Dorm:
    def __init__(self,number_dorm):
        self.rooms = [Room(number_room) for number_room in range(8)]
        self.number_dorm = number_dorm

    def add_tenant(self, tenant:Solider, specific_room  = None):
        room = None if specific_room is None else self.find_room(specific_room)
        if room:
            if room.is_room_full():
                print('this room full')
                return
            else:
                room.add_tenant(tenant,self.number_dorm)
                tenant.dorm = self.number_dorm
                tenant.location['dorm'] = self.number_dorm
                print(f'{tenant} welcome to room {specific_room}')
        else:
            optional_room = self.returning_room_empty()
            if optional_room is None:
                print('the dorm full')
            else:
                number_room,room  = optional_room
                room.add_tenant(tenant,self.number_dorm)
                print(f'{tenant} welcome to room {number_room} our choice')
                return

    def returning_room_empty(self) -> tuple[int,Room]|None:
        for number_room, room in enumerate(self.rooms):
            if not room.is_room_full():
                return number_room , room
        return None


    def is_dorm_full(self):
        return all([room.is_room_full() for room in self.rooms])

    def find_room(self,room_number:int):
        for room in self.rooms:
            if room.number_room == room_number:
                return room
        return None
