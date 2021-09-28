# -*- coding: utf-8 -*-
from config import importConfig
import pyshark
import subprocess
from logging import getLogger, config
import json

logger = getLogger(__name__)


def main():
    """設定を読み込み、パケットキャプチャを開始"""
    with open("./log_config.json", "r") as f:
        log_conf = json.load(f)

    # log config
    config.dictConfig(log_conf)

    conf = importConfig()
    if not conf:
        print("invalid config.json.")
        return

    interface = conf[0]
    arc_path = conf[1]
    devices = conf[2]

    device_dic = {}
    for d in devices:
        if not d["message"]["notify"]:
            continue
        device_dic[d["mac_addr"]] = d

    logger.info("start packet capture")
    while True:

        def take_packet_callback(packet):
            logger.debug("capture")
            logger.debug(packet)
            if packet.arp.src_hw_mac in device_dic:
                logger.debug("filterd")
                logger.debug(packet)
                device = device_dic[packet.arp.src_hw_mac]
                cmd = f'{arc_path} -d "{device["message"]["echo_dot_name"]}" -e "{device["message"]["message"]}" '
                logger.info(f"cmd: {cmd}")
                proc = subprocess.Popen(cmd)
                result = proc.communicate()
                logger.info(result)

        # arp.opcode==1&&arp.src.proto_ipv4==0.0.0.0
        capture = pyshark.LiveCapture(interface=interface, display_filter="arp.opcode==1")
        capture.apply_on_packets(take_packet_callback)  # キャプチャを実行


if __name__ == "__main__":
    main()
