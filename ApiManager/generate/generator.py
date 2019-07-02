import base64
import json
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
    print(response.json())
    return response.json()


def area_lua_generate():
    # for area lua event
    # RegionalPedestrianFlow
    pass


def status_generate(devices, fe_env, gateway_env, id_mapping, isopen='close'):
    # for status data generate
    # StuffGeolocating VehicleGeolocating ParkingLotSystem CameraPeopleCountingSystem
    success = 0
    fail = 0
    detail = []
    for device in devices:
        # send a status need
        # 1. deviceType
        # 2. deviceID
        # 3. timestamp
        # 4. data{}
        # 5. token : get token need a channel
        device_type = device

        ids = id_mapping[device_type]['id_channel']
        if len(ids) == 0:
            fail += 1
            detail.append({device_type: 'data not set yet'})
        else:
            try:
                for id_channel in ids:
                    device_id = id_channel['id']
                    data = id_mapping[device_type][isopen]
                    body = {
                        "deviceType": device_type,
                        "deviceID": device_id,
                        "timestamp": int(time.time()) - 120,
                        "data": data
                    }

                    # device_channel = id_mapping[device_type]['id_channel'][0]['channel']
                    device_channel = id_channel['channel']
                    token = get_token(gateway_env, device_channel, fe_env)

                    result = send_status(gateway_env, token, body)
                    if result['result'] == 'success':
                        success += 1
                    else:
                        fail += 1
                    detail.append({device_type: {"request": body, "response": result}})
            except TypeError as e:
                fail += 1
                detail.append({device_type: 'data set wrong'})
                print(e)
    return {"success": success, "fail": fail, "detail": detail}
