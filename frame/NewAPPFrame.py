import sys,os
import wx

from BasicClass import DropTarget as DT
from BasicClass import FileCtrl as FC
from BasicClass import Button as BT
from BasicClass import PanelTemp as PT
from frame import NewListFrame as NLF
from frame import Preview 

from collections import defaultdict
from wx.lib.pubsub import pub


class AppFrame(wx.Frame):

    def __init__(self,args,argc,title = 'Demo'
                                        ,file_path = None):

        super(AppFrame,self).__init__(parent = None, id =-1, title = title, size = (800,600))

        self.SetBackgroundColour(wx.WHITE)
        self.file_path = file_path
        self.filesAndLinks = list()
        self.col_dict = {}
        self.select_col = None
        self.select_index = None
        # panel = PT.MyPanel(self)
        panel = wx.Panel(self,-1)
        pub.subscribe(self.OnListen, 'GetSelectCol')

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
        self.buttonpnl = ButtonPanel(panel,onlistALL= self.OnListColButton,size = (-1,100))
        # self.buttonpnl = BT.ButtonPanel(panel, ButtonName= 'List Column', onButtonHandlers= self.OnListColButton)
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
    def OnListen(self,index,select_index,select_col):
    
        self.filedropctrl.SetItem(index,3,str(len(select_col)))
        self.select_col = select_col
        self.select_index = select_index


    def OnFilesDropped(self, filenameDropDict):
       
        dropTarget = self.filedropctrl
        
        dropCoord = filenameDropDict[ 'coord' ]                 # Not used as yet.
        pathList = filenameDropDict[ 'pathList' ]
        basename_list = filenameDropDict[ 'basenameList' ]     # leaf folders, not basenames !
        pathname_list = filenameDropDict[ 'pathname' ]
        filetype_list = filenameDropDict['filetype']
        col_dict = filenameDropDict['col_info']
        for index in range(len(basename_list)):
            basename = basename_list[index]
            pathname = pathname_list[index]
            filetype = filetype_list[index]
            total_col = len(col_dict[basename])
            textTuple = (pathname,basename,filetype,total_col)
            dropTarget.WriteTextTuple(textTuple)

    def OnGetSample(self, event):

        currRow = self.filedropctrl.GetCurrRow()
        looptoken = 0

        try:
            select_path = self.filedropctrl.GetItemText(currRow,col = 0)
            select_name = self.filedropctrl.GetItemText(currRow,col = 1)
            os.chdir(select_path)
            if self.select_col == None:
                
                with open(select_name) as Sample:
                    for line in Sample:
                        looptoken = looptoken + 1
                        if looptoken == 1:
                            column_list = line.split('\t')
                            continue
                        

            # with open(select_name) as Sample:
            #     for line in Sample:
            #         looptoken = looptoken + 1 
            #         if looptoken == 1:
            #             column_list = line.split('\t')
            #             continue
            #         for filename, col_name in enumerate(self.)
                    
                    
        pass




    def OnListColButton(self, event):
       
        currRow = self.filedropctrl.GetCurrRow()
        
        try:
            select_path = self.filedropctrl.GetItemText(currRow,col = 0)
            select_name = self.filedropctrl.GetItemText(currRow,col = 1)
            select_type = self.filedropctrl.GetItemText(currRow,col = 2)
            col_info = self.col_dict[select_name]
            ListCol_frame = NLF.NewListFrame(currRow,select_name,col_info,self.file_path)
            ListCol_frame.Show()
        except TypeError:
            self.Warn('You should select one row or drag one file at least')
        except OSError:
            self.Warn('You should select one row or drag one file at least')
        
    def Warn(self, message, caption = 'Warning!'):
        dlg = wx.MessageDialog(self, message, caption, wx.OK | wx.ICON_WARNING)
        dlg.ShowModal()
        dlg.Destroy() 

class ButtonPanel(wx.Panel):

    def __init__(self,parent = None, id = -1, onlistALL = None, onGetSample = None,size = wx.DefaultSize,style = wx.DEFAULT_FRAME_STYLE):

        super(ButtonPanel, self).__init__(parent = parent , id = id,size = size, style = style)

        listALL = wx.Button(self,-1,'List Columns')
        GetSample = wx.Button(self,-1,'Get Sample')

        listALL.Bind(wx.EVT_LEFT_DOWN, onlistALL)
        GetSample.Bind(wx.EVT_LEFT_DOWN, onGetSample)


        btn_vert = wx.BoxSizer(wx.VERTICAL)
        btn_vert.AddSpacer(5)
        btn_vert.Add(listALL)
        btn_vert.AddSpacer(5)
        btn_vert.Add(GetSample)
        btn_vert.AddSpacer(5)

        btn_horz = wx.BoxSizer(wx.HORIZONTAL)
        btn_horz.AddStretchSpacer(prop = 1)
        btn_horz.Add(btn_vert,flag = wx.EXPAND)
        btn_horz.AddSpacer(25)

        # btnPanel_innerHorzSzr = wx.BoxSizer( wx.HORIZONTAL )
        # btnPanel_innerHorzSzr.AddStretchSpacer( prop=1 )
        # btnPanel_innerHorzSzr.Add(listALL)
        # btnPanel_innerHorzSzr.AddSpacer( 25 )

        # btnPanel_innerHorzSzr.AddStretchSpacer( prop=1 )

        # btnPanel_outerVertSzr = wx.BoxSizer( wx.VERTICAL )
        # btnPanel_outerVertSzr.AddSpacer( 5 )
        # btnPanel_outerVertSzr.Add( btnPanel_innerHorzSzr, flag=wx.EXPAND )
        # btnPanel_outerVertSzr.AddSpacer( 5 )

        # self.SetSizer( btnPanel_outerVertSzr )
        self.SetSizer(btn_horz)
        self.Layout()
