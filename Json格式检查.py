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

                    data = json.loads(jsonStr)
                    data['_id'] = nameArr[0]
                    data['Name'] = nameArr[1]
                   
                    # newJsonStr = json.dumps(data,ensure_ascii=False)
                    # curJsonFile.write(newJsonStr)
                    # print(newJsonStr)
                    curJsonFile.close()


        # for root in roots:  # 得到一个路径
            # print(root)
            # DealOneDir(root)


# rename()
DealOneDir(sys.path[0])
