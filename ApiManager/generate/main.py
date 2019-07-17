import os
import json
import time
import datetime
import requests
from ApiManager.generate.generator import event_generate, status_generate, get_imagedata
from ApiManager.generate.prepare import disable_rule, create_rule, create_point, create_device


def event_prepare():
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
    return {"device": devices, "mapping": ID_MAPPING}


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

    # data = event_prepare()
    # ID_MAPPING = data['mapping']
    # devices = data['device']
    # print("***************XXXXXXXXXXX****************")
    # print(ID_MAPPING)
    # print(devices)
    # event_generate(devices, env_fe, env_gateway, ID_MAPPING, 'open')
    # TODO 造在线率

    # print(get_imagedata(False))
    # print(type(get_imagedata(False)))
    # d = ['ParkingLotSystem', 'CameraPeopleCountingSystem', 'StuffGeolocating', 'VehicleGeolocating']
    status_generate(['StuffGeolocating'], env_fe, env_gateway, num=10)

    # 元数据
    # https://10.101.12.4:19916/ciimc-fe-api/meta/subscribe-change?message_class=generic-property&token=e1550202429f43c7bf71043868712642

    # url = env_fe['url'] + '/ciimc-fe-api/meta/subscribe-change'
    # filters = {
    #     "generic-property": {
    #         "name": "PRESSURE"
    #     }
    # }
    # params = {
    #     "token": env_fe['token'],
    #     "message_class": 'generic-property',
    #     "filters": json.dumps(filters)
    # }
    # with requests.get(url=url, params=params, stream=True, verify=False) as response:
    #     data = []
    #     for chunk in response.iter_lines(chunk_size=1):
    #         chunk = chunk.decode('utf-8')
    #         if chunk:
    #             if chunk == 'change':
    #                 break
    #             else:
    #                 meta = json.loads(chunk)
    #                 print(meta)
    #                 data.append(meta['record'])

    # 删路由规则

    # for i in range(99, 113):
    #     url = "http://10.101.12.4:17999/united-ciimc-api/v1/routing-rule/remove"
    #
    #     querystring = {"id": i}
    #
    #     headers = {
    #         'cache-control': "no-cache",
    #         'Postman-Token': "52065aca-0a62-480d-b4c8-2be4683fcef6"
    #     }
    #
    #     response = requests.request("GET", url, headers=headers, params=querystring)
    #
    #     print(response.text)
