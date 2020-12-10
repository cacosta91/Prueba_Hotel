from datetime import datetime
from pydantic import BaseModel

class BookingInDB(BaseModel):
    booking_number: int
    id_room: int
    id_customer: int
    state_booking: str
    date_create: datetime = datetime.now()
    date_end: datetime
    date_create: datetime
    value: int
    id_room: int
    

database_booking = []
generator = {"id":0}

def save_booking(booking_in_db: BookingInDB):
    generator["id"] = generator["id"] + 1
    booking_in_db.booking_number = generator["id"]
    database_booking.append(booking_in_db)
    return booking_in_db