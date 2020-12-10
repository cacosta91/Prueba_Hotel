import datetime
from fastapi import FastAPI, HTTPException
from fastapi import FastAPI
from apis import search_rooms_api, create_rooms_api
""" , search_booking_api, search_rooms_api, create_rooms_api """

api = FastAPI()

api.include_router(search_rooms_api.router)
"""app.include_router(search_booking_api.router)
app.include_router(search_rooms_api.router) """
api.include_router(create_rooms_api.router)