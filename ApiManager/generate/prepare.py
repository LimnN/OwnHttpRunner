import base64
import json
import random
import time

import requests


def get_metadata(env, message_class):
    """
    :param env: env is a dict include url and ssl token
    :param message_class
    :return: is a list like this: [{'channel': 'channel1', 'key': 'aaaaa', 'uuid': 'bbbbb',
    'deviceTypes': ['' , '', '']},{}]
    """
    url = env['url'] + '/ciimc-fe-api/meta/subscribe-change'
    # filter = None
    params = {"token": env['token'], "message_class": message_class}
    with requests.get(url=url, params=params, stream=True, verify=False) as response:
        meta = []
        for chunk in response.iter_lines(chunk_size=1):
            chunk = chunk.decode('utf-8')
            if chunk:
                if chunk == 'change':
                    break
                else:
                    data = json.loads(chunk)
                    if message_class == 'api-key':
                        channel = data['record']['channel']
                        key = data['record']['key']
                        uuid = data['record']['uuid']
                        devicetypes = data['record']['deviceTypes']
                        meta.append({"channel": channel, "key": key, "uuid": uuid, "deviceTypes": devicetypes})
    return meta


def get_token(env, channel, fe_env):
    url = env['url'] + '/v2/auth'
    channels = get_metadata(env=fe_env, message_class='api-key')
    key = None
    for chan in channels:
        if channel == chan['channel']:
            key = chan['key']
            break
    params = {"key": key}
    with requests.get(url=url, params=params, verify=False) as response:
        token = response.json()['token']
    return token


def set_body(device_type, device_id, isopen=None):
    data = set_data(device_type, isopen)
    return {
        "deviceType": device_type,
        "deviceID": device_id,
        "timestamp": int(time.time()) - 120,
        "data": data
    }


def set_data(device_type, isopen=None):
    """

    :param device_type:
    :param isopen:
    :return: a json dict
    """
    return {
            'SmokeDetectionSensor': lambda switch: {"smoke": random.randrange(101, 300, 1)}
            if switch else {"smoke": random.randrange(0, 20, 1)},
            'WaterPressureSensor': lambda switch: {"pressure": round(random.uniform(0.11, 1), 2)}
            if switch else {"pressure": round(random.uniform(0, 0.09), 2)},
            "VehicleGeolocating": lambda switch: {
                "work_status": False,
                "carNum": "\u6caaD67581",
                "temperature": random.randrange(12, 40, 1),
                "longitude": 121.4557008,
                "course": 7,
                "mile": 2607,
                "latitude": 31.231937,
                "speed": random.randrange(20, 60, 2)
            },
            "StuffGeolocating": lambda switch: {
                "latitude": 31.2310654404,
                "work_status": True,
                "working_hours": random.randrange(1, 10, 2),
                "name": "\u5434\u96ef\u7ee2",
                "longitude": 121.4537033905
            },
            "ParkingLotSystem": lambda switch: {
                "num_park_free": random.randrange(0, 200, 1),
                "num_guest_park_free": random.randrange(0, 200, 1),
                "num_monthly_park_free": random.randrange(0, 200, 1)
            },
            "CameraPeopleCountingSystem": lambda switch: {
                "num_stay": random.randrange(0, 5000, 1),
                "num_enter": random.randrange(0, 5000, 1),
                "num_leave": random.randrange(0, 5000, 1)
            }
        }[device_type](isopen)


def get_imagedata(isarray):
    """
    :param isarray: is a list? True or False
    :return:
    """
    if isarray:
        with open('../../ExampleFile/a.png', 'rb') as f:
            image_base64 = base64.b64encode(f.read())
        with open('../../ExampleFile/b.png', 'rb') as f:
            image2_base64 = base64.b64encode(f.read())
        image_data = [
            {
                "blob": image_base64,
                "contentType": "image/png"
            },
            {
                "blob": image2_base64,
                "contentType": "image/png"
            }
        ]
    else:
        with open('../../ExampleFile/a.png', 'rb') as f:
            image_base64 = base64.b64encode(f.read())
        image_data = {
            "blob": image_base64,
            "contentType": "image/png"
        }
    return image_data


def send_status(env, token, body):
    # need url\channel token\body
    url = env['url'] + '/v2/device/event'

    querystring = {"token": token}
    body = body
    payload = json.dumps(body)
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache"
    }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring, verify=False)
    print(payload)
    print(response.text)
