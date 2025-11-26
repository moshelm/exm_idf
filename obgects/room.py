

MAX_TENANTS = 8

class Room:
    def __init__(self,number_room):
        self.number_room = number_room
        self.number_tenants = 0
        self.tenants = []

    def add_tenant(self, tenant):
        if self.number_tenants <= MAX_TENANTS:
            self.number_tenants +=1
            self.tenants.append(tenant)
        else:
            print('room full')

    def remove_tenant(self,tenant):
        if self.number_tenants > 0:
            self.number_tenants -= 1
            self.tenants.remove(tenant)
        else:
            print('empty room')

    def is_room_full(self):
        return self.number_tenants == MAX_TENANTS

