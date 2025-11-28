
class Solider:
    def __init__(self,personal_number, first_name, last_name, gender, city, distance_from_base):
        self.personal_number = personal_number
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.distance_base = distance_from_base
        self.gender = gender
        self.is_placed = False
        self.location = {'dorm':None,'room':None}


    def insert_location(self,dorm, room):
        self.location['room'] = room
        self.location['dorm'] = dorm
        self.is_placed = True

    def __str__(self):
        return f'{self.first_name} {self.last_name} ID : {self.personal_number} dis : {self.distance_base}'
