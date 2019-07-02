import os
import json
import time
from ApiManager.generate.generator import status_generate
from ApiManager.generate.prepare import disable_rule, create_rule, create_point, create_device

if __name__ == '__main__':
    # select fe api env
    env_fe = {"url": "https://10.101.12.4:17998", "token": "063f2acb8048a8af15074f0387aeda1b"}
    # select gate way env
    env_gateway = {"url": "http://10.101.12.4:10099"}
    env_screen = {"url": "http://10.101.12.4:17999"}
    env = {
        "fe": env_fe,
        "gateway": env_gateway,
        "screen": env_screen
    }

    here = os.path.abspath(os.path.dirname(__file__))
    file = here + '\\init_data.json'
    with open(file, encoding='utf-8') as data:
        source = data.read()
    data = json.loads(source)
    # disable_rule(screen_env=env_screen, data=data)
    ID_MAPPING = {}
    devices = set()
    for t in data['rules']:
        rule = t['rule_json']
        point = t['point']
        device = t['device']
        open_data = t['open_data']
        close_data = t['close_data']

        try:
            ID_MAPPING[device['deviceType']]
        except KeyError:
            ID_MAPPING[device['deviceType']] = {
                "close": close_data,
                "id_channel": [],
                "open": open_data
            }

        ID_MAPPING[device['deviceType']]['id_channel'].append(
            {
                "id": device['deviceID'],
                "channel": device['channel']
            }
        )
        devices.add(device['deviceType'])

        create_rule(env_screen, rule)
        point_name = create_point(env_fe, point)
        time.sleep(5)
        create_device(env_fe, device, point_name)

    # disable_rule(env_screen)

    print("***************XXXXXXXXXXX****************")
    print(ID_MAPPING)
    print(devices)
    status_generate(devices, env_fe, env_gateway, ID_MAPPING, 'close')
    # TODO 造在线率 造人员车辆
