from pydantic import BaseModel

class BookinIn(BaseModel):
    booking_number: str
    id_custumer: int
    state: str
    

class BookinrOut(BaseModel):
    state: str
    id_custumer: int
    booking_number: str
    state: str