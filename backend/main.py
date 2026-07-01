from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pydantic import BaseModel
from contextlib import asynccontextmanager

# Modules
from libs.status import get_status
from libs.preview import get_preview
from libs.record import record
from libs.record import stop_record
from libs.extras import *
from libs.zoom import top_camera_zoom
from libs.camera_manager import CameraManager

@asynccontextmanager
async def lifespan(app: FastAPI):
    global camera_manager
    camera_manager = await CameraManager.create()
    yield

app = FastAPI(lifespan=lifespan)

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
    cameraSide: str

camera_manager = None

@app.get("/status")
async def status():
    return await get_status(camera_manager)

@app.get("/preview")
async def preview():
    return await get_preview(camera_manager)

@app.get("/zoom/{percent}")
async def zoom(percent: str):
    return await top_camera_zoom(camera_manager, percent)

    
@app.get("/controls/{action}")
async def controls(action: str):
    match action:
        case "clear_gopros":
            return await clear_gopros(camera_manager)
        case "set_keep_alive":
            return await set_keep_alive(camera_manager)
        case "get_presets":
            return await get_preset(camera_manager)
        case "reset_connection":
            try: 
                camera_manager = await CameraManager.create()
                return {
                    "status": 200, 
                }
            except Exception as e:
                return {
                    "status": 500,
                    "error": repr(e)
                }
        case _:
            return {
                "status": 500,
                "error": "Route not found!"
            }

@app.post("/start_record")
async def start_recording(experiment: Experiment):
    return await record(experiment.name, camera_manager)

@app.post("/stop_record")
async def stop_recording(experiment: Experiment):
    return await stop_record(experiment.name, experiment.cameraSide, camera_manager)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
