# coding:utf8
import os
import sys
import shutil

i = 0

# def DealFileInDir(dir):
#      filelist = os.walk(dir)


def DealOneDir(dir):

    filelist = os.listdir(dir)


    for file in filelist:
        if file.count('.png') > 0:  
            filename = os.path.splitext(file)[0]
            newdir = os.path.join(dir, filename)
            isExists=os.path.exists(newdir)        
            if not isExists:
                os.makedirs(newdir)
            oldName = os.path.join(dir, file)
            newName = os.path.join(newdir, file)
            shutil.copyfile(oldName,newName)
# rename()
DealOneDir(sys.path[0])
