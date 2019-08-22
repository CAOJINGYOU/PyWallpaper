import sys
import LogHandler
import json

log = LogHandler.Logger("PyWallpaper")

def ReadJsonObj(filename):
    try:
        with open(filename, "r", encoding="utf-8") as jsonfile:
            jsonobj = json.load(jsonfile)
            return jsonobj
    except Exception as e:
        log.logger.exception(sys.exc_info())
    return None

def WriteJsonObj(jsonobj,filename):
    try:
        with open(filename, "w", encoding="utf-8") as jsonfile:
            json.dump(jsonobj,jsonfile,ensure_ascii=False,indent=4)
    except Exception as e:
        log.logger.exception(sys.exc_info())
