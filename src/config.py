import json


def importConfig():
    """設定ファイルの読み込み

    Returns:
        tuple:
            str: interface,
            list: detection rule
            list: device list
    """

    with open("config.json", "r") as f:
        config = json.load(f)

    interface = config["interface"]
    if not interface:
        return False

    detectRule = config["detection_rule"]
    if not detectRule:
        return False

    devices = config["device_list"]

    # TODO データの検証

    return (interface, detectRule, devices)
