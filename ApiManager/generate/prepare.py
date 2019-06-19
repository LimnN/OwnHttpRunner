import requests
import json

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


def get_cookie():
    url = "http://10.101.12.4:17996/users/signin"

    payload = "user_name=admin&password=123456&token="
    headers = {
        'accept': "application/json, text/javascript, */*; q=0.01",
        'accept-encoding': "gzip, deflate",
        'accept-language': "zh-CN,zh;q=0.9",
        'cache-control': "no-cache,no-cache",
        'content-length': "38",
        'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
        'host': "10.101.12.4:17996",
        'origin': "http://10.101.12.4:17996",
        'pragma': "no-cache",
        'proxy-connection': "keep-alive",
        'referer': "http://10.101.12.4:17996/",
        'user-agent': "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/75.0.3770.90 Safari/537.36",
        'x-requested-with': "XMLHttpRequest",
        'Postman-Token': "4e9f5336-f0c7-423c-b3e4-7ef33fe1e5b5"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    return response.headers['Set-Cookie']


def create_rule(screen_env, rule):
    """

    :param screen_env:
    :param rule:
    :return:
    """
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
    fe_env = {"url": "https://10.101.12.4:17998", "token": "063f2acb8048a8af15074f0387aeda1b"}
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


def disable_rule(screen_env):
    # screen_env = {"url": "http://10.101.12.4:17999"}
    url = screen_env['url'] + "/united-ciimc-api/v1/area-rule/list"

    response = requests.request("POST", url)
    rules = response.json()
    for rule in rules['data']:
        # print(type(rule))
        rule['enabled'] = False
        url = screen_env['url'] + "/united-ciimc-api/v1/area-rule/save"
        params = {
            "data": json.dumps(rule)
        }
        response = requests.request("POST", url, params=params)
    # print(response.json())


if __name__ == '__main__':
    # TODO check if area rule/ point/ device exist
    # disable_rule()
    # print(get_cookie())
    # print(create_point())
    # point = create_point()
    # print(create_device(point))
    disable_rule()
    create_rule()
    # create_point()
    create_device()
    # print(create_device())
