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

#滑动次数统计
n = 0
def swip(position_hc,position_jz):
    '''
    滑动屏幕函数
    
    '''
    global n
    T = 4
    
    while T>0:
        #坐标移动
        k = 0
        for j in range(3):
            subprocess.Popen(
                    'adb shell input swipe {} {} {} {}'.format(
                                                                position_hc[0],position_hc[1],
                                                                position_jz[0],position_jz[1]-k),
                                                                shell=True)
            n+=1   
            print(f'----------------->滑动{n}次.',end='\r')
            #滑动速度调节越小越快，调得太快手机卡死别怪我
            time.sleep(0.3)
            k+=300
        T-=1
        
    
if __name__ == "__main__":
    
    while True:
        for h in range(3):
            for e in range(3):
                swip(hc_position[h],jz_position[e])
                #time.sleep(0.5)
        print('_____已完成一次108次的循环_________')
        n = 0
        
                








