import sys,os
import wx

from BasicClass import DropTarget as DT
from BasicClass import FileCtrl as FC
from BasicClass import Button as BT
from BasicClass import PanelTemp as PT
from frame import NewListFrame as NLF
from frame import Preview 
from frame import Combination
from TEST import test

from collections import defaultdict
from wx.lib.pubsub import pub


class AppFrame(wx.Frame):

    def __init__(self,args,argc,title = 'Demo'
                                        ,file_path = None):

        super(AppFrame,self).__init__(parent = None, id =-1, title = title, size = (800,600))

        self.SetBackgroundColour(wx.WHITE)
        self.file_path = file_path
        self.filesAndLinks = list()
        self.dict_combination = {}
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
        self.buttonpnl = ButtonPanel(panel,onlistALL= self.OnListColButton, onGetSample = self.OnGetSample, onCombine= self.OnCombine,size = (-1,100))
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
        select_dict = {}
        self.filedropctrl.SetItem(index,3,str(len(select_col)))
        self.select_col = select_col
        self.select_index = select_index
        aPath = self.filedropctrl.GetItemText(index, col = 0)
        file_name = self.filedropctrl.GetItemText(index,col = 1)
        select_dict[file_name] = {}
        select_dict[file_name] = select_dict[file_name].fromkeys(self.select_col)
        for i in range(len(self.select_col)):
            select_dict[file_name][self.select_col[i]] = self.select_index[i]
        self.UpdateComDict(aPath,select_dict)




    def OnFilesDropped(self, filenameDropDict):
       
        dropTarget = self.filedropctrl
        # self.previous_drop = {}
        dropCoord = filenameDropDict[ 'coord' ]                 # Not used as yet.
        pathList = filenameDropDict[ 'pathList' ]
        basename_list = filenameDropDict[ 'basenameList' ]     # leaf folders, not basenames !
        pathname_list = filenameDropDict[ 'pathname' ]
        filetype_list = filenameDropDict['filetype']
        self.drop_col_dict = filenameDropDict['col_info']
        # print(pathList)
        # print(self.drop_col_dict)
        self.GetCombDict(self.drop_col_dict)
        for index in range(len(basename_list)):
            basename = basename_list[index]
            pathname = pathname_list[index]
            filetype = filetype_list[index]
            total_col = len(self.drop_col_dict[pathname][basename])
            textTuple = (pathname,basename,filetype,total_col)
            dropTarget.WriteTextTuple(textTuple)

    def UpdateComDict(self,aPath,col_dict):
        self.dict_combination[aPath].update(col_dict)
        # print(self.dict_combination)


    def GetCombDict(self,drop_col_dict):

        for aPath,filedict in drop_col_dict.items():
            x = self.dict_combination.get(aPath,None)
            for filename in filedict:
                
                if x == None:
                    self.dict_combination[aPath] = drop_col_dict[aPath]
                else:
                    try:
                        self.dict_combination[aPath][filename].update(drop_col_dict[aPath][filename])
                    except KeyError:
                        self.dict_combination[aPath][filename] = drop_col_dict[aPath][filename]

        # try:
        #     self.dict_combination
        # # if self.dict_combination =={}:
        # # for aPath,file_dict in drop_col_dict.items():
        # #     self.dict_combination[aPath].update(file_dict)

        # self.dict_combination.update(drop_col_dict) 
        # return self.dict_combination 

    
    def OnGetSample(self, event):

        currRow = self.filedropctrl.GetCurrRow()

        looptoken = 0
        try:
            select_path = self.filedropctrl.GetItemText(currRow,col = 0)
            select_name = self.filedropctrl.GetItemText(currRow,col = 1)
            os.chdir(select_path)
            if self.select_col == None:
                self.col_dict = {}
                with open(select_name) as Sample:
                    for line in Sample:
                        looptoken = looptoken + 1
                        if looptoken == 1:
                            column_list = line.split('\t')
                            self.col_dict.fromkeys(column_list)
                            continue
                        value_list = line.split('\t')
                        for i in range(len(column_list)):
                            self.col_dict[select_name][column_list[i]] = value_list[i]
                        if looptoken == 100:
                            break
            else:
                self.col_dict = {}
                with open(select_name) as Sample:
                    for line in Sample:
                        looptoken = looptoken + 1
                        if looptoken == 1:
                            column_list = line.split('\t')
                            self.col_dict = self.col_dict.fromkeys(self.select_col)
                            continue
                        value_list = line.split('\t')
                        for i in range(len(self.select_col)):
                            if self.col_dict[self.select_col[i]] == None:
                                self.col_dict[self.select_col[i]] = []
                            self.col_dict[self.select_col[i]].append(value_list[self.select_index[i]])
                        if looptoken == 100:
                            break
            preview_frame = Preview.MainFrame(looptoken,list(self.col_dict.keys()), self.col_dict)
            preview_frame.Show()
        except TypeError as e:
            print(e)
            self.Warn('You should select one row or drag one file at least')
        except OSError as e:
            print(e)
            self.Warn('You should select one row or drag one file at least')

    def OnCombine(self,event):

        combination_frame = Combination.MainFrame(self.dict_combination)
        combination_frame.Show()
        pass             

    def DataSlicer(self,file_dict):
        # CheckNum = self.CheckNum(file_dict)
        # if CheckNum = False:
        #     pass
        # elif CheckNum = True & 
        pass

            


    def CheckNum(self,file_dict):
        CheckNum = True
        for afile in file_dict:
            num_lines = sum(1 for line in open(afile))
            if num_lines > 1048577:
                self.Warn('This file exceed  excel maximum')
                CheckNum = False
            else:
                total_num = total_num + num_lines

        if total_num > 1048577:
            self.Warn('total data of these files exceed excel maximum')
            CheckNum = False
        else:
            CheckNum = True
        return CheckNum




    def OnListColButton(self, event):
       
        currRow = self.filedropctrl.GetCurrRow()
        # print(currRow)
        try:
            select_path = self.filedropctrl.GetItemText(currRow,col = 0)
            select_name = self.filedropctrl.GetItemText(currRow,col = 1)
            select_type = self.filedropctrl.GetItemText(currRow,col = 2)
            col_info = self.dict_combination[select_path][select_name]
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

    def __init__(self,parent = None, id = -1, onlistALL = None, onGetSample = None,onCombine = None,size = wx.DefaultSize,style = wx.DEFAULT_FRAME_STYLE):

        super(ButtonPanel, self).__init__(parent = parent , id = id,size = size, style = style)

        listALL = wx.Button(self,-1,'List Columns')
        GetSample = wx.Button(self,-1,'Get Sample')
        Combine = wx.Button(self,-1,'Combine')

        listALL.Bind(wx.EVT_LEFT_DOWN, onlistALL)
        GetSample.Bind(wx.EVT_LEFT_DOWN, onGetSample)
        Combine.Bind(wx.EVT_LEFT_DOWN, onCombine)


        btn_vert = wx.BoxSizer(wx.VERTICAL)
        btn_vert.AddSpacer(5)
        btn_vert.Add(listALL)
        btn_vert.AddSpacer(5)
        btn_vert.Add(GetSample)
        btn_vert.AddSpacer(5)
        btn_vert.Add(Combine)
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
