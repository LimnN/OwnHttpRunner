from IndependentPro.Generator.utils import get_token
import time

MAPPING = {
    'WellCoverSensor': [],
    'StuffGeolocating': [],
    'CameraMonitor': [],
    'WeChatDoorOpen': [],
    'BedMat': [],
    'WaterPressureSensor': [],
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
    'RegionalPedestrianFlow': [],
    'WaterPumpSensor': [],
    'SmokeDetectionSensor': []
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
            d = {device_type: MAPPING[device_type]}
            type2id.get(d)
        return type2id

    def execute(self, parameter_list):
        """
        execute posts need gateway-env channel-token body
        """
        for device_type in self.device_types:
            url = self.gateway + '/v2/device/event'
            token = get_token()
            data = {}
            body = {
                "deviceType": device_type,
                "deviceID": '',
                "timestamp": int(time.time()),
                "data": data
            }
        pass

    def show_rules(self, parameter_list):
        pass

    def set_mapping(self, devietype):
        pass
