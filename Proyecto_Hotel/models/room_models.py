from pydantic import BaseModel

class RoomIn(BaseModel):
    room_number: str
    state_room: str
    capacity: int
    

class RoomOut(BaseModel):
    id_room: int
    room_number: str
    state_room: str
    capacity: int