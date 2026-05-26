from datetime import datetime
from .connect import *
from .conf import *
from open_gopro.models import constants

conf = get_conf()

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
            await gopro.http_command.set_shutter(shutter=constants.Toggle.ENABLE)

        return {
            "status": 200,
            "saved_file": filename
        }
    
    except Exception as e:
        return {
            "status": 500,
            "saved_file": filename
        }

async def stop_record(filename):
    try:
        front_gopro = await get_front_gopro()
        top_gopro = await get_top_gopro()
        short_gopro = await get_short_gopro()

        cameras = [[front_gopro, "Front"], [top_gopro, "Top"], [short_gopro, "Short"]]

        if os.path.isdir(conf["LOCAL_DIR"]) == False:
            os.mkdir(conf["LOCAL_DIR"])

        for camera in cameras:
            gopro = camera[0]
            view = camera[1]
            
            await gopro.http_command.set_shutter(shutter=constants.Toggle.DISABLE)
            
            video = await gopro.http_command.get_last_captured_media()
            new_file_path = os.path.join(conf["LOCAL_FOLDER"], get_file_prefix() + '_{' + filename + '}_' + view + '.MP4')
            
            print(new_file_path)
            await gopro.http_command.download_file(camera_file=video, local_file=new_file_path)


        return {
            "status": 200,
            "saved_file": filename
        }
    except Exception as e:
        return {
            "status": 500,
            "saved_file": filename
        }
    
