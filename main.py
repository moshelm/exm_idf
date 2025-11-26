import csv

import uvicorn
from fastapi import UploadFile, FastAPI, File, APIRouter
from typing import Optional
import io
from obgects.base import Base
from placement_logic import *

app = FastAPI()

base = Base()

@app.post('/assignWithCsv')
def upload_file(file: UploadFile ):
    file_bytes = file.file.read()
    buffer = io.StringIO(file_bytes.decode('utf-8'))
    csv_file = csv.reader(buffer)
    header = next(csv_file)

    info_rows = list(csv_file)

    soldiers :list[Solider] = info_soldiers_to_objects(info_rows)

    report = ControlUnit(soldiers)
    report = report.placement_soldiers(base)
    response = {
        'soldiers deployed:':report.num_placements,
        'soldiers left:':len(report.waiting_list)
        }

    for soldier in soldiers:
        info_report = {f'{soldier}':soldier.location}
        response.update(info_report)

    return response



@app.get('/space')
def get_space_info():
    dorms = base.dorms

    return {}

@app.get('/search')
def search_by_personal_number():
    pass
@app.get('/waitingList')
def waiting_list():
    pass



def info_soldiers_to_objects(info: list[list]):
    soldiers_of_file = []
    for row in info:
        soldiers_of_file.append(Solider(row[0], row[1], row[2], row[3], row[4], row[5]))
    return soldiers_of_file


if __name__ == "__main__":

    uvicorn.run(app, host="127.0.0.1", port=8000)




