from pydantic import BaseModel

class RoomIn(BaseModel):
    id_room: int
    room_number: str
    state: str
    capacity: int
    

class RoomOut(BaseModel):
    room_number: str
    state: str
    booking_number: str
    capacity: int