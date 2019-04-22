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
        # aPath,file_name, col_dict, col_comb, file_list,col_index = self.DictRefactory(file_dict)
        # # print(aPath,file_name,col_comb,col_dict,file_list,col_index)
        # Sample_Dict = self.GetSampleData(aPath,file_name,file_list,col_dict,col_index,col_comb)
        # print(Sample_Dict)
        # print(col_comb)
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
    # def GetSampleData(self,aPath,file_name,file_list,col_dict,col_index,col_comb):
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
    #                         # df = pd.DataFrame(columns = col_dict[file_list[aPath_index][afile_index]])
    #                         df_dict = df_dict.fromkeys(col_dict[file_list[aPath_index][afile_index]])
    #                         looptoken = looptoken +1
    #                         continue
    #                     value_list = line.split('\t')
    #                     df_list = itemgetter(*col_index[afile_index])(value_list)
    #                     for i in range(len(col_dict[file_list[aPath_index][afile_index]])):
    #                         if df_dict[col_dict[file_list[aPath_index][afile_index]][i]] == None:
    #                             df_dict[col_dict[file_list[aPath_index][afile_index]][i]] = []
    #                         df_dict[col_dict[file_list[aPath_index][afile_index]][i]].append(df_list[i])
    
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
    #     col_dict = []
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
    #             col_dict.append(item)
    #             col_index.append(item_index)
    #     col_comb = list(set(col_comb))
    #     file_list.append(aPath_item)
        
    #     return aPath,file_name,col_dict,col_comb,file_list,col_index



