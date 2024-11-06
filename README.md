ショートカットファイルだけが置かれたUSBディスク。<br>
そのショートカットファイルを動かすと任意の画像がpcの壁紙にセットされる。<br>
そんなUSBディスクを作ることができるpythonコードです。<br>
<br>
必要な事前準備<br>
1．最新リリースからWallPaperChangeViaFlashDisk.zipをダウンロード<br>
2．コマンドプロンプトからpythonが使えるようにすること<br>
<br>
コードの使い方<br>
1．空のUSBディスクをwindowsPCにセット、D: が割り当てられていることを確認する<br>
2．WallPaperChangeViaFlashDisk.zipを開いて、main.pyとresourcesファイルをDディレクトリ（D:）にコピーする<br>
3．main.pyを'python d:/main.py' で走らせる<br>
4．main.pyとresourcesファイルを削除、もしくは別の場所に移動させておく<br>
5．RenameMe.lnk(ショートカットファイル)のみが置かれたUSBディスクが完成<br>
6．RenameMe.lnkの名前やアイコンを好きなものに変更<br>
<br>
USBディスクを元に戻す流れ<br>
1．after-use.pyをダウンロード<br>
2．USBディスクをセット、d: を確認<br>
2．after-use.pyをDディレクトリ（D:）に移動、'python d:/after-use.py' で走らせる<br>
3．隠されていた諸々のファイルがunvailされるので、それらを削除、after-use.pyも削除<br>
4．完了<br>
<br>
備考<br>
resources内のChangeWP.exeは、ChangeWPをnuitkaにより実行ファイルにしたものです。<br>
