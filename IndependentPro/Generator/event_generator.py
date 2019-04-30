from IndependentPro.Generator.utils import get_token
import requests
import time
import json

ID_MAPPING = {
    'WellCoverSensor': [],
    'StuffGeolocating': [],
    'CameraMonitor': [],
    'WeChatDoorOpen': [],
    'BedMat': [],
    'WaterPressureSensor': [{"id": "D1538040277089", "channel": "sii"}],
    'VehicleGeolocating': [],
    'CameraPeopleCountingSystem': [],
    'ParkingLotSystem': [],
    'ElevatorSensor': [],
    'DistributionBoxSensor': [],
    'TrashBin': [],
    'PuddleSensor': [],
    'ElectronicFenceCard': [],
    'AreaDustMonitor': [],
    'TemperatureSmokeSensor': [],
    'TemperatureHumiditySensor': [],
    'DoorSensor': [],
    'FireAlarmSensor': [],
    'WaterLevelSensor': [],
    'GeomagneticSensor': [],
    'RegionalPedestrianFlow': [{"id": "HCZ-HCS-01", "channel": "newlan"}],
    'WaterPumpSensor': [],
    'SmokeDetectionSensor': [{"id": "D1530710043009", "channel": "sii"}]
}


class EventGenerator(object):
    def __init__(self, gateway, fe, device_types):
        self.device_types = device_types
        self.gateway = gateway
        self.fe = fe

    def set_env(self):
        """
        setting gateway env & fe-api env
        """
        pass

    def set_devicetypes2ids(self):
        """

        """
        type2id = {}
        for device_type in self.device_types:
            d = {device_type: ID_MAPPING[device_type]}
            type2id.get(d)
        return type2id

    def construct(self, isopen):
        if isopen:
            for device_type in self.device_types:
                device_id = ID_MAPPING[device_type][0]['id']
                channel = ID_MAPPING[device_type][0]['channel']
        else:
            pass

    def execute(self, data):
        """
        data is a list of {channel , deviceType, deviceID, data}
        :param data:
        :return:
        """
        # send a status need url:port token body
        url = self.gateway + '/v2/device/event'
        token = ''  # wait for channel
        params = {"token": token}

        device_type = ''
        device_id = ''
        timestamp = int(time.time())
        data = {}
        pre = {
            "deviceType": device_type,
            "deviceID": device_id,
            "timestamp": timestamp,
            "data": data
        }
        body = json.dumps(pre)

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

        response = requests.request("POST", url, data=body, headers=headers, params=params)
        # for device_type in self.device_types.py:
        #     url = self.gateway + '/v2/device/event'
        #     token = get_token()
        #     data = {}
        #     body = {
        #         "deviceType": device_type,
        #         "deviceID": '',
        #         "timestamp": int(time.time()),
        #         "data": data
        #     }

    def show_rules(self, parameter_list):
        pass

    def set_mapping(self, devietype):
        pass