class MainFrame(wx.Frame):
    """"""

    #----------------------------------------------------------------------
    def __init__(self,file_dict):
        """Constructor"""
        wx.Frame.__init__(self,None,title="Preview", size=(800,600))
        self.file_dict = file_dict
        self.count = 5
        # print(self.file_dict)
        self.aPath,self.file_name, self.col_dict, self.col_comb, self.file_list,self.col_index,self.total = self.DictRefactory(file_dict)
        Sample_Dict = self.GetSampleData(self.aPath,self.file_name,self.file_list,self.col_dict,self.col_index,self.col_comb)
        panel = wx.Panel(self,-1)
        self.btn_pnl = ButtonPanel(panel,onButton= self.onButton)
        self.grid_pnl = GridPanel(panel,Sample_Dict,self.col_comb)

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
        currentDirctory = os.getcwd()
        # Final, Slicer, multi = self.DataSlicer(self.total)
        # print('Final:%s' %(Final))
        # print('Slicer:%s' %(Slicer))
        # print('multi:%s' %(multi))
        dlg = wx.FileDialog(
            self, message = 'Save File As',
            defaultDir = currentDirctory,
            defaultFile = "", wildcard = "Excel files (*.xlsx)|*.xlsx",
            style = wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT

        )
        if dlg.ShowModal() == wx.ID_OK:
            SaveFileName = dlg.GetFilename()
            path = dlg.GetPath()
            data_total = 0

            if self.total > self.count:
                for aPath_index in range(len(self.aPath)):
                    os.chdir(self.aPath(aPath_index))
                    file_list = self.file_list[aPath_index]

                    for afile_index in range(len(file_list)):
                        Final, Slicer, file_total = self.FileDataSlicer(file_list[afile_list],self.aPath[aPath_index])
                        with open(file_list[afile_list]) as f:
                            for line in f:
                                value_list = line.split('\t')
                                df_list = list(itemgetter(*self.col_index[afile_index])(value_list))

            # sheet_list = self.SheetName(Slicer)
            for aPath_index in range(len(self.aPath)):
                    os.chdir(self.aPath(aPath_index))
                    looptoken = 0
                    file_list = self.file_list[aPath_index]

                    for afile_index in range(len(file_list)):
                        Final, Slicer,file_total = self.FileDataSlicer(file_list[afile_list],self.aPath[aPath_index])
                        data_total = file_total + data_total
                        
                        if data_total == self.total:
                            sheet_list = self.SheetName(Slicer)
                            df_dict = {}
                            with open(file_list[afile_list]) as f:
                                readtoken = 0
                                for line in f:
                                    value_list = line.split('\t')
                                    df_list = list(itemgetter(*self.col_index[afile_index])(value_list))
                                    if readtoken == 0:
                                        col = df_list
                                        df_dict = df_dict.fromkeys(col)
                                        for i in range(len(col)):
                                            df_dict[col[i]] = []
                                        readend = self.count
                                    
    def MoreDataSave(self,Slicer,Final,df_list):
        sheet_list = self.SheetName(Slicer)
        df_dict = {}





    def FileDataSlicer(self,filename,path): 
        os.chdir(path)
        Slicer = 1
        with open(filename) as f:
            file_total = sum(1 for _ in f) -1
        if file_total > self.count:
            pre_slicer = int(file_total / self.count)
            Slicer = pre_slicer +1
            Final = file_total - (pre_slicer * self.count)
        else:
            Final = file_total
        return Final,Slicer,file_total
            # if multi == False:
            #     df = self.ErrorSave()
            #     writer = ExcelWriter(SaveFileName)
            #     df.to_excel(writer,'Sheet1',index = False)
            #     writer.save()
            # elif multi == True:
            #     sheet_list = self.SheetName(Slicer)
            #     for aPath_index in range(len(self.aPath)):
            #         os.chdir(self.aPath(aPath_index))
            #         file_list = self.file_list[aPath_index]
            #         for afile_index in range(len(file_list)):
            #             df_dict = {}
            #             with open(file_list[afile_index]) as Sample:
            #                 for line in Sample:
            #                     value_list = line.split('\t')
            #                     df_list = list(itemgetter(*self.col_index[afile_index])(value_list))
            #                     if readtoken == 0:
            #                         col = df_list
            #                         df_dict = df_dict.fromkeys(col)
            #                         for i in range(len(col)):
            #                             df_dict[col[i]] = []
            #                         readend = self.count
                                
            #                     for i in range(len(col)):
            #                         df_dict[col[i]].append(df_list[i])
                                
            #     for i in range(Slicer):
            #         if slicer != Slicer:
            #             looptoken = (slicer+1) * self.count
            #             # df_final = pd.DataFrame(columns = self.col_comb)
            #             for aPath_index in range(len(self.aPath)):
            #                 os.chdir(self.aPath[aPath_index])
            #                 file_list = self.file_list[aPath_index]
            #                 for afile_index in range(len(file_list)):
            #                     df_dict = {}
            #                     readtoken = 0
            #                     with open(file_list[afile_index]) as Sample:
            #                         for line in Sample:
            #                             value_list = line.split('\t')
            #                             df_list = list(itemgetter(*self.col_index[afile_index])(value_list))
            #                             if readtoken == 0 and looptoken == self.count:
            #                                 col = df_list
            #                                 df_dict = df_dict.fromkeys(col)
            #                                 for i in range(len(col)):
            #                                     df_dict[col[i]] = []
            #                                 readend = self.count
                                        
            #                             for i in range(len(col)):
            #                                 df_dict[self.col_dict[self.file_list[aPath_index][afile_index]][i]].append(df_list[i])
            #                                 # print(df_dict)
            #                             readtoken = readtoken + 1
            #                             if readtoken == readend:
            #                                 df = pd.DataFrame.from_dict(df_dict)
            #                                 df = df.reset_index(drop = True)
            #                                 writer = ExcelWriter(SaveFileName)
            #                                 df.to_excel(writer,sheet_list[i],index = False)
            #                                 writer.save()
                                            # writer.close()





    def SaveDataFrame(self,path,filename,col_index,slicer,count):
        os.chdir(path)
        df_dict = {}
        readtoken = 0
        looptoken = (slicer +1) * count
        with open(filename) as Sample:
            for line in Sample:
                value_list = line.split('\t')
                df_list = list(itemgetter(*col_index)(value_list))
                if readtoken == 0 and looptoken == count:
                    col = df_list
                    df_dict = df_dict.fromkeys(df_list)
                    for i in range(len(col)):
                        df_dict[col[i]] = []
                    readend = count
                
                for j in range(len(df_list)):
                    df_dict[col[j]].append(df_list[j])
                readtoken = readtoken + 1

                if readtoken == readend:

                




                if readtoekn == 0 and looptoken == count:
                    col = line.split('\t')
                    df_dict = df_dict.fromkeys(col)
                    readtoken = readtoken  + 1
                    readend = count
                
                value_list = line.split('\t')
                df_list = list(itemgetter(*col_index)(value_list))

        pass
        # pass

    def SheetName(self,Slicer):
        sheet_list = []
        for i in range(Slicer):
            sheet_list.append('Sheet%d' %int(i+1))
        return sheet_list

    # def ErrorSlicer(self,Slicer,SaveFileName):
    #     sheet_list = self.SheetName(Slicer)
    #     for i in range(Slicer):
    #         if i =! Slicer:
    #             df_final = pd.DataFrame(columns = self.col_comb)
    #             for aPath_index in range(len(self.aPath)):
    #                 os.chdir(self.aPath[aPath_index])
    #                 for afile_index in range(len(self.file_list[aPath_index])):

    #                     df_dict = {}
    #                     looptoken = 0
    #                     with open(self.file_list[aPath_index][afile_index]) as Sample:
    #                 # print(col_dict)
    #                         for line in Sample:
    #                             if looptoken ==0:
    #                                 df_dict = df_dict.fromkeys(self.col_dict[self.file_list[aPath_index][afile_index]])
    #                                 looptoken = looptoken +1 
    #                                 continue
    #                             value_list = line.split('\t')
    #                             df_list = itemgetter(*self.col_index[afile_index])(value_list)
    #                             for i in range(len(self.col_dict[self.file_list[aPath_index][afile_index]])):
    #                                 if df_dict[self.col_dict[self.file_list[aPath_index][afile_index]][i]] == None:
    #                                     df_dict[self.col_dict[self.file_list[aPath_index][afile_index]][i]] = []
    #                                 df_dict[self.col_dict[self.file_list[aPath_index][afile_index]][i]].append(df_list[i])

    #                             looptoken = looptoken + 1
    #                             if looptoken == self.count:
    #                                 break  
    #                         df = pd.DataFrame.from_dict(df_dict)
    #                     df_final = df_final.append(df)
    #             df_final = df_final.reset_index(drop = True)
    #             writer = ExcelWriter(SaveFileName)
    #             df_final.to_excel(writer,sheet_list[i])
    #             writer.save()
    #         else:
                

            
    #     pass
    def ErrorSave(self):
        df_final = pd.DataFrame(columns = self.col_comb)
        df_dict = {}
        for aPath_index in range(len(self.aPath)):
            os.chdir(self.aPath[aPath_index])
            for afile_index in range(len(self.file_list[aPath_index])):

                df_dict = {}
                looptoken = 0
                with open(self.file_list[aPath_index][afile_index]) as Sample:
                    # print(col_dict)
                    for line in Sample:
                        
                        if looptoken ==0:
                            # df = pd.DataFrame(columns = col_dict[file_list[aPath_index][afile_index]])
                            df_dict = df_dict.fromkeys(self.col_dict[self.file_list[aPath_index][afile_index]])
                            looptoken = looptoken +1
                            continue
                        value_list = line.split('\t')
                        df_list = itemgetter(*self.col_index[afile_index])(value_list)
                        for i in range(len(self.col_dict[self.file_list[aPath_index][afile_index]])):
                            if df_dict[self.col_dict[self.file_list[aPath_index][afile_index]][i]] == None:
                                df_dict[self.col_dict[self.file_list[aPath_index][afile_index]][i]] = []
                            df_dict[self.col_dict[self.file_list[aPath_index][afile_index]][i]].append(df_list[i])
    
                    df = pd.DataFrame.from_dict(df_dict)
                df_final = df_final.append(df)
        df_final=df_final.reset_index(drop = True)
        return df_final


        
            




    def DictRefactory(self,file_dict):
        aPath = []
        file_name = []
        file_list = []
        col_dict = {}
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
                col_dict[afile] = item
                col_index.append(item_index)
            file_list.append(aPath_item)
        col_comb = list(set(col_comb))
        
        for i in range(len(aPath)):
            os.chdir(aPath[i])
            for afile_i in range(len(file_list[i])):
                aPath_total = 0
                with open(file_list[i][afile_i]) as f:
                    afile_total = sum(1 for _ in f) -1
                    aPath_total = afile_total + aPath_total
                total = total + aPath_total
        
        return aPath,file_name,col_dict,col_comb,file_list,col_index,total
    def GetSampleData(self,aPath,file_name,file_list,col_dict,col_index,col_comb):
        # self.Sample_dict = pd.DataFrame(columns = )
        df_final = pd.DataFrame(columns = col_comb)
        df_dict = {}
        # df_dict = df_dict.fromkeys(col_comb)
        NumOfRows = int(100/len(file_name))
        for aPath_index in range(len(aPath)):
            os.chdir(aPath[aPath_index])
            # print(aPath[aPath_index])
            for afile_index in range(len(file_list[aPath_index])):
                # print(file_list[aPath_index][afile_index])
                df_dict = {}
                looptoken = 0
                with open(file_list[aPath_index][afile_index]) as Sample:
                    # print(col_dict)
                    for line in Sample:
                        
                        if looptoken ==0:
                            # df = pd.DataFrame(columns = col_dict[file_list[aPath_index][afile_index]])
                            df_dict = df_dict.fromkeys(col_dict[file_list[aPath_index][afile_index]])

                            looptoken = looptoken +1
                            continue
                        value_list = line.split('\t')
                        df_list = itemgetter(*col_index[afile_index])(value_list)
                        for i in range(len(col_dict[file_list[aPath_index][afile_index]])):
                            if df_dict[col_dict[file_list[aPath_index][afile_index]][i]] == None:
                                df_dict[col_dict[file_list[aPath_index][afile_index]][i]] = []
                            df_dict[col_dict[file_list[aPath_index][afile_index]][i]].append(df_list[i])
    
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