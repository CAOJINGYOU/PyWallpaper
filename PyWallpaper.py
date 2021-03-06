import wx
import os
import sys
import wx.adv
import JsonConfig
import SetWallpaper
import NetUtility
import ImageUtility
import TimerWallpaper

def ResourcePath(relativePath):
    basePath = getattr(sys,"_MEIPASS",os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(basePath,relativePath)

icoFileName = os.path.join(ResourcePath("."), "desktop.ico")

class PyWallpaperApp(wx.App):
    def OnInit(self):
        jsonConfig = JsonConfig.InitJsonConfig()

        self.thisFrame =WallpaperFrame(None,"PyWallpaper")

        TimerWallpaper.TimerWallpaper()

        return True

    def OnExit(self):
        self.thisFrame.DestroyTaskBarIcon()
        TimerWallpaper.TimerWallpaperStop()
        return True

class MyTaskBarIcon(wx.adv.TaskBarIcon):
    ID_ABOUT = wx.NewId()  # 菜单选项“关于”的ID
    ID_EXIT = wx.NewId()  # 菜单选项“退出”的ID
    ID_SHOW_WEB = wx.NewId()  # 菜单选项“显示页面”的ID
    ID_TEM_BING = wx.NewId()
    ID_TEM_UNSPLASH_RANDOM = wx.NewId()
    ID_TEM_UNSPLASH_YHCAO = wx.NewId()

    def __init__(self,frame,title):
        wx.adv.TaskBarIcon.__init__(self)
        self.frame = frame
        self.SetIcon(wx.Icon(icoFileName), title)  # 设置图标和标题
        self.Bind(wx.EVT_MENU, self.onAbout, id=self.ID_ABOUT)  # 绑定“关于”选项的点击事件
        self.Bind(wx.EVT_MENU, self.onExit, id=self.ID_EXIT)  # 绑定“退出”选项的点击事件
        self.Bind(wx.EVT_MENU, self.onShowWeb, id=self.ID_SHOW_WEB)  # 绑定“显示页面”选项的点击事件
        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DCLICK, self.OnTaskBarLeftDClick)

        self.Bind(wx.EVT_MENU, self.onTemBing, id=self.ID_TEM_BING)
        self.Bind(wx.EVT_MENU, self.onTemUnsplashRandom, id=self.ID_TEM_UNSPLASH_RANDOM)
        self.Bind(wx.EVT_MENU, self.onTemUnsplashYhcao, id=self.ID_TEM_UNSPLASH_YHCAO)

    # “关于”选项的事件处理器
    def onAbout(self, event):
        wx.MessageBox('程序作者：yhcao\n最后更新日期：2019-8-25', "关于")

    # “退出”选项的事件处理器
    def onExit(self, event):
        wx.Exit()
        #wx.Colse()

    # “显示页面”选项的事件处理器
    def onShowWeb(self, event):
        if not self.frame.IsShown():
            self.frame.Show(True)
        self.frame.Raise()

    def onTemBing(self,event):
        if not self.frame.IsShown():
            jsonObj = {"type":"0","timer":"3600","unsplashurl":"https://source.unsplash.com/random/"}
            JsonConfig.WriteJsonConfig(jsonObj)
            TimerWallpaper.TimerWallpaperRestart()

    def onTemUnsplashRandom(self, event):
        if not self.frame.IsShown():
            jsonObj = {"type":"1","timer":"3600","unsplashurl":"https://source.unsplash.com/random/"}
            JsonConfig.WriteJsonConfig(jsonObj)
            TimerWallpaper.TimerWallpaperRestart()
    def onTemUnsplashYhcao(self, event):
        if not self.frame.IsShown():
            jsonObj = {"type":"1","timer":"3600","unsplashurl":"https://source.unsplash.com/user/yhcao/likes/"}
            JsonConfig.WriteJsonConfig(jsonObj)
            TimerWallpaper.TimerWallpaperRestart()

    # 创建菜单选项
    def CreatePopupMenu(self):
        menu = wx.Menu()
        menu.Append(self.ID_SHOW_WEB, "显示")

        menuTemplate = wx.Menu()
        menuTemplate.Append(self.ID_TEM_BING, "bing")
        menuTemplate.Append(self.ID_TEM_UNSPLASH_RANDOM, "unsplash-random")
        menuTemplate.Append(self.ID_TEM_UNSPLASH_YHCAO, "unsplash-yhcao")

        menu.AppendMenu(wx.ID_ANY, "模板",menuTemplate)
        menu.Append(self.ID_ABOUT, "关于")
        menu.Append(self.ID_EXIT, "退出")

        return menu


    def OnTaskBarLeftDClick(self, event):
        if self.frame.IsIconized():
            self.frame.Iconize(False)
        if not self.frame.IsShown():
            self.frame.Show(True)
        self.frame.Raise()

class WallpaperFrame(wx.Frame):
    def __init__(self, parent, title):
        super(WallpaperFrame, self).__init__(parent, title=title,size=(450, 200))

        self.SetIcon(wx.Icon(icoFileName))

        self.taskBarIcon = MyTaskBarIcon(self,title)  # 显示系统托盘图标
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.Bind(wx.EVT_SHOW, self.OnShow)

        self.InitUI()

        self.Centre()
        #self.Show()


    def InitUI(self):
        self.panel = wx.Panel(self)
        self.sizer = wx.GridBagSizer(1, 1)

        self.textCtrlSourceJson = wx.TextCtrl(self.panel,style = wx.TE_MULTILINE)
        self.sizer.Add(self.textCtrlSourceJson, pos=(0, 0), flag=wx.ALIGN_CENTER | wx.ALL | wx.EXPAND,
                       border=10)

        self.sizer.AddGrowableCol(0)
        self.sizer.AddGrowableRow(0)

        self.panel.SetSizerAndFit(self.sizer)

    def OnShow(self, event):
        if self.IsShown():
            jsonConfig = JsonConfig.InitJsonConfig()
            jsonString = JsonConfig.JsonObjToString(jsonConfig)
            self.textCtrlSourceJson.SetValue(jsonString)
        else:
            jsonString = self.textCtrlSourceJson.GetValue()
            jsonObj = JsonConfig.StringToJsonObj(jsonString)
            JsonConfig.WriteJsonConfig(jsonObj)
            TimerWallpaper.TimerWallpaperRestart()

    def OnClose(self, event):
        self.Hide()
        #self.taskBarIcon.Destroy()
        #self.Destroy()

    def DestroyTaskBarIcon(self):
        self.taskBarIcon.Destroy()
        self.Destroy()

if __name__ == "__main__":
    app = PyWallpaperApp()
    app.MainLoop()