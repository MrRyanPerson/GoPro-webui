from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pydantic import BaseModel

# Modules
from libs.status import get_status
from libs.preview import get_preview
from libs.record import record
from libs.record import stop_record
from libs.extras import *

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://localhost:4173",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Experiment(BaseModel):
    name: str

@app.get("/status")
async def status():
    return await get_status()

@app.get("/preview")
async def preview():
    return await get_preview()

@app.get("/controls/{action}")
async def controls(action: str):
    match action:
        case "clear_gopros":
            return await clear_gopros()
        case "set_keep_alive":
            return await set_keep_alive()
        case _:
            return {
                "status": 500
            }

@app.post("/start_record")
async def start_recording(experiment: Experiment):
    return await record(experiment.name)

@app.post("/stop_record")
async def stop_recording(experiment: Experiment):
    return await stop_record(experiment.name)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
