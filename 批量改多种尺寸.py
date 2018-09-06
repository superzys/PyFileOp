# 提取目录下所有图片,更改尺寸后保存到另一目录
from PIL import Image
import os.path
import glob
import sys


def convertjpg(jpgfile, outdir, width=96, height=96):
    img = Image.open(jpgfile)
    try:
        # +"_"+str(width)
        basename = os.path.basename(jpgfile)
        filename = os.path.splitext(basename)[0]
        filetype = os.path.splitext(basename)[1]  # 文件扩展名
        new_img = img.resize((width, height), Image.BILINEAR)
        new_img.save(os.path.join(outdir, filename+"_"+str(width)+filetype))
        # new_img.save(os.path.join(outdir, os.path.basename(jpgfile)))
    except Exception as e:
        print(e)


for jpgfile in glob.glob(sys.path[0]+"/*.png"):
    convertjpg(jpgfile, sys.path[0]+"\\done",320,180)
    # convertjpg(jpgfile, sys.path[0]+"\\done",144,144)
    # convertjpg(jpgfile, sys.path[0]+"\\done",96,96)
    # convertjpg(jpgfile, sys.path[0]+"\\done",72,72)
    # convertjpg(jpgfile, sys.path[0]+"\\done",48,48)
    # convertjpg(jpgfile, sys.path[0]+"\\done",36,36)
