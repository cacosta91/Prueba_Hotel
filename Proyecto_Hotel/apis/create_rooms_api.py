from db.room_db import RoomInDB
from fastapi import APIRouter
from db.room_db import get_room, update_room, database_room, create_room
from models.room_models import RoomIn, RoomOut

from fastapi import FastAPI
from fastapi import HTTPException

router = APIRouter()


@router.post("/create_room/")
async def create_rooms(room: RoomInDB):
    return create_room(room)