[Codes for windows]<br>
[There is also a version that runs on E-directry for those who want to make sure it works on Windows in a virtual environment].<br>
<br>
A USB disk with only a shortcut file on it.<br>
When you run the shortcut file, the image you have chosen will be set as the wallpaper of your PC.<br>
This python code enable you to create such a USB disk.<br>
<br>
Preparations required<br>
1. Prepare an image file of your choice.<br>
2. Download WallPaperChangeViaFlashDisk.zip from the latest release.<br>
3. Please make sure that you can use python from the command prompt.<br>
<br>
How to use the code<br>
1. Put a blank USB disk into your windows PC and make sure D: is assigned.<br>
2. Open WallPaperChangeViaFlashDisk.zip and copy [main.py and resources folder] to D directory (D:)<br>
3. Run main.py as 'python d:/main.py<br>
4. Delete [main.py and resources folder] 
(or move them to other location).<br>
5. USB disk with only RenameMe.lnk (shortcut file) is now here!<br>
<br>
How to return the USB disk to the original state<br>
1. Download after-use.py<br>
2. Insert the USB disk and check if it is on d:<br>
2. Move after-use.py to the D directory (D:) and run 'python d:/after-use.py<br>
3. Delete the unvailed files and after-use.py, too.<br>
4. That's all.<br>
<br>
Remarks<br>
ChangeWP.exe in resources is EXE file of ChangeWP.py built by nuitka.<br>

# License
The source code is licensed MIT.<br>
<br>
以下、日本語版<br>
<br>
<windows向けコードです><br>
<仮想環境にあるWindowsで動作を確認したい方向けにEdirで動くようにしたバージョンもあります><br>
<br>
ショートカットファイルだけが置かれたUSBディスク。<br>
そのショートカットファイルを動かすと任意の画像がpcの壁紙にセットされる。<br>
そんなUSBディスクを作ることができるpythonコードです。<br>
<br>
必要な事前準備<br>
1．お好みの画像ファイルを用意してください<br>
2．最新リリースからWallPaperChangeViaFlashDisk.zipをダウンロードしてください<br>
3．コマンドプロンプトからpythonが使えるようにしてください<br>
<br>
コードの使い方<br>
1．空のUSBディスクをwindowsPCにセット、D: が割り当てられていることを確認する<br>
2．WallPaperChangeViaFlashDisk.zipを開いて、main.pyとresourcesファイルをDディレクトリ（D:）にコピーする<br>
3．main.pyを'python d:/main.py' で走らせる<br>
4．main.pyとresourcesファイルを削除、もしくは別の場所に移動させておく<br>
5．RenameMe.lnk(ショートカットファイル)のみが置かれたUSBディスクが完成<br>
<br>
USBディスクを元に戻す流れ<br>
1．after-use.pyをダウンロード<br>
2．USBディスクをセット、d: を確認<br>
2．after-use.pyをDディレクトリ（D:）に移動、'python d:/after-use.py' で走らせる<br>
3．隠されていた諸々のファイルがunvailされるので、それらを削除、after-use.pyも削除<br>
4．完了<br>
<br>
備考<br>
resources内のChangeWP.exeは、ChangeWPをnuitkaにより実行ファイルにしたものです<br>
動作デモ:<br>
https://x.com/300kyen/status/1854147116656177185

# License
The source code is licensed MIT.