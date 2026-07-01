

async def top_camera_zoom(CameraManager, zoom):
    try: 

        if int(zoom) > 100 or int(zoom) < 0:
            return {
                "status": 500,
                "error": "Zoom Out Of Range. (0-100)"
            }
        
        top_gopro = CameraManager.top_gopro

        # Zoom is between 0 and 100 where 0 is minimum zoom and 100 is maximum
        await top_gopro.http_command.set_digital_zoom(percent=int(zoom))

        return {
            "status": 200
        }
    except Exception as e:
        return {
            "status": 500,
            "error": repr(e)
        }





