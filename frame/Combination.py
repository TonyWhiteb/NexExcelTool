import sys,os
import wx
import wx.grid as grid
import pandas as pd
from pandas import ExcelWriter
from operator import itemgetter
class ButtonPanel(wx.Panel):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent,onButton = None):
        """Constructor"""
        wx.Panel.__init__(self, parent = parent)

        button = wx.Button(self, label = "Save")
        button.Bind(wx.EVT_BUTTON, onButton)

        btn_vert = wx.BoxSizer(wx.VERTICAL)
        btn_vert.AddSpacer(5)
        btn_vert.Add(button)
        btn_vert.AddSpacer(5)


        btn_horz = wx.BoxSizer(wx.HORIZONTAL)
        btn_horz.Add(btn_vert,flag = wx.EXPAND)
        btn_horz.AddSpacer(25)
        self.SetSizer(btn_horz)
        self.Layout()


class GridPanel(wx.Panel):

    def __init__(self, parent,Sample_Dict,col_comb):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)
        NumOfRows = 100
        # aPath,file_name, col_list, col_comb, file_list,col_index = self.DictRefactory(file_dict)
        # # print(aPath,file_name,col_comb,col_list,file_list,col_index)
        # Sample_Dict = self.GetSampleData(aPath,file_name,file_list,col_list,col_index,col_comb)
        print(Sample_Dict)
        print(col_comb)
        MyGrid=grid.Grid(self)
        MyGrid.CreateGrid(NumOfRows,len(col_comb))
        for i in range(len(col_comb)):
            MyGrid.SetColLabelValue(i,col_comb[i])
            MyGrid.AutoSizeColLabelSize(i)
            value_list = Sample_Dict[col_comb[i]]
            for row in value_list:
                MyGrid.SetCellValue(row,i,str(value_list[row]))
            # for value in Sample_Dict[col_comb[i]]:
                
            #     row = Sample_Dict[col_comb[i]].index(value)
            #     MyGrid.SetCellValue(row,i,value)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(MyGrid, 0, wx.EXPAND)
        self.SetSizer(sizer)
    # def GetSampleData(self,aPath,file_name,file_list,col_list,col_index,col_comb):
    #     # self.Sample_dict = pd.DataFrame(columns = )
    #     df_final = pd.DataFrame(columns = col_comb)
    #     df_dict = {}
    #     # df_dict = df_dict.fromkeys(col_comb)
    #     NumOfRows = int(100/len(file_name))
    #     for aPath_index in range(len(aPath)):
    #         os.chdir(aPath[aPath_index])
        
    #         for afile_index in range(len(file_list[aPath_index])):

    #             looptoken = 0
    #             with open(file_name[afile_index]) as Sample:
    #                 for line in Sample:
                        
    #                     if looptoken ==0:
    #                         # df = pd.DataFrame(columns = col_list[afile_index])
    #                         df_dict = df_dict.fromkeys(col_list[afile_index])
    #                         looptoken = looptoken +1
    #                         continue
    #                     value_list = line.split('\t')
    #                     df_list = itemgetter(*col_index[afile_index])(value_list)
    #                     for i in range(len(col_list[afile_index])):
    #                         if df_dict[col_list[afile_index][i]] == None:
    #                             df_dict[col_list[afile_index][i]] = []
    #                         df_dict[col_list[afile_index][i]].append(df_list[i])
    
    #                     looptoken = looptoken +1
    #                     if looptoken == NumOfRows:
    #                         break
    #                 df = pd.DataFrame.from_dict(df_dict)
    #             df_final = df_final.append(df)
    #     df_final=df_final.reset_index(drop = True)
    #     sample_dict = df_final.to_dict()
    #     return sample_dict

                    
    # def DictRefactory(self,file_dict):
    #     aPath = []
    #     file_name = []
    #     file_list = []
    #     col_list = []
    #     col_comb = []
    #     col_index = []
    #     for key,value in file_dict.items():
    #         aPath_item = []
    #         aPath.append(key)
    #         for afile,col in value.items():
    #             item = []
    #             item_index = []
    #             file_name.append(afile)
    #             aPath_item.append(afile)
    #             for c,index in col.items():
    #                 col_comb.append(c)
    #                 item.append(c)
    #                 item_index.append(index)
    #             col_list.append(item)
    #             col_index.append(item_index)
    #     col_comb = list(set(col_comb))
    #     file_list.append(aPath_item)
        
    #     return aPath,file_name,col_list,col_comb,file_list,col_index



