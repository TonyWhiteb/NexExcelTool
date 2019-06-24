import wx
# from wx.lib.pubsub import pub


class ButtonPanel(wx.Panel):

    def __init__(self,parent = None, id = -1,ButtonName_1 = None, onButtonHandlers_1 = None, ButtonName_2 = None, onButtonHandlers_2 = None):

        super(ButtonPanel, self).__init__(parent = parent , id = id)
        
        # pub.subscribe(self.OnListen, 'GetSelectCol')

        Button_1 = wx.Button(self,-1,ButtonName_1)
        Button_2 = wx.Button(self,-1,ButtonName_2)

        Button_1.Bind(wx.EVT_LEFT_DOWN, onButtonHandlers_1)
        Button_2.Bind(wx.EVT_LEFT_DOWN, onButtonHandlers_2)

        btnPanel_innerHorzSzr = wx.BoxSizer( wx.HORIZONTAL )
        btnPanel_innerHorzSzr.AddStretchSpacer( prop=1 )
        btnPanel_innerHorzSzr.Add(Button_1)
        btnPanel_innerHorzSzr.AddSpacer( 25 )
        btnPanel_innerHorzSzr.Add(Button_2)
        btnPanel_innerHorzSzr.AddSpacer( 25 )

        btnPanel_innerHorzSzr.AddStretchSpacer( prop=1 )

        btnPanel_outerVertSzr = wx.BoxSizer( wx.VERTICAL )
        btnPanel_outerVertSzr.AddSpacer( 5 )
        btnPanel_outerVertSzr.Add( btnPanel_innerHorzSzr, flag=wx.EXPAND )
        btnPanel_outerVertSzr.AddSpacer( 5 )

        self.SetSizer( btnPanel_outerVertSzr )
        self.Layout()

    # def OnListen(self, select_col):

    #     self.select_col = select_col