import ctypes

f = open('D:\pic_name.txt', 'r', encoding='UTF-8')
basename = f.read() #read the note text of the file name of the pic
f.close()

ctypes.windll.user32.SystemParametersInfoW(20, 0, f"D:\{basename}" , 0) #set the pic desktop

#Copyright (c) 2024 Gimeitarou
#This software is released under the MIT License, see LICENSE.