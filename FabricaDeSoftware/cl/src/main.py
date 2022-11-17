from typing import Union

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel


import Router

app = FastAPI()

class Item(BaseModel):
    cars: int

global TOTAL_PARKING_SPOTS
TOTAL_PARKING_SPOTS = 50

global AVAILABLE_SPOTS
AVAILABLE_SPOTS = TOTAL_PARKING_SPOTS

global USED_SPOTS
USED_SPOTS = 0

@app.get(Router.GET_MAIN_API_LANDING)
def ping():
    return {"Ping": "Pong"}


@app.get(Router.GET_AVAILABLE_SPACES)
def available_spaces():
    global USED_SPOTS
    return {"cars_parked": USED_SPOTS, "available_spaces": TOTAL_PARKING_SPOTS - USED_SPOTS}


@app.put(Router.PUT_TOTAL_SPACES)
def update_total_spaces(total_spaces: int):
    global TOTAL_PARKING_SPOTS
    TOTAL_PARKING_SPOTS = total_spaces
    return {"total_spaces": TOTAL_PARKING_SPOTS}

@app.post(Router.POST_USED_SPACES)
async def Used_Spots(item: Item):
    global USED_SPOTS
    USED_SPOTS = item.cars
    return item
#def update_available_spaces(used_spots: int):
#    global AVAILABLE_SPOTS
#    AVAILABLE_SPOTS = TOTAL_PARKING_SPOTS - used_spots
#    return {"available_spots": AVAILABLE_SPOTS}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
