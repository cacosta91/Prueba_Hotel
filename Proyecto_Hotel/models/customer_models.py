from pydantic import BaseModel

class CostumerIn(BaseModel):
    name_customer: str
    last_name_customer: str
    number_phone_customer: str
    addres_customer: str
    booking_number: str
    
    

class CostumerOut(BaseModel):
    id_customer: int
    name_customer: str
    last_name_customer: str
    number_phone_customer: str
    addres_costumer: str
    booking_number: str