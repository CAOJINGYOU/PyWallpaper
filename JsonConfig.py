import sys
import LogHandler
import json

jsonFileName = "config.json"

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

def InitJsonConfig():
    jsonConfig = ReadJsonObj(jsonFileName)
    if jsonConfig is None:
        jsonConfig ={"type":"1","timer":"3600","unsplashurl":"https://source.unsplash.com/random/"}
        WriteJsonObj(jsonConfig,jsonFileName)
    return jsonConfig

def WriteJsonConfig(jsonConfig):
    WriteJsonObj(jsonConfig,jsonFileName)

def ReadJsonObj(filename):
    try:
        with open(filename, "r", encoding="utf-8") as jsonfile:
            jsonobj = json.load(jsonfile)
            return jsonobj
    except Exception as e:
        log.logger.exception(sys.exc_info())
    return None

def JsonObjToString(jsonobj):
    try:
        return json.dumps(jsonobj,ensure_ascii=False,indent=4)
    except Exception as e:
        log.logger.exception(sys.exc_info())

def StringToJsonObj(jsonString):
    try:
        return json.loads(jsonString)
    except Exception as e:
        log.logger.exception(sys.exc_info())
