import wx
import os
import sys
import wx.adv
import JsonConfig
import SetWallpaper
import NetUtility
import ImageUtility

def ResourcePath(relativePath):
    basePath = getattr(sys,"_MEIPASS",os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(basePath,relativePath)

icoFileName = os.path.join(ResourcePath("."), "desktop.ico")

jsonFileName = "config.json"

jsonConfig = None

class PyWallpaperApp(wx.App):
    def OnInit(self):
        jsonConfig = JsonConfig.ReadJsonObj(jsonFileName)
        if jsonConfig is None:
            jsonConfig ={"type":"0"}
            JsonConfig.WriteJsonObj(jsonConfig,jsonFileName)
        if jsonConfig["type"] == "0":
            BingWallpaperFrame(None)
        elif jsonConfig["type"] == "1":
            UnsplashWallpaperFrame(None)
        return True

class MyTaskBarIcon(wx.adv.TaskBarIcon):
    ID_ABOUT = wx.NewId()  # 菜单选项“关于”的ID
    ID_EXIT = wx.NewId()  # 菜单选项“退出”的ID
    ID_SHOW_WEB = wx.NewId()  # 菜单选项“显示页面”的ID

    def __init__(self,frame,title):
        wx.adv.TaskBarIcon.__init__(self)
        self.frame = frame
        self.SetIcon(wx.Icon(icoFileName), title)  # 设置图标和标题
        self.Bind(wx.EVT_MENU, self.onAbout, id=self.ID_ABOUT)  # 绑定“关于”选项的点击事件
        self.Bind(wx.EVT_MENU, self.onExit, id=self.ID_EXIT)  # 绑定“退出”选项的点击事件
        self.Bind(wx.EVT_MENU, self.onShowWeb, id=self.ID_SHOW_WEB)  # 绑定“显示页面”选项的点击事件
        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DCLICK, self.OnTaskBarLeftDClick)

    # “关于”选项的事件处理器
    def onAbout(self, event):
        wx.MessageBox('程序作者：yhcao\n最后更新日期：2019-8-22', "关于")

    # “退出”选项的事件处理器
    def onExit(self, event):
        wx.Exit()

    # “显示页面”选项的事件处理器
    def onShowWeb(self, event):
        if not self.frame.IsShown():
            self.frame.Show(True)
        self.frame.Raise()

    # 创建菜单选项
    def CreatePopupMenu(self):
        menu = wx.Menu()
        for mentAttr in self.getMenuAttrs():
            menu.Append(mentAttr[1], mentAttr[0])
        return menu

    # 获取菜单的属性元组
    def getMenuAttrs(self):
        return [('进入程序', self.ID_SHOW_WEB),
                ('关于', self.ID_ABOUT),
                ('退出', self.ID_EXIT)]

    def OnTaskBarLeftDClick(self, event):
        if self.frame.IsIconized():
            self.frame.Iconize(False)
        if not self.frame.IsShown():
            self.frame.Show(True)
        self.frame.Raise()

class WallpaperFrame(wx.Frame):
    def __init__(self, parent, title,size):
        super(WallpaperFrame, self).__init__(parent, title=title,size=size)

        self.SetIcon(wx.Icon(icoFileName))

        MyTaskBarIcon(self,title)  # 显示系统托盘图标
        self.Bind(wx.EVT_CLOSE, self.OnClose)

        self.InitUI()

        self.Centre()
        self.Show()

    def InitUI(self):
        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(0, 0)
        #sizer.AddGrowableCol(0)
        #sizer.AddGrowableRow(0)

        panel.SetSizerAndFit(sizer)

    def OnClose(self, event):
        self.Hide()

class BingWallpaperFrame(WallpaperFrame):
    def __init__(self, parent):
        super(BingWallpaperFrame, self).__init__(parent, title='BingWallpaper',size=(600, 600))

        imageFileName = NetUtility.DownloadBingImageFile()
        if not imageFileName is None:
            #strTempFile = os.path.join(os.getcwd(),"image\\temp.jpg")
            #ImageUtility.compress_image(imageFileName,strTempFile)
            SetWallpaper.SetWallpaper(imageFileName)

class UnsplashWallpaperFrame(WallpaperFrame):
    def __init__(self, parent):
        super(UnsplashWallpaperFrame, self).__init__(parent, title='UnsplashWallpaper',size=(600, 600))
        SetWallpaper.SetWallpaper(r"E:\code\github\CAOJINGYOU\PyWallpaper\wxPython2.jpg")
if __name__ == "__main__":
    app = PyWallpaperApp()
    app.MainLoop()