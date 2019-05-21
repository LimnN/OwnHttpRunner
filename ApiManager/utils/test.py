import shutil
from os.path import exists

import requests
import json
import base64
import time
import os


# from Crypto.Cipher import AES


def get_metadata(env, message_class):
    """
    :param env: env is a dict include url and ssl token
    :param message_class
    :return: is a list like this: [{'channel': 'channel1', 'key': 'aaaaa', 'uuid': 'bbbbb',
    'deviceTypes': ['' , '', '']},{}]
    """
    env = {"url": "https://10.101.12.4:17998", "token": "063f2acb8048a8af15074f0387aeda1b"}
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
                    if message_class == 'channel':
                        meta.append(data['record']['name'])
                    elif message_class == 'api-key':
                        channel = data['record']['channel']
                        key = data['record']['key']
                        uuid = data['record']['uuid']
                        devicetypes = data['record']['deviceTypes']
                        meta.append({"channel": channel, "key": key, "uuid": uuid, "deviceTypes": devicetypes})
    return meta


def get_token(env, channel):
    env = {"url": "http://10.101.12.4:10099"}
    url = env['url'] + '/v2/auth'
    channels = get_metadata(env=[], message_class='api-key')
    api_key = None
    for chan in channels:
        if channel == chan['channel']:
            api_key = chan['key']
            break
    params = {"key": api_key}
    with requests.get(url=url, params=params) as response:
        print(response.json())


def get_imagedata(isarray):
    """
    :param isarray: is a list? True or False
    :return:
    """
    # image_data = None
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


def set_data(devicetype):
    def doorsensor():
        print("this is door sensor")

    def waterpressuresensor():
        print("this is water pressure sensor")

    swither = {
        "DoorSensor": doorsensor,
        "WaterPressureSensor": waterpressuresensor
    }
    swither[devicetype]()


def send_status():
    url = "http://10.101.12.4:10099/v2/device/event"

    querystring = {"token": "76a0863ebdf830eb43aa19141a778e70d8c2e1ba9261118249243c02c5886d06"}

    data_dict = {
        "deviceType": "AreaDustMonitor",
        "deviceID": "SXHB0JAQX00003",
        "timestamp": 1546930862,
        "data": {
            "dust_avg": 0.01,
            "signal": 98
        }
    }
    payload = json.dumps(data_dict)
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "c396ef0e-413e-4baf-b548-909ed2c06df7"
    }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    print(response.text)


def smokeopen():
    url = "http://10.101.12.4:10099/v2/device/event"

    querystring = {"token": "6b7228ef31c207035868c28162cdb2bfcacdd53e444f8cfc5fc21a66d85d9696"}

    # payload = "{\n    \"deviceType\": \"WaterPressureSensor\",\n    \"deviceID\": \"D1538040277089\",\n
    # \"timestamp\": 1556010121,\n    \"data\": {\n        \"pressure\": 0.2\n    }\n}"
    device = 'SmokeDetectionSensor'
    deviceid = 'D1530710043009'
    timestamp = int(time.time()) - 1000
    data = {
        "smoke": 132
    }
    j = {
        "deviceType": device,
        "deviceID": deviceid,
        "timestamp": timestamp,
        "data": data
    }
    payload = json.dumps(j)
    headers = {
        'Content-Type': "application/json",
        'User-Agent': "PostmanRuntime/7.11.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "4ad8a33b-3bcb-4ba0-8656-0836f317161e,b98eaf3b-b386-4800-b7aa-218e8965bf11",
        'Host': "10.101.12.4:10099",
        'accept-encoding': "gzip, deflate",
        'content-length': "153",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    print(response.text)


def smokeclose():
    url = "http://10.101.12.4:10099/v2/device/event"

    querystring = {"token": "6b7228ef31c207035868c28162cdb2bfcacdd53e444f8cfc5fc21a66d85d9696"}

    # payload = "{\n    \"deviceType\": \"WaterPressureSensor\",\n    \"deviceID\": \"D1538040277089\",\n
    # \"timestamp\": 1556010121,\n    \"data\": {\n        \"pressure\": 0.002\n    }\n}"
    device = 'SmokeDetectionSensor'
    deviceid = 'D1530710043009'
    timestamp = int(time.time()) - 1000
    data = {
        "smoke": 12
    }
    j = {
        "deviceType": device,
        "deviceID": deviceid,
        "timestamp": timestamp,
        "data": data
    }
    payload = json.dumps(j)
    headers = {
        'Content-Type': "application/json",
        'User-Agent': "PostmanRuntime/7.11.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "4ad8a33b-3bcb-4ba0-8656-0836f317161e,b98eaf3b-b386-4800-b7aa-218e8965bf11",
        'Host': "10.101.12.4:10099",
        'accept-encoding': "gzip, deflate",
        'content-length': "153",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    print(response.text)


def pressureopen():
    url = "http://10.101.12.4:10099/v2/device/event"

    querystring = {"token": "6b7228ef31c207035868c28162cdb2bfcacdd53e444f8cfc5fc21a66d85d9696"}

    # payload = "{\n    \"deviceType\": \"WaterPressureSensor\",\n    \"deviceID\": \"D1538040277089\",\n
    # \"timestamp\": 1556010121,\n    \"data\": {\n        \"pressure\": 0.002\n    }\n}"
    device = 'WaterPressureSensor'
    deviceid = 'D1538040277089'
    timestamp = int(time.time()) - 1000
    data = {
        "pressure": 0.2
    }
    j = {
        "deviceType": device,
        "deviceID": deviceid,
        "timestamp": timestamp,
        "data": data
    }
    payload = json.dumps(j)
    headers = {
        'Content-Type': "application/json",
        'User-Agent': "PostmanRuntime/7.11.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "4ad8a33b-3bcb-4ba0-8656-0836f317161e,b98eaf3b-b386-4800-b7aa-218e8965bf11",
        'Host': "10.101.12.4:10099",
        'accept-encoding': "gzip, deflate",
        'content-length': "153",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    print(response.text)


def pressureclose():
    url = "http://10.101.12.4:10099/v2/device/event"

    querystring = {"token": "6b7228ef31c207035868c28162cdb2bfcacdd53e444f8cfc5fc21a66d85d9696"}

    # payload = "{\n    \"deviceType\": \"WaterPressureSensor\",\n    \"deviceID\": \"D1538040277089\",\n
    # \"timestamp\": 1556010121,\n    \"data\": {\n        \"pressure\": 0.002\n    }\n}"
    device = 'WaterPressureSensor'
    deviceid = 'D1538040277089'
    timestamp = int(time.time()) - 1000
    data = {
        "pressure": 0.0012
    }
    j = {
        "deviceType": device,
        "deviceID": deviceid,
        "timestamp": timestamp,
        "data": data
    }
    payload = json.dumps(j)
    headers = {
        'Content-Type': "application/json",
        'User-Agent': "PostmanRuntime/7.11.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "4ad8a33b-3bcb-4ba0-8656-0836f317161e,b98eaf3b-b386-4800-b7aa-218e8965bf11",
        'Host': "10.101.12.4:10099",
        'accept-encoding': "gzip, deflate",
        'content-length': "153",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    print(response.text)


def regionflow(num_stay):
    url = "http://10.101.12.4:10099/v2/device/event"

    querystring = {"token": "0d9962ff210f4e56588c21e90d8b7be70c8cca2b5615c29441be386b6d943803"}

    # payload = "{\n    \"deviceType\": \"RegionalPedestrianFlow\",\n    \"deviceID\": \"HCZ-HCS-01\",\n
    # \"timestamp\": 1556010121,\n    \"data\": {\n        \"num_stay\": 254,\n        \"num_enter\": 10,\n
    # \"num_leave\": 12\n    }\n}"
    device = 'RegionalPedestrianFlow'
    deviceid = 'HCZ-HCS-01'
    timestamp = int(time.time()) - 1000
    data = {
        "num_enter": 12,
        "num_leave": 23,
        "num_stay": num_stay
    }
    j = {
        "deviceType": device,
        "deviceID": deviceid,
        "timestamp": timestamp,
        "data": data
    }
    payload = json.dumps(j)
    headers = {
        'Content-Type': "application/json",
        'User-Agent': "PostmanRuntime/7.11.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "8b2f1cc7-96aa-42c7-a3b2-a64ebca68c03,1a700025-72f6-49f5-afc4-c3a39db019d6",
        'Host': "10.101.12.4:10099",
        'accept-encoding': "gzip, deflate",
        'content-length': "200",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    print(response.text)


def smokeevent():
    smokeopen()
    time.sleep(10)
    smokeclose()
    time.sleep(10)


def pressureevent():
    pressureopen()
    time.sleep(10)
    pressureclose()
    time.sleep(10)


NUM_STAY = 23
OPEN = 300
CLOSE = 9


def railwayopen():
    # stay = 23
    global NUM_STAY
    # open
    regionflow(NUM_STAY)
    time.sleep(5)
    regionflow(NUM_STAY + CLOSE)
    time.sleep(10)
    regionflow(NUM_STAY + OPEN + CLOSE)
    NUM_STAY = NUM_STAY + OPEN + CLOSE

    # close
    time.sleep(10)
    regionflow(NUM_STAY)
    time.sleep(10)
    regionflow(NUM_STAY + CLOSE)
    NUM_STAY = NUM_STAY + CLOSE


def mk_model_dir():
    here = os.path.abspath(os.path.dirname(__file__))
    model_folder = os.path.join(here, '..\\models')
    if not exists(model_folder):
        os.mkdir(model_folder)
    return model_folder


def query():
    url = "http://10.101.12.4:17999/united-ciimc-api/v1/generic-query"

    # querystring = {"table": "area-event", "index_type": "active", "limit": "5", "offset": "0",
    #                "filter": "time%3D1500000000~1600000000%26town.id%3Deq.2%26area_district.id%3Deq.39%26"
    #                          "simple.messageType%3D%E7%8E%AF%E5%8D%AB%E5%B8%82%E5%AE%B9%26eventSourceType%3Deq.2%26"
    #                          "eventDiscoverType%3Deq.%E4%B8%BB%E5%8A%A8%E5%8F%91%E7%8E%B0%26"
    #                          "address%3Deq.%E5%AE%89%E4%B8%9A%E8%B7%AF21%E5%8F%B7%E5%90%91%E5%8C%9715%E7%B1%B3%26"
    #                          "args.eventLevel%3D0",
    #                "transform": "messages%5B%5D.%7Buuid%3Adata.uuid%2Ctown%3Adata.town.areaName%2CeventSourceType%3A"
    #                             "data.eventSourceType%2CeventDiscoverType%3Adata.eventDiscoverType%2CeventType%3A"
    #                             "messageType%2CeventLevel%3Aargs.eventLevel%2Caddress%3Adata.address%2Ctimestamp%3A"
    #                             "data.openTS%2CisOpen%3Adata.isOpen%7D",
    #                "need_transform": "1"}
    table = 'area-event'
    index = 'active'
    limit = 5
    offset = 0
    filters = 'time=1557974120~1557974122' \
              '&area_district.id=eq.39'
    # filters = 'time=1500000000~1600000000' \
    #           '&town.id=eq.2' \
    #           '&area_district.id=eq.39' \
    #           '&simple.messageType=环卫市容' \
    #           '&eventSourceType=eq.2' \
    #           '&eventDiscoverType=eq.主动发现' \
    #           '&address=eq.安业路21号向北15米' \
    #           '&args.eventLevel=0'
    transform = 'messages[].{' \
                'uuid:data.uuid,town:data.town.areaName,eventSourceType:data.eventSourceType,' \
                'eventDiscoverType:data.eventDiscoverType,' \
                'eventType:messageType,' \
                'eventLevel:args.eventLevel,' \
                'address:data.address,' \
                'timestamp:data.openTS,' \
                'isOpen:data.isOpen}'
    need_transform = 1
    params = {
        "table": table,
        "index": index,
        "limit": limit,
        "offset": offset,
        "filter": filters,
        "transform": transform,
        "need_transform": need_transform
    }

    payload = ""
    headers = {
        'User-Agent': "PostmanRuntime/7.11.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "f38dce01-941e-49eb-8f0f-8685e821c5f0,c0e4465c-ad97-4bb8-bcc4-ce146fda5bde",
        'Host': "10.101.12.4:17999",
        'accept-encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=params)

    print(response.text)


def query_map():
    url = "http://10.101.12.4:17999/united-ciimc-api/v1/generic-query"

    # querystring = {"table": "area-event", "index_type": "active", "limit": "0",
    #                "filter": "time%3D1500000000~1600000000%26"
    #                          "town.id%3Deq.2%26"
    #                          "area_district.id%3Deq.39%26"
    #                          "simple.messageType%3D%E7%8E%AF%E5%8D%AB%E5%B8%82%E5%AE%B9%26"
    #                          "eventSourceType%3Deq.2%26"
    #                          "eventDiscoverType%3Deq.%E4%B8%BB%E5%8A%A8%E5%8F%91%E7%8E%B0%26"
    #                          "address%3Deq.%E5%AE%89%E4%B8%9A%E8%B7%AF21%E5%8F%B7%E5%90%91%E5%8C%9715%E7%B1%B3%26"
    #                          "args.eventLevel%3D0",
    #                "group_by": "geo.p8"}
    table = 'area-event'
    index = 'active'
    limit = 0
    filters = 'time=1500000000~1600000000'
    # '&area_district.id=eq.39'
    # filters = 'time=1500000000~1600000000' \
    #           '&town.id=eq.2' \
    #           '&area_district.id=eq.39' \
    #           '&simple.messageType=环卫市容' \
    #           '&eventSourceType=eq.2' \
    #           '&eventDiscoverType=eq.主动发现' \
    #           '&address=eq.安业路21号向北15米' \
    #           '&args.eventLevel=0'
    group_by = 'geo.p8'
    params = {
        "table": table,
        "index": index,
        "limit": limit,
        "filter": filters,
        "group_by": group_by
    }
    payload = ""
    headers = {
        'User-Agent': "PostmanRuntime/7.11.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "9b5282c5-0d28-490a-824b-971c2be1690d,fb89745e-5040-4469-97b7-3d82818385bd",
        'Host': "10.101.12.4:17999",
        'accept-encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=params)

    print(response.text)


if __name__ == "__main__":
    # query()
    # query_map()
    # smokeopen()
    # smokeclose()
    # railwayopen()
    # for i in range(200):
    #     smokeevent()
    #     pressureevent()
    # for i in range(1):
    #     smokeevent()
    #     # pressureclose()
    #     # time.sleep(10)
    #     # pressureopen()
    #     pressureevent()
    #     railwayopen()
    tem = {'id_channel': [{'id': '863703037668410', 'channel': 'unicom'}], 'open': {'garbage': 12},
           'close': {'garbage': 89}}
    string = str(tem)
    print(string)
