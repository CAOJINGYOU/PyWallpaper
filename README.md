# PyWallpaper

[https://www.microsoft.com/zh-CN/download/details.aspx?id=35844](https://www.microsoft.com/zh-CN/download/details.aspx?id=35844)

设置windows桌面壁纸

	import win32api, win32con, win32gui
	
	def set_wallpaper(img_path):
	    # 打开指定注册表路径
	    reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
	    # 最后的参数:2拉伸,0居中,6适应,10填充,0平铺
	    win32api.RegSetValueEx(reg_key, "WallpaperStyle", 0, win32con.REG_SZ, "2")
	    # 最后的参数:1表示平铺,拉伸居中等都是0
	    win32api.RegSetValueEx(reg_key, "TileWallpaper", 0, win32con.REG_SZ, "0")
	    # 刷新桌面
	    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, img_path, win32con.SPIF_SENDWININICHANGE)
	
# 系统分辨率 # 

	from win32api import GetSystemMetrics
    width = GetSystemMetrics(0)
    height = GetSystemMetrics(1)

# Bing code #

	import urllib.request,re,sys,os
	
	def get_bing_backphoto():
	    if (os.path.exists('pictures')== False):
	        os.mkdir('pictures')        #设置图片下载路径，默认是文件的当前路径
	
	    for i in range(0,10):
	        url = 'http://cn.bing.com/HPImageArchive.aspx?format=js&idx='+str(i)+'&n=1&nc=1361089515117&FORM=HYLH1'
	        html = urllib.request.urlopen(url).read()
	
	        if html == 'null':
	            print( 'open & read bing error!')
	            sys.exit(-1)
	
	        html = html.decode('utf-8')
	        html = html.replace('/az/','http://cn.bing.com/az/')
	        reg = re.compile('"url":"(.*?)","urlbase"',re.S)
	        text = re.findall(reg,html)
	
	        for imgurl in text :
	            right = imgurl.rindex('/')
	            print(imgurl)
	            name = imgurl.replace(imgurl[:right+1],'')
	            savepath = 'pictures/'+ name
	            urllib.request.urlretrieve(imgurl, savepath)
	            print (name + ' save success!')
	
	get_bing_backphoto()

[https://www.cnblogs.com/hixin/p/7444214.html](https://www.cnblogs.com/hixin/p/7444214.html)

[https://www.cnblogs.com/TongZen/articles/3155403.html](https://www.cnblogs.com/TongZen/articles/3155403.html)

# Bing #

http://az517271.vo.msecnd.net/TodayImageService.svc/HPImageArchive?mkt=zh-cn&idx=%d'

https://github.com/rorschachhb/cleanBingDesktop

https://bingdesktop.com/gallery/cn

http://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&nc=1361089515117&FORM=HYLH1

http://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&nc=1490537646012&pid=hp&video=1

https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-cn

# unsplash #

https://source.unsplash.com/random