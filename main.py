import csv
import uvicorn
from fastapi import UploadFile, FastAPI, File
from typing import Optional
import io
from obgects.solidrs import Solider
from placement_logic import ControlUnit

app = FastAPI()
control = ControlUnit()

@app.post('/assignWithCsv')
def upload_file(file: UploadFile ):
    file_bytes = file.file.read()
    buffer = io.StringIO(file_bytes.decode('utf-8'))
    csv_file = csv.reader(buffer)
    header = next(csv_file)

    info_rows = list(csv_file)

    soldiers :list[Solider] = info_soldiers_to_objects(info_rows)

    control.new_group_to_place(soldiers)
    control.do_it()
    response = {
        'soldiers deployed:':control.num_placements,
        'soldiers left:':len(control.waiting_list)
        }

    for soldier in control.soldiers:
        info_report = {f'{soldier}':soldier.location if soldier.is_placed else 'not placed'}
        response.update(info_report)

    return response



@app.get('/space')
def get_space_info():
    info_rooms = control.base.get_info_rooms()
    return {'rooms full : ':info_rooms[0],
            'rooms empty : ':info_rooms[1],
            'rooms middel : ':info_rooms[2]}

@app.get('/search')
def search_by_personal_number(soldier_id:str):
    info = {}
    print(control.soldiers)
    for sol in control.soldiers:
        if int(sol.personal_number) == int(soldier_id):
            info['soldier'] = sol.__str__()
            if sol.is_placed:
                info['is placed'] = 'yes'
                dorm,room = sol.location.values()
                info['location'] = f'dorm : {dorm} room : {room}'
            else :
                info['is placed'] = 'no'
                info['status'] = 'waiting list'
            return info

    return {soldier_id: 'not in list'}

@app.get('/waitingList')
def waiting_list():
    return {'waiting list':[sol.__str__() for sol in control.waiting_list]}




def info_soldiers_to_objects(info: list[list]):
    soldiers_of_file = []
    for row in info:
        soldiers_of_file.append(Solider(row[0], row[1], row[2], row[3], row[4], int(row[5])))
    return soldiers_of_file


if __name__ == "__main__":

    uvicorn.run(app, host="127.0.0.1", port=8000)




