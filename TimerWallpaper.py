import threading
import NetUtility
import SetWallpaper
import JsonConfig

timerWallpaper = None

imageFileWallpaper = None

timerStop = False

def TimerWallpaperStop():
    global timerStop
    timerStop = True
    global timerWallpaper
    timerWallpaper = threading.Timer(1, TimerWallpaper)

def TimerWallpaper():
    global timerStop
    global timerWallpaper
    if timerStop:
        if not timerWallpaper is None:
            timerWallpaper.cancel()
            timerWallpaper = None
        return

    jsonConfig = JsonConfig.InitJsonConfig()
    nInterval = int(jsonConfig["timer"])
    if jsonConfig["type"] == "0":
        timerWallpaper = threading.Timer(nInterval, TimerBingWallpaper)
    elif jsonConfig["type"] == "1":
        timerWallpaper = threading.Timer(nInterval, TimerUnsplashWallpaper)
    timerWallpaper.start()

def TimerBingWallpaper():
    imageFileName = NetUtility.DownloadBingImageFile()
    if not imageFileName is None:
        global imageFileWallpaper
        if imageFileWallpaper != imageFileName:
            SetWallpaper.SetWallpaper(imageFileName)
            imageFileWallpaper = imageFileName
    TimerWallpaper()

def TimerUnsplashWallpaper():
    imageFileName = NetUtility.DownloadUnsplashImageFile()
    if not imageFileName is None:
        global imageFileWallpaper
        if imageFileWallpaper != imageFileName:
            SetWallpaper.SetWallpaper(imageFileName)
            imageFileWallpaper = imageFileName
    TimerWallpaper()




