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
                filetype = os.path.splitext(file)[1]  # 文件扩展名
                if filename.count('_') > 0:
                    print(Olddir)
                    nameArr = filename.split('_')
                    # print(nameArr[0])
                    # print(nameArr[1])
                    curJsonFile = open(Olddir,'r+',encoding='utf-8')
                    jsonStr = curJsonFile.read()
                    #把文件指针移动回去
                    curJsonFile.seek(0, os.SEEK_SET)
                    curJsonFile.truncate()
                    jsonStr = jsonStr.encode('utf-8').decode('utf-8-sig')
                    # print(jsonStr)
                    # json_str = json.dumps(jsonStr,ensure_ascii=False)
                    data = json.loads(jsonStr)
                    # print(json_str)
                    # print(type(json_str))
                    # print(data)
                    # print(type(data))
                    data['_id'] = nameArr[0]
                    data['Name'] = nameArr[1]
                    # for dt in data:                      
                    #     print( dt) 
                    # idStr = '"_id": "%s"' % (nameArr[0])
                    # nameStr = '"Name": "%s"' % (nameArr[1])
                    # print(idStr)
                    # newJsonStr = jsonStr.replace('"_id": "1"',idStr)
                    # newJsonStr = jsonStr.replace('"Name": "名字"',nameStr)
                    newJsonStr = json.dumps(data,ensure_ascii=False)
                    curJsonFile.write(newJsonStr)
                    # print(newJsonStr)
                    curJsonFile.close()


        # for root in roots:  # 得到一个路径
            # print(root)
            # DealOneDir(root)


# rename()
DealOneDir(sys.path[0])
