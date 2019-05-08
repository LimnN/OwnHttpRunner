from ApiManager.generate.prepare import send_status, get_token, set_body

ID_MAPPING = {
    'WellCoverSensor': [],
    'StuffGeolocating': [{"id": "07ee5f2a-1ad9-4540-bad4-7969480fe36e", "channel": "shcg"}],
    'CameraMonitor': [],
    'WeChatDoorOpen': [],
    'BedMat': [],
    'WaterPressureSensor': [{"id": "D1538040277089", "channel": "sii"}],
    'VehicleGeolocating': [{"id": "64710127608", "channel": "saige"}],
    'CameraPeopleCountingSystem': [],
    'ParkingLotSystem': [{"id": "ja31010600001", "channel": "road-service"}],
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


def area_lua_generate():
    # for area lua event
    # RegionalPedestrianFlow
    pass


def event_generate(devices, fe_env, gateway_env, isopen):
    # for area event generate
    for device in devices:
        device_type = device
        device_id = ID_MAPPING[device][0]['id']
        device_channel = ID_MAPPING[device][0]['channel']
        token = get_token(gateway_env, device_channel, fe_env)
        body = set_body(device_type, device_id, isopen)
        send_status(gateway_env, token, body)


def status_generate(devices, fe_env, gateway_env):
    # for status data generate
    # StuffGeolocating VehicleGeolocating ParkingLotSystem CameraPeopleCountingSystem
    # TODO do result count result = {}
    for device in devices:
        device_type = device
        device_id = ID_MAPPING[device][0]['id']
        device_channel = ID_MAPPING[device][0]['channel']
        token = get_token(gateway_env, device_channel, fe_env)
        body = set_body(device_type, device_id)
        send_status(gateway_env, token, body)


def generator(status_devices, event_devices, fe_env, gateway_env, isopen):
    status_generate(status_devices, fe_env, gateway_env)
    event_generate(event_devices, fe_env, gateway_env, isopen)
