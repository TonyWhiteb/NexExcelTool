import wx
import os,sys

class DropTarget(wx.FileDropTarget):
    def __init__(self,targetControl):
        self.targetControl = targetControl

        wx.FileDropTarget.__init__(self)

    # def FilenameDropDict(self):

    #     filenameDropDict = {}

    #     filenameDropDict['coord'] = (-1,-1)
    #     filenameDropDict['pathname'] = ''
    #     filenameDropDict['basenameList'] = []
    #     filenameDropDict['pathlist'] = []
    #     filenameDropDict['filetype'] = []
    #     filenameDropDict['NoCol'] = []

    #     return filenameDropDict

    def OnDropFiles(self, xOrd, yOrd, pathList):

        pathname, _ignored = os.path.split(pathList[0])

        basenameList = []
        filetype = []
        col_info = {}
        for aPath in pathList :
            _ignoredDir, aBasename = os.path.split(aPath)
            basenameList.append(aBasename)
            namelist = aBasename.split('.')
            filetype.append(namelist[len(namelist)-1])
            # print(aBasename[point:])
            # print(aPath)
            # print(_ignoredDir)
            # os.chdir(_ignoredDir)
            if filetype == 'errors':

                # col_info = []
                with open(aBasename) as afile:
                    for line in afile:
                        sp = {}
                        afile_list = line.split('\t')
                        sp = sp.fromkeys(afile_list)
                        break
                col_info.append(sp)



        filenameDropDict = {}
        filenameDropDict['coord'] = (xOrd,yOrd)
        filenameDropDict['pathList'] = pathList
        filenameDropDict['pathname'] = pathname
        filenameDropDict['basenameList'] = basenameList
        filenameDropDict['filetype'] = filetype
        filenameDropDict['col_info'] = col_info
        # # print(filenameDropDict)

        if (hasattr( self.targetControl, 'dropFunc' ))  and  \
           (self.targetControl.dropFunc != None) :

            # Call the callback function with the processed drop data.
            self.targetControl.dropFunc( filenameDropDict )
        
       # HIGHL: 
        # How to add a function dynamically
