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
コードはWindowsでの動作を想定したものです<br>
>resources内のChangeWP.exeは、ChangeWPをnuitkaにより実行ファイルにしたもの<br>
動作デモ
https://x.com/300kyen/status/1854147116656177185
