# coding:utf8
import os
import sys

i = 0

# def DealFileInDir(dir):
#      filelist = os.walk(dir)
def DealOneDir(dir):
   
    global i
    filelist = os.walk(dir)
    for roots, dirs, files in filelist:  # 遍历所有文件
        print('start one ------------' + roots)
        # print(roots)
        # print(dirs)
        # print(files)
        # if roots != dir:
        #     print(roots)
        #     DealOneDir(roots)
        # else:
        #     DealFileInDir(roots)
        for file in files:
            if file.count('.json') > 0:
                i = i+1
                Olddir = os.path.join(roots, file)  # 原来的文件路径
                # print(Olddir)
                if os.path.isdir(Olddir):  # 如果是文件夹则跳过
                    continue
                # filename = os.path.splitext(file)[0]  # 文件名
                # filetype = os.path.splitext(file)[1]  # 文件扩展名
                # print(filename)
                # print(filetype)
                idxStr = '0000'+str(i)
                filename = 'weapon_'+idxStr[-4:]
                Newdir = os.path.join(roots, filename)  # 新的文件路径
                print(Newdir)
                os.rename(Olddir, Newdir)  # 重命名
        # for root in roots:  # 得到一个路径
            # print(root)
            # DealOneDir(root)


# rename()
DealOneDir(sys.path[0])

	# protoReuestName = handlerName.replace('_RPC','')

