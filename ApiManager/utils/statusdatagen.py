import time


def set_body(devicetype, channel):
    deviceid = ''
    devicetype = devicetype
    timestamp = int(time.time())
    # data depend on device type
    data = set_data(devicetype)
    body = {
        "deviceType": devicetype,
        "deviceID": deviceid,
        "timestamp": timestamp,
        "data": data
    }
    return body


def set_data(devicetype):
    data = {}

    def doorsensor():
        pass

    return data


def set_id(devicetype):
    # including channel???
    pass
# TODO may be set a devicetype's template in fe


def set_devicetype_id():
    mapping = {
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
        'WaterPumpSensor': []
    }
