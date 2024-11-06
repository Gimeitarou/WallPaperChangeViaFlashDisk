ショートカットファイルだけが置かれたUSBディスク。
そのショートカットファイルを動かすと任意の画像がpcの壁紙にセットされる。
そんなUSBディスクを作ることができるpythonコードです。

コードの使い方
1．空のUSBディスクをwindowsPCにセット、D: が割り当てられていることを確認する
2．main.pyとresourcesファイルをDディレクトリ（D:）に移動させる
3．main.pyを 'python d:/main.py' で走らせる
4．main.pyとresourcesファイルを削除、もしくは別の場所に移動させておく
5．RenameMe.lnk(ショートカットファイル)のみが置かれたUSBディスクが完成

USBディスクを元に戻す流れ
1．USBディスクをセット、d: を確認
2．after-use.pyをDディレクトリ（D:）に移動、'python d:/after-use.py' で走らせる
3．隠されていた諸々のファイルがunvailされるので、それらを削除、after-use.pyも削除
4．完了

備考
resources内のChangeWP.exeのソースコードは
[import ctypes

f = open('D:\\pic_name.txt', 'r', encoding='UTF-8')
basename = f.read() #read the note text of the file name of the pic
f.close()

ctypes.windll.user32.SystemParametersInfoW(20, 0, f"D:\\{basename}" , 0) #set the pic desktop]
で、nuitkaにより実行ファイルにしたものです。