class MainFrame(wx.Frame):
    """"""

    #----------------------------------------------------------------------
    def __init__(self,file_dict):
        """Constructor"""
        wx.Frame.__init__(self,None,title="Preview", size=(800,600))
        self.file_dict = file_dict
        print(self.file_dict)
        aPath,file_name, col_list, col_comb, file_list,col_index,total = self.DictRefactory(file_dict)
        Sample_Dict = self.GetSampleData(aPath,file_name,file_list,col_list,col_index,col_comb)
        panel = wx.Panel(self,-1)
        self.btn_pnl = ButtonPanel(panel,onButton= self.onButton)
        self.grid_pnl = GridPanel(panel,Sample_Dict,col_comb)

        box_h = wx.BoxSizer(wx.VERTICAL)
        box_v = wx.BoxSizer(wx.HORIZONTAL)
        box_v.AddSpacer(25)
        box_v.Add(self.grid_pnl,1,wx.EXPAND)
        box_v.AddSpacer(25)
        box_v.Add(self.btn_pnl,0,wx.EXPAND)

        box_h.AddSpacer(20)
        box_h.Add(box_v,-1,wx.EXPAND)
        box_h.AddSpacer(20)

        panel.SetSizer(box_h)
        panel.Fit()
        self.Centre()
    def onButton(self,event):
        pass
    def TotalLines(self):
        pass
    def AddPanel(self):
        self.newPanel = ButtonPanel(self, 1, 1)
        self.sizer.Add(self.newPanel, 1, wx.EXPAND)
        self.sizer.Layout()
    def DictRefactory(self,file_dict):
        aPath = []
        file_name = []
        file_list = []
        col_list = []
        col_comb = []
        col_index = []
        total = 0
        for key,value in file_dict.items():
            aPath_item = []
            aPath.append(key)
            for afile,col in value.items():
                item = []
                item_index = []
                file_name.append(afile)
                aPath_item.append(afile)
                for c,index in col.items():
                    col_comb.append(c)
                    item.append(c)
                    item_index.append(index)
                col_list.append(item)
                col_index.append(item_index)
        col_comb = list(set(col_comb))
        file_list.append(aPath_item)
        for i in range(len(aPath)):
            os.chdir(aPath(i))
            for afile in file_list(i):
                aPath_total = 0
                with open(afile) as f:
                    afile_total = sum(1 for _ in f)
                aPath_total = afile_total + aPath_total
            total = total + aPath_total
        
        return aPath,file_name,col_list,col_comb,file_list,col_index,total
    def GetSampleData(self,aPath,file_name,file_list,col_list,col_index,col_comb):
        # self.Sample_dict = pd.DataFrame(columns = )
        df_final = pd.DataFrame(columns = col_comb)
        df_dict = {}
        # df_dict = df_dict.fromkeys(col_comb)
        NumOfRows = int(100/len(file_name))
        for aPath_index in range(len(aPath)):
            os.chdir(aPath[aPath_index])
        
            for afile_index in range(len(file_list[aPath_index])):

                looptoken = 0
                with open(file_name[afile_index]) as Sample:
                    for line in Sample:
                        
                        if looptoken ==0:
                            # df = pd.DataFrame(columns = col_list[afile_index])
                            df_dict = df_dict.fromkeys(col_list[afile_index])
                            looptoken = looptoken +1
                            continue
                        value_list = line.split('\t')
                        df_list = itemgetter(*col_index[afile_index])(value_list)
                        for i in range(len(col_list[afile_index])):
                            if df_dict[col_list[afile_index][i]] == None:
                                df_dict[col_list[afile_index][i]] = []
                            df_dict[col_list[afile_index][i]].append(df_list[i])
    
                        looptoken = looptoken +1
                        if looptoken == NumOfRows:
                            break
                    df = pd.DataFrame.from_dict(df_dict)
                df_final = df_final.append(df)
        df_final=df_final.reset_index(drop = True)
        sample_dict = df_final.to_dict()
        return sample_dict

# if __name__ == "__main__":
#     app = wx.App(False)
#     frame = MainFrame()
#     frame.Show()
#     app.MainLoop()