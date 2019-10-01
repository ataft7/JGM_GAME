# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 11:37:26 2019

@author: Ataft7

程序功能：《家国梦》自动刷金币脚本
"""

import time
import subprocess

#以下坐标请跟进屏幕像素确定

#火车货物坐标
hc_position = [
      [660,1870],
      [820,1790],
      [950,1730]]

#建筑物坐标
jz_position = [
      [300,1420],
      [550,1330],
      [800,1200]]


def swip(index):
    '''
    滑动屏幕函数
    index 货物坐标列表的下标
    '''
    k = 0
    l = 0
    for i in range(3):
#        process = subprocess.Popen(
#                'adb shell input swipe {} {} {} {}'.format(
#                hc_position[index][0],
#                hc_position[index][1],
#                jz_position[index][0],
#                jz_position[index][1]-k),
#                shell=True)
#        process.wait()
        subprocess.Popen(
                    'adb shell input swipe {} {} {} {}'.format(
                    hc_position[index][0],                        
                    hc_position[index][1],
                    jz_position[index][0],
                    jz_position[index][1]-k),
                    shell=True)
    
        #滑动速度调节越小越快，调得太快手机卡死别怪我
        time.sleep(1)
        print(
                hc_position[index][0],
                hc_position[index][1],
                jz_position[index][0],
                jz_position[index][1]-k,
                )
        #坐标减少
        k+=300
        l+=300
        

def main():
    n = 0
    j=5
    while j>0:
        for e in range(3):
            swip(e)
            n+=3
            print(f'{n}times.')
        j-=1
    
        
if __name__ == "__main__":
    while True:
        main()
        time.sleep(10)
    









