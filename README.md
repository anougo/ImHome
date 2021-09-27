# ImHome
Detect and notify the connection of a specific device to Wifi.

## TODO
- echo dotへの通知  
  [`alexa-remote-control`](https://github.com/thorsten-gehrig/alexa-remote-control)を使う予定
- rasberry piでの動作確認  
  8月以降予定

## Windows上での動作環境
[`alexa-remote-control`](https://github.com/thorsten-gehrig/alexa-remote-control)は、WSL等で動かす必要がある
1. Wiresharkのインストール
1. IFの名前取得  
  Wiresharkのインストールディレクトリ`C:\Program Files\Wireshark`へ移動
  下記のコマンドを実行する
    ```cmd
    rem 文字化けするので文字コードを変更
    chcp 65001
    dumpcap -D
    ```
    キャプチャ対象のIFの名前`\Device\NPF_{xxxxx}`を控えておく  
    [参考にしたURL](https://one.angato.org/studyenv/wireshark/)


## Install
1. sudo apt-get intall tshark
1. sudo chmod +x /usr/bin/dumpcap
1. sudo apt-get intall pyshark
1. git clone
1. pip install -r requiremtns.txt
1. git clone `alexa-remote-control`
1. `alexa-remote-control` setting
1. imhome setting
