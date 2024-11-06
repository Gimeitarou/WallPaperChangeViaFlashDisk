ショートカットファイルだけが置かれたUSBディスク。<br>
そのショートカットファイルを動かすと任意の画像がpcの壁紙にセットされる。<br>
そんなUSBディスクを作ることができるpythonコードです。<br>
<br>
コードの使い方<br>
1．空のUSBディスクをwindowsPCにセット、D: が割り当てられていることを確認する<br>
2．main.pyとresourcesファイルをDディレクトリ（D:）に移動させる<br>
3．main.pyを 'python d:/main.py' で走らせる<br>
4．main.pyとresourcesファイルを削除、もしくは別の場所に移動させておく<br>
5．RenameMe.lnk(ショートカットファイル)のみが置かれたUSBディスクが完成<br>
<br>
USBディスクを元に戻す流れ<br>
1．USBディスクをセット、d: を確認<br>
2．after-use.pyをDディレクトリ（D:）に移動、'python d:/after-use.py' で走らせる<br>
3．隠されていた諸々のファイルがunvailされるので、それらを削除、after-use.pyも削除<br>
4．完了<br>
<br>
備考<br>
resources内のChangeWP.exeのソースコードは<br>
[import ctypes<br>
<br>
f = open('D:\\pic_name.txt', 'r', encoding='UTF-8')<br>
basename = f.read() #read the note text of the file name of the pic<br>
f.close()<br>
<br>
ctypes.windll.user32.SystemParametersInfoW(20, 0, f"D:\\{basename}" , 0) #set the pic desktop]<br>
で、nuitkaにより実行ファイルにしたものです。<br>
