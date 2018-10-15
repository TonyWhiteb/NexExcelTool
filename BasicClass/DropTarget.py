import wx
import os,sys

class DropTarget(wx.FileDropTarget):
    def __init__(self,targetControl):
        self.targetControl = targetControl

        wx.FileDropTarget.__init__(self)

    def OnDropFiles(self, xOrd, yOrd, pathList):
  
        for aPath in pathList :
            pathname, aBasename = os.path.split(aPath)
            namelist = aBasename.split('.')
            filetype = namelist[len(namelist)-1]
            os.chdir(pathname)
            if filetype == 'errors':

                col_info = []
                with open(aBasename) as afile:
                    for line in afile:
                        col_info= {}
                        afile_list = line.split('\t') 
                        col_info = col_info.fromkeys(afile_list)
                        break


        filenameDropDict = {}
        filenameDropDict['coord'] = (xOrd,yOrd)
        filenameDropDict['pathList'] = pathList
        filenameDropDict['pathname'] = pathname
        filenameDropDict['basenameList'] = aBasename
        filenameDropDict['filetype'] = filetype
        filenameDropDict['col_info'] = col_info

        if (hasattr( self.targetControl, 'dropFunc' ))  and  \
           (self.targetControl.dropFunc != None) :

            # Call the callback function with the processed drop data.
            self.targetControl.dropFunc( filenameDropDict )
        
       # HIGHL: 
        # How to add a function dynamically
