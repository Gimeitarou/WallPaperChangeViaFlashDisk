import subprocess

f = open('D:\\pic_name.txt', 'r', encoding='UTF-8')
basename = f.read() #read the note text of the file name of the pic
f.close()

subprocess.run('attrib -r -h d:\\ChangeWP.exe' #unvail ChangeWP.exe
                +f'&& attrib -r -h d:\\{basename}' #unvail the pic
                +'&& attrib -r -h d:\\pic_name.txt', shell=True) #unvail note of file name of the pic

#Copyright (c) 2024 Gimeitarou
#This software is released under the MIT License, see LICENSE.