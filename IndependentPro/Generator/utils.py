def get_token(parameter_list):
    pass


def set_mapping(devietype):
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
        'WaterPumpSensor': [],
        'SmokeDetectionSensor': []
    }
    return mapping[devietype]

