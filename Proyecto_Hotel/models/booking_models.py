from pydantic import BaseModel
import datetime

class BookingIn(BaseModel):
    booking_number: str
    id_customer: int
    id_room: int
    date_begin: datetime
    date_end: datetime
    value: int
    

class BookingOut(BaseModel):
    state_booking: str
    id_customer: int
    booking_number: str
    id_room: int
    date: datetime
    date_end: datetime
    date_create: datetime
    value: int
