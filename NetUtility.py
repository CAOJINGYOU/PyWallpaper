import os
import sys
import traceback
import time
import datetime
import LogHandler
import requests
import json
import SetWallpaper

bingUrl = "https://www.bing.com"
bingJsonUrl = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-cn"

unsplashUrl = "https://source.unsplash.com/random/"

urlHeaders={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}

log = LogHandler.Logger("PyWallpaper")

def GetUrlText(url):
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url, headers=urlHeaders,timeout=1000, verify=False)
        '''if response.encoding == "ISO-8859-1":
            response.encoding = response.apparent_encoding'''
        response.raise_for_status()
    except requests.RequestException as e:
        strerro = "\nURL异常：" + str(traceback.format_exc()) + "\n出错URL：" + str(url)
        log.logger.error(strerro)
    else:
        return response.text

def DownloadUrlFile(strImageSrc, strNewUrl):
    response = requests.get(strImageSrc,headers=urlHeaders,timeout = 180, verify=False)
    with open(strNewUrl, 'wb') as f:
        f.write(response.content)

def DownloadBingImageFile():
    try:
        text = GetUrlText(bingJsonUrl)
        jsonText = json.loads(text)
        unsplashImageUrl = unsplashUrl+SetWallpaper.GetSystemMetricsXY()
        log.logger.info(unsplashImageUrl)
        unsplashImagePath = os.path.join(os.getcwd(), "image\\Unsplash")
        if os.path.exists(unsplashImagePath) == False:
            os.makedirs(unsplashImagePath)
        strDate = time.strftime("%Y-%m-%d-%H-%M-%S.jpg",time.localtime())
        unsplashImageFileName = os.path.join(unsplashImagePath, strDate)
        if os.path.exists(unsplashImageFileName) == False:
            DownloadUrlFile(unsplashImageUrl,unsplashImageFileName)
        if os.path.exists(unsplashImageFileName):
            return unsplashImageFileName
    except :
        log.logger.exception(sys.exc_info())
    else:
        return None

def DownloadUnsplashImageFile():
    try:
        text = GetUrlText(bingJsonUrl)
        jsonText = json.loads(text)
        bingImageUrl = bingUrl+jsonText["images"][0]["url"]
        log.logger.info(bingImageUrl)

        bingImagePath = os.path.join(os.getcwd(), "image\\Bing")
        if os.path.exists(bingImagePath) == False:
            os.makedirs(bingImagePath)
        strDate = datetime.date.today().strftime("%Y-%m-%d.jpg")
        bingImageFileName = os.path.join(bingImagePath, strDate)
        if os.path.exists(bingImageFileName) == False:
            DownloadUrlFile(bingImageUrl,bingImageFileName)
        if os.path.exists(bingImageFileName):
            return bingImageFileName
    except :
        log.logger.exception(sys.exc_info())
    else:
        return None
