#coding:utf-8
#家国梦刷金币助手
#没有火车货物请使用这个脚本
#2019年10月1日 by ataft7
import time
import subprocess
i = 0

sleep_time = 0.5
while 1:
 
  process = subprocess.Popen('adb shell input  swipe 300 970 800 725',shell=True)
  time.sleep(sleep_time)
  process = subprocess.Popen('adb shell input  swipe 300 1230 800 980',shell=True)
  time.sleep(sleep_time)
  process = subprocess.Popen('adb shell input  swipe 300 1480 800 1230',shell=True)
 
  
  i+=1
  s=' ____________________________滑动完成{}次！'
  print(s.format(i),end='\r')
  time.sleep(2)
