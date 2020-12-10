import datetime
from fastapi import FastAPI, HTTPException
from fastapi import FastAPI
from apis import search_rooms_api, create_rooms_api
""" , search_booking_api, search_rooms_api, create_rooms_api """


app = FastAPI()

app.include_router(search_rooms_api.router)
""" pp.include_router(search_booking_api.router)
app.include_router(search_rooms_api.router) """
app.include_router(create_rooms_api.router)