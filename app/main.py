from fastapi import FastAPI, Query, Depends
from datetime import date
from pydantic import BaseModel

app = FastAPI()

class HotelSearchArgs:
    def __init__(
        self,
        location: str,
        date_from: date,
        date_to: date,
        has_spa: bool = Query(default = None),
        stars: int = Query(ge=1, le=5, default = None)
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.has_spa = has_spa
        self.stars = stars
        

class SHotel(BaseModel):
    address: str
    name: str
    stars: int

@app.get('/hotels')
def get_hotels(
    search_args: HotelSearchArgs = Depends()
) -> list[SHotel]:
    hotels = [
        {
            "address": "adr 1",
            "name": "First Hotel",
            "stars": 5,
        },
        {
            "address": "adr 2",
            "name": "Second Hotel",
            "stars": 3,
        },
    ]
    return hotels

class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date

@app.post('/bookings')
def add_booking(booking: SBooking):
    pass