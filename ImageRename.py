import os
import time

def secondsToStr(seconds):
    x = time.localtime(seconds)  # 时间元组
    return time.strftime("%Y-%m-%d", x)  # 时间元组转为字符串


def ImageRename(folder_path):
    list = os.listdir(folder_path)
    i = 0
    os.chdir(folder_path)
    for img in list:
        print(list[i]) #原来的名字
        image_Info = os.stat(list[i]) #获取图片属性信息
        image_time = secondsToStr(image_Info.st_ctime)
        #图片名字格式为:xxxx-xx-xx_xxxx.jpg/png
        print(image_time+'_'+list[i])
        os.rename(list[i],image_time+'_'+list[i])
        i+=1

if __name__ == "__main__":
    folder_path = './photos'
    ImageRename(folder_path)
    