import json


def importConfig():
    """設定ファイルの読み込み

    Returns:
        tuple:
            str: interface,
            str: alexa_remote_control.sh path
            list: device list
    """

    with open("config.json", "r", encoding="utf-8") as f:
        config = json.load(f)

    interface = config["interface"]
    if not interface:
        return False

    arc_path = config["arc_path"]

    devices = config["device_list"]

    return (interface, arc_path, devices)
