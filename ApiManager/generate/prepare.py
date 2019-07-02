import requests
import json
import time

"""
    What we want?
    1. 不同town
    2. 不同device
    3. 不同PTscene
    4. 不同topics
    5. 不同eventType 不同级别
    6. 不同eventLevel
    7. 不同areaCategory
    First: Create A rule include
    1. town
    2. eventType
    3. eventLevel
    4. areaCategory
    5. deviceType
    6. trigger
    Second: Create A point
    Third: Create A device
        dependency
        1. bindingPlaceInfo's area ID
"""


# def get_cookie():
#     url = "http://10.101.12.4:17996/users/signin"
#
#     payload = "user_name=admin&password=123456&token="
#     headers = {
#         'accept': "application/json, text/javascript, */*; q=0.01",
#         'accept-encoding': "gzip, deflate",
#         'accept-language': "zh-CN,zh;q=0.9",
#         'cache-control': "no-cache,no-cache",
#         'content-length': "38",
#         'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
#         'host': "10.101.12.4:17996",
#         'origin': "http://10.101.12.4:17996",
#         'pragma': "no-cache",
#         'proxy-connection': "keep-alive",
#         'referer': "http://10.101.12.4:17996/",
#         'user-agent': "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
#                       "Chrome/75.0.3770.90 Safari/537.36",
#         'x-requested-with': "XMLHttpRequest",
#         'Postman-Token': "4e9f5336-f0c7-423c-b3e4-7ef33fe1e5b5"
#     }
#
#     response = requests.request("POST", url, data=payload, headers=headers)
#     return response.headers['Set-Cookie']


def create_rule(screen_env, rule):
    """

    :param screen_env:
    :param rule:
    :return:
    """
    check = check_exist('rule', rule, screen_env)
    if check == 'Exist':
        print('Rule Already Exists')
        return 'Rule Already Exists'
    elif check is None:
        # screen_env = {"url": "http://10.101.12.4:17999"}
        url = screen_env['url'] + '/united-ciimc-api/v1/area-rule/create'

        rule = rule
        params = {
            "data": json.dumps(rule)
        }
        response = requests.request('POST', url, params=params)
        print("********rule create********")
        print(response.json())
        return response.json()


def create_point(fe_env, point):
    check = check_exist('point', point, fe_env)
    if check == 'Exist':
        print('Point Already Exists')
        return 'Point Already Exists'
    elif check is None:
        # fe_env = {"url": "https://10.101.12.4:17998", "token": "063f2acb8048a8af15074f0387aeda1b"}
        url = fe_env['url'] + '/ciimc-fe-api/area/create'
        params = {
            "token": fe_env['token']
        }

        payload = 'area_json=' + json.dumps(point)
        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            'User-Agent': "PostmanRuntime/7.15.0",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "90fadad6-344f-4467-a5c4-0883259a1c34,9621eddf-6a8a-412b-863b-74ce91c9feff",
            'Host': "10.101.12.4:17998",
            'accept-encoding': "gzip, deflate",
            'content-length': "2024",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }

        response = requests.request("POST", url, data=payload, params=params, verify=False, headers=headers)
        print("**********point create************")
        print(response.json())
        return response.json()['data']


def create_device(fe_env, device, point):
    check = check_exist('device', device, fe_env)
    if check == 'Exist':
        print('Device Already Exists')
        return 'Device Already Exists'
    elif check is None:
        # fe_env = {"url": "https://10.101.12.4:17998", "token": "063f2acb8048a8af15074f0387aeda1b"}
        url = fe_env['url'] + '/ciimc-fe-api/device/register'
        params = {
            "token": fe_env['token']
        }
        point_name = point['name']
        # device = device
        device['data']['bindingPlaceInfo'] = point_name
        payload = json.dumps(device)
        headers = {
            'Content-Type': "application/json",
            'User-Agent': "PostmanRuntime/7.15.0",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Host': "10.101.12.4:17998",
            'accept-encoding': "gzip, deflate",
            'content-length': "1864",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }

        response = requests.request("POST", url, data=payload, params=params, verify=False, headers=headers)
        print("***********device create********")
        print(device)
        print(response.json())
        return response.json()


def delete_rule():
    pass


def delete_point():
    pass


def delete_device():
    pass


def check_exist(metatype, data, env):
    """

    :param data:
    :param metatype:
    :param env:
        for rule env=screen_env
        for device
    :return:
    """
    print("*******check env************8")
    print(env)
    if metatype == 'rule':
        url = env['url'] + "/united-ciimc-api/v1/area-rule/list"
        response = requests.request("POST", url)
        rules = response.json()
        for rule in rules['data']:
            if rule['name'] == data['name'] and rule['smartRule'] == data['smartRule']:
                return 'Exist'
            else:
                continue
        return None
    elif metatype == 'point':
        url = env['url'] + '/ciimc-fe-api/area/list'
        params = {
            "token": env['token'],
            "name": data['name'],
            "category": "点位"
        }
        response = requests.request('GET', url, verify=False, params=params).json()
        if response['count'] == 0:
            return None
        elif response['count'] > 0:
            for area in response['areas']:
                if area['name'] == data['name'] and area['address'] == data['address'] \
                        and area['parentID'] == data['parentID']:
                    return 'Exist'
                else:
                    continue
            return 'Exist'
    elif metatype == 'device':
        url = env['url'] + '/ciimc-fe-api/meta/subscribe-change'
        filters = {
            "device": {
                "deviceID": data['deviceID'],
                "deviceType": data['deviceType']
            }
        }
        params = {
            "token": env['token'],
            "message_class": 'device',
            "filters": json.dumps(filters)
        }
        with requests.get(url=url, params=params, stream=True, verify=False) as response:
            devices = []
            for chunk in response.iter_lines(chunk_size=1):
                chunk = chunk.decode('utf-8')
                if chunk:
                    if chunk == 'change':
                        break
                    else:
                        meta = json.loads(chunk)
                        devices.append(meta['record'])
        for device in devices:
            if device['exists'] and device['deviceID'] == data['deviceID'] \
                    and device['deviceType'] == data['deviceType']:
                return 'Exist'
            else:
                return None
        return None
    else:
        print('**************type is not included****************')


def disable_rule(screen_env, data):
    # screen_env = {"url": "http://10.101.12.4:17999"}
    url = screen_env['url'] + "/united-ciimc-api/v1/area-rule/list"

    response = requests.request("POST", url)
    rules = response.json()
    our_rule = []
    for t in data['rules']:
        rule_json = t['rule_json']
        our_rule.append(rule_json['name'])
    for rule in rules['data']:
        if rule['name'] not in our_rule:
            rule['enabled'] = False
            url = screen_env['url'] + "/united-ciimc-api/v1/area-rule/save"
            params = {
                "data": json.dumps(rule)
            }
            response = requests.request("POST", url, params=params)
            print(response.json())
        elif rule['name'] in our_rule:
            continue


def creator():
    pass


def model_set(data, env):
    env_fe = env['fe']
    env_screen = env['screen']
    print(type(env_fe))
    print(type(env_screen))
    id_mapping = {}
    devices = set()
    for t in data['rules']:
        rule = t['rule_json']
        point = t['point']
        device = t['device']
        open_data = t['open_data']
        close_data = t['close_data']

        try:
            id_mapping[device['deviceType']]
        except KeyError:
            id_mapping[device['deviceType']] = {
                "close": close_data,
                "id_channel": [],
                "open": open_data
            }

        id_mapping[device['deviceType']]['id_channel'].append(
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
    return {"ID_MAPPING": id_mapping, "device_types": devices}
