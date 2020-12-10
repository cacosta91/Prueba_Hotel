from typing import  Dict
from pydantic import BaseModel

class RoomInDB(BaseModel):
    id_room: int
    room_number: str
    state_room: str
    capacity: int    

database_room = Dict[int, RoomInDB]

database_room = {
    1: RoomInDB(**{"id_room":1,
                "room_number":"101",
                "state_room":"Disponible",
                "capacity":2}),

    2: RoomInDB(**{"id_room":2,
                "room_number":"102",
                "state_room":"Disponible",
                "capacity":2}),

    3: RoomInDB(**{"id_room":3,
                "room_number":"103",
                "state_room":"Disponible",
                "capacity":2}),
    4: RoomInDB(**{"id_room":3,
                "room_number":"201",
                "state_room":"Disponible",
                "capacity":3}),
    5: RoomInDB(**{"id_room":5,
                "room_number":"202",
                "state_room":"Ocupada",
                "capacity":3}),
}

def get_room(room_number: str):
    if room_number in database_room.keys():
        return database_room[room_number]
    else:
        return None

def update_room(room_in_db: RoomInDB):
    database_room[room_in_db.id_room] = room_in_db
    return room_in_db

def create_room(room_in_db: RoomInDB):
    autoid = len(database_room)+1
    room_in_db.id_room = autoid
    database_room[autoid] = room_in_db
    return room_in_db