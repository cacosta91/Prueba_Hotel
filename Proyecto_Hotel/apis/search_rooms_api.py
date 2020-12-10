from fastapi import APIRouter
from db.room_db import database_room
from fastapi.exceptions import HTTPException

router = APIRouter()

@router.get("/searchrooms/{id_room}")
async def get_room_by_state(id_room : int):
    if id_room in database_room:
        return {"menssage":database_room[id_room]}
    raise HTTPException(status_code = 404, detail = "No hay habitaciones disponibles")

  