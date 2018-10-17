import sys,os
import wx

from BasicClass import DropTarget as DT
from BasicClass import FileCtrl as FC
from BasicClass import Button as BT
from BasicClass import PanelTemp as PT
from frame import NewListFrame as NLF

from collections import defaultdict


class AppFrame(wx.Frame):

    def __init__(self,args,argc,title = 'Demo'
                                        ,file_path = None):

        super(AppFrame,self).__init__(parent = None, id =-1, title = title, size = (800,600))

        self.SetBackgroundColour(wx.WHITE)
        self.file_path = file_path
        self.filesAndLinks = list()
        self.col_dict = {}
        panel = PT.MyPanel(self)

        self.filedropctrl = FC.FileCtrl(panel,size = (550,300),style = wx.LC_REPORT|wx.BORDER_SUNKEN)
        self.filedropctrl.InsertColumn(0,'File Path')
        self.filedropctrl.InsertColumn(1,'File Name')
        self.filedropctrl.InsertColumn(2,'File Type')
        self.filedropctrl.InsertColumn(3,'Number of Columns')

        helpTextTuple = (' '*40, 'Drop Files and Folders Here',' '*len('File Type')*2
                        ,' '*len('Number of Columns  ')*2)
        self.filedropctrl.Append(helpTextTuple)

        self.filedropctrl.SetDropTarget(DT.DropTarget(self.filedropctrl))
        self.filedropctrl.dropFunc = self.OnFilesDropped
        self.filedropctrl.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        self.filedropctrl.SetColumnWidth(1, wx.LIST_AUTOSIZE)
        self.filedropctrl.SetColumnWidth(2, wx.LIST_AUTOSIZE)
        self.filedropctrl.SetColumnWidth(3, wx.LIST_AUTOSIZE)



        # onButtonHandlers = self.OnListColButton
        # self.buttonpnl = ButtonPanel(panel,onButtonHandlers= onButtonHandlers,size = (-1,100))
        self.buttonpnl = BT.ButtonPanel(panel, ButtonName= 'List Column', onButtonHandlers= self.OnListColButton)
        box_h = wx.BoxSizer(wx.VERTICAL)
        box_v = wx.BoxSizer(wx.HORIZONTAL)
        box_v.AddSpacer(25)
        box_v.Add(self.filedropctrl,1,wx.EXPAND)
        box_v.AddSpacer(25)
        box_v.Add(self.buttonpnl,0,wx.EXPAND)

        box_h.AddSpacer(20)
        box_h.Add(box_v,-1,wx.EXPAND)
        box_h.AddSpacer(20)

        panel.SetSizer(box_h)
        panel.Fit()
        self.Centre()
        self.Show()
    # def OnColInfo(self,col_info):

    def OnFilesDropped(self, filenameDropDict):
       
        dropTarget = self.filedropctrl
        
        dropCoord = filenameDropDict[ 'coord' ]                 # Not used as yet.
        pathList = filenameDropDict[ 'pathList' ]
        basename_list = filenameDropDict[ 'basenameList' ]     # leaf folders, not basenames !
        pathname_list = filenameDropDict[ 'pathname' ]
        filetype_list = filenameDropDict['filetype']
        col_dict = filenameDropDict['col_info']
        self.col_dict.update(col_dict)
        for index in range(len(basename_list)):
            basename = basename_list[index]
            pathname = pathname_list[index]
            filetype = filetype_list[index]
            total_col = len(col_dict[basename])
            textTuple = (pathname,basename,filetype,total_col)
            dropTarget.WriteTextTuple(textTuple)


    def OnListColButton(self, event):
       
        currRow = self.filedropctrl.GetCurrRow()
        
        try:
            select_path = self.filedropctrl.GetItemText(currRow,col = 0)
            select_name = self.filedropctrl.GetItemText(currRow,col = 1)
            select_type = self.filedropctrl.GetItemText(currRow,col = 2)
            col_info = self.col_dict[select_name]
            ListCol_frame = NLF.NewListFrame(select_name,col_info,self.file_path)
            ListCol_frame.Show()
        except TypeError:
            self.Warn('You should select one row or drag one file at least')
        except OSError:
            self.Warn('You should select one row or drag one file at least')
        
    def Warn(self, message, caption = 'Warning!'):
        dlg = wx.MessageDialog(self, message, caption, wx.OK | wx.ICON_WARNING)
        dlg.ShowModal()
        dlg.Destroy() 

# class ButtonPanel(wx.Panel):

#     def __init__(self,parent = None, id = -1, onButtonHandlers = None,size = wx.DefaultSize,style = wx.DEFAULT_FRAME_STYLE):

#         super(ButtonPanel, self).__init__(parent = parent , id = id,size = size, style = style)

#         listALL = wx.Button(self,-1,'List Columns')

#         listALL.Bind(wx.EVT_LEFT_DOWN, onButtonHandlers)

#         btnPanel_innerHorzSzr = wx.BoxSizer( wx.HORIZONTAL )
#         btnPanel_innerHorzSzr.AddStretchSpacer( prop=1 )
#         btnPanel_innerHorzSzr.Add(listALL)
#         btnPanel_innerHorzSzr.AddSpacer( 25 )

#         btnPanel_innerHorzSzr.AddStretchSpacer( prop=1 )

#         btnPanel_outerVertSzr = wx.BoxSizer( wx.VERTICAL )
#         btnPanel_outerVertSzr.AddSpacer( 5 )
#         btnPanel_outerVertSzr.Add( btnPanel_innerHorzSzr, flag=wx.EXPAND )
#         btnPanel_outerVertSzr.AddSpacer( 5 )

#         self.SetSizer( btnPanel_outerVertSzr )
#         self.Layout()
