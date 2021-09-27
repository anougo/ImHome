# -*- coding: utf-8 -*-
from typing import Tuple
from config import importConfig
import pyshark


def main():
    """設定を読み込み、パケットキャプチャを開始"""
    config = importConfig()
    if not config:
        print("invalid config.json.")
        return

    interface = config[0]
    # detect_rule = config[1]
    devices = config[2]

    device_dic = {}
    for d in devices:
        device_dic[d["mac_addr"]] = d["name"]

    print("start packet capture")
    while True:

        def take_packet_callback(packet):
            if packet.arp.src_hw_mac in device_dic:
                print("============= Received ================")
                print(packet)
                # TODO 複数回同一同じ内容が送信されているので対応の検討が必要
                # TODO 通知先の呼び出し
            # print(packet.arp.field_names) # フィールドの一覧を取得

        capture = pyshark.LiveCapture(interface=interface, display_filter="arp.opcode==1&&arp.src.proto_ipv4==0.0.0.0")
        capture.apply_on_packets(take_packet_callback)  # キャプチャを実行


if __name__ == "__main__":
    main()
