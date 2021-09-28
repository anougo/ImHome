# ImHome
## 概要
デバイスからWifiへの接続を検出し、Alexaを喋らせる  
キッズケータイ(SH-03M)は、Wifiを検出するが接続しないため通知されないかも

## Alexa
[alexa-remote-control](https://github.com/thorsten-gehrig/alexa-remote-control)を使用する

## Install
1. sudo apt-get intall tshark
1. sudo chmod +x /usr/bin/dumpcap
1. sudo apt-get intall pyshark
1. git clone https://github.com/anougo/ImHome.git
1. pip install -r requiremtns.txt
1. git clone https://github.com/thorsten-gehrig/alexa-remote-control.git
1. `alexa-remote-control` setting
1. imhome setting

## 設定
`src/config.json`を設定する
- `interface`  
  パケットを監視するインターフェースの名前  
  `eth0`など
- `arc_path`  
  `alexa-remote-control.sh`のパス
- `device_list`
  - `mac_addr`  
    監視するデバイスのmacアドレス
  - `name`  
    デバイスの名前(特に使用していない)
  - `message`
    - `notify`  
      `true` or `false`  
      `true`の場合通知対象となる
    - `message`  
      alexaの喋る内容
    - `echo_dot_name`  
      喋るEchoデバイスの名前

