# coding:utf8
import os
import sys
import json

i = 0

# def DealFileInDir(dir):
#      filelist = os.walk(dir)


def DealOneDir(dir):

    global i
    filelist = os.walk(dir)
    hbStr = '\r'
    ctStr = ''
    for roots, dirs, files in filelist:  # 遍历所有文件
        print('start one ------------' + roots)
        for file in files:
            if file.count('.json') > 0:
                i = i+1
                Olddir = os.path.join(roots, file)  # 原来的文件路径
                # print(Olddir)
                if os.path.isdir(Olddir):  # 如果是文件夹则跳过
                    continue
                filename = os.path.splitext(file)[0]  # 文件名
                # filetype = os.path.splitext(file)[1]  # 文件扩展名
                if filename.count('_') > 0:
                    print(Olddir)
                    nameArr = filename.split('_')
                    
                    curJsonFile = open(Olddir,'r+',encoding='utf-8')
                    jsonStr = curJsonFile.read()
                  
                    jsonStr = jsonStr.encode('utf-8').decode('utf-8-sig')
                    ctStr += jsonStr+'\r'
                    curJsonFile.close()


        # for root in roots:  # 得到一个路径
            # print(root)
            # DealOneDir(root)
    hbStr = hbStr +ctStr+''
    print('--------------------------------------')
    # print(hbStr)
    tarpath = os.path.join(dir, 'zysServer.js')
    wjsFile = open(tarpath,'w+',encoding='utf-8')
    wjsFile.write(hbStr)
    wjsFile.close()

# rename()
DealOneDir(sys.path[0])
