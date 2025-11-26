from room import Room


class Dorm:
    def __init__(self,number_dorm):
        self.rooms = [Room(number_room) for number_room in range(8)]
        self.number_dorm = number_dorm

    def add_tenant(self, tenant, specific_room  = None):
        for room in self.rooms:
            if specific_room and specific_room < len(self.rooms):
                if self.rooms[specific_room].is_room_full():
                    print('this room full')
                    return
                else:
                    self.rooms[specific_room].add_tenant(tenant)
                    print(f'{tenant} welcome to room {specific_room}')
            else:
                if not room.is_room_full():
                    room.add_tenant(tenant)
                    print(f'{tenant} welcome to room {self.rooms.index(room)} our choice')
                    return
        print('the dorm full')



    def is_dorm_full(self):
        return all([room.is_room_full() for room in self.rooms])