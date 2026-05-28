from datetime import datetime
from .connect import *
from .conf import *
from open_gopro.models import constants
import asyncio
import httpx

conf = get_conf()

async def send_start_video(gopro):
    ip_address = gopro.ip_address
    mode = "start"
    with httpx.AsyncClient() as client:
        await client.get(f"http://{ip_address}gopro/camera/shutter/{mode}")

async def send_stop_video(gopro):
    ip_address = gopro.ip_address
    mode = "stop"
    with httpx.AsyncClient() as client:
        await client.get(f"http://{ip_address}gopro/camera/shutter/{mode}")


def get_file_prefix():
    # Get current timestamp to use for prefix of filename
    current_time = datetime.now()
    # Convert to: YYYYMMDD_ HHMMSS format
    file_prefix = current_time.strftime("%Y%m%d_%H%M%S")
    return file_prefix

async def record(filename):
    try:
        front_gopro = await get_front_gopro()
        top_gopro = await get_top_gopro()
        short_gopro = await get_short_gopro()

        gopros = [front_gopro, top_gopro, short_gopro]

        for gopro in gopros:
            await send_start_video(gopro)

        return {
            "status": 200,
            "saved_file": filename
        }
    
    except Exception as e:
        print("Error:", e)
        return {
            "status": 500,
            "error": repr(e)
        }

async def stop_record(filename):
    try:
        front_gopro = await get_front_gopro()
        top_gopro = await get_top_gopro()
        short_gopro = await get_short_gopro()

        cameras = [[front_gopro, "Front"], [top_gopro, "Top"], [short_gopro, "Short"]]

        if os.path.isdir(conf["LOCAL_FOLDER"]) == False:
            os.mkdir(conf["LOCAL_FOLDER"])

        for camera in cameras:
            gopro = camera[0]
            view = camera[1]
            
            await send_stop_video(gopro)

            await asyncio.sleep(0.3)    

            video = await gopro.http_command.get_last_captured_media()
            new_file_path = os.path.join(conf["LOCAL_FOLDER"], f"{get_file_prefix()}_{ {filename} }_{view}.MP4")
            
            video_path = video.data.folder + '/' + video.data.file
            print(new_file_path)
            print(video_path)

            await gopro.http_command.download_file(camera_file=video_path, local_file=new_file_path)


        return {
            "status": 200,
            "saved_file": filename
        }
    except Exception as e:
        print("Error:", e)
        return {
            "status": 500,
            "error": repr(e)
        }
    
