import wx
import wx.grid as grid

class GridPanel(wx.Panel):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent = parent)

        self.txtOne = wx.StaticText(self, -1, label = "piradoba", pos = (20,10))
        self.txtPlace = wx.TextCtrl(self, pos = (20,30))
        self.txtTwo = wx.StaticText(self, -1, label = "", pos = (20,40))

        button = wx.Button(self, label = "search", pos = (20,70))
        button.Bind(wx.EVT_BUTTON, self.onButton)

    def onButton(self, event):
        var=self.txtPlace.GetValue()
        if len(var) == 9 or len(var) == 11:
            print ("???")
        # GridPanel->SplitterWindow->MainFrame ( 2x GetParent() )
        self.GetParent().GetParent().AddPanel()

class ButtonPanel(wx.Panel):

    def __init__(self, parent,a,b):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)

        MyGrid=grid.Grid(self)
        MyGrid.CreateGrid(a, b)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(MyGrid, 0, wx.EXPAND)
        self.SetSizer(sizer)

class MainFrame(wx.Frame):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="test", size=(800,600))

        self.splitter = wx.SplitterWindow(self)

        self.panelOne = GridPanel(self.splitter)
        self.panelTwo = ButtonPanel(self.splitter, 1, 1)

        self.splitter.SplitHorizontally(self.panelOne, self.panelTwo)
        self.splitter.SetMinimumPaneSize(20)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.splitter, 2, wx.EXPAND)

        self.SetSizer(self.sizer)

    def AddPanel(self):
        self.newPanel = ButtonPanel(self, 1, 1)
        self.sizer.Add(self.newPanel, 1, wx.EXPAND)
        self.sizer.Layout()

if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    frame.Show()
    app.MainLoop()