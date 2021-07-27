# coding: utf-8
import os
import configparser
import pyshark

def import_config():
    """設定ファイルの読み込み
    Returns:
        tuple: mac_addres(list), interface(string)
    """
    # 設定ファイルの読み込み
    config_ini = configparser.ConfigParser()
    config_ini.read("config.ini", encoding="utf-8")
    read_default = config_ini["DEFAULT"]

    # mac_addrs
    mac_addrs = read_default.get("mac_addrs")
    if mac_addrs is None:
        print("config.ini: mac_addrs is None.")
        return False

    if "," in mac_addrs:
        mac_addrs = mac_addrs.split(",")
    else:
        mac_addrs = [mac_addrs]
    
    # names
    names = read_default.get("names")
    if names is None:
        print("config.ini: names is None.")
        return False

    if "," in names:
        names = names.split(",")
    else:
        names = [names]

    # interface
    interface = read_default.get("interface")
    if interface is None:
        interface = "eth0"
    
    if os.name == "nt" and interface == "eth0":
        # windows
        print("config.ini: interface is required")
        return False

    # TODO 指定されたNICが存在するかの判定

    return (mac_addrs, names, interface)

def main():
    """初期化と設定の読み込み、パケットキャプチャを開始
    """
    config = import_config()
    if config == False:
        print("invalid config.ini.")
        return
    mac_addrs = config[0]
    names = config[1]
    interface = config[2]

    while True:
        def take_packet_callback(packet):
            if packet.arp.src_hw_mac in mac_addrs:
                print(packet)
                # TODO 複数回同一同じ内容が送信されているので対応の検討が必要
                # TODO 通知先の呼び出し
            #print(packet.arp.field_names) # フィールドの一覧を取得

        capture = pyshark.LiveCapture(interface=interface, display_filter="arp.opcode==1")
        capture.apply_on_packets(take_packet_callback) # キャプチャを実行


if __name__ == '__main__':
    main()