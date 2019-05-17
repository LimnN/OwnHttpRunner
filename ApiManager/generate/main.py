from ApiManager.generate.generator import status_generate

MAPPING = {
    "ID_MAPPING": {
        "WellCoverSensor": [],
        "StuffGeolocating": [
            {
                "id": "07ee5f2a-1ad9-4540-bad4-7969480fe36e",
                "channel": "shcg"
            }
        ],
        "CameraMonitor": [],
        "WeChatDoorOpen": [],
        "BedMat": [],
        "WaterPressureSensor": [
            {
                "id": "D1538040277089",
                "channel": "sii"
            }
        ],
        "VehicleGeolocating": [
            {
                "id": "13501752513",
                "channel": "saige"
            }
        ],
        "CameraPeopleCountingSystem": [],
        "ParkingLotSystem": [
            {
                "id": "ja31010600001",
                "channel": "road-service"
            }
        ],
        "ElevatorSensor": [],
        "DistributionBoxSensor": [],
        "TrashBin": [{"id": "863703037668410", "channel": "unicom"}],
        "PuddleSensor": [],
        "ElectronicFenceCard": [],
        "AreaDustMonitor": [],
        "TemperatureSmokeSensor": [],
        "TemperatureHumiditySensor": [],
        "DoorSensor": [],
        "FireAlarmSensor": [],
        "WaterLevelSensor": [],
        "GeomagneticSensor": [],
        "RegionalPedestrianFlow": [
            {
                "id": "HCZ-HCS-01",
                "channel": "newlan"
            }
        ],
        "WaterPumpSensor": [],
        "SmokeDetectionSensor": [
            {
                "id": "D1530710043009",
                "channel": "sii"
            }
        ]
    },
    "dataModel": {
        "SmokeDetectionSensor": {
            "open": {"smoke": 200},
            "close": {"smoke": 12}
        }
    }
}
data = {
    "ID_MAPPING": {
        "WellCoverSensor": [],
        "StuffGeolocating": [
            {
                "id": "07ee5f2a-1ad9-4540-bad4-7969480fe36e",
                "channel": "shcg"
            }
        ],
        "CameraMonitor": [],
        "WeChatDoorOpen": [],
        "BedMat": [],
        "WaterPressureSensor": [
            {
                "id": "D1538040277089",
                "channel": "sii"
            }
        ],
        "VehicleGeolocating": [
            {
                "id": "13501752513",
                "channel": "saige"
            }
        ],
        "CameraPeopleCountingSystem": [],
        "ParkingLotSystem": [
            {
                "id": "ja31010600001",
                "channel": "road-service"
            }
        ],
        "ElevatorSensor": [],
        "DistributionBoxSensor": [],
        "TrashBin": [{"id": "863703037668410", "channel": "unicom"}],
        "PuddleSensor": [],
        "ElectronicFenceCard": [],
        "AreaDustMonitor": [],
        "TemperatureSmokeSensor": [],
        "TemperatureHumiditySensor": [],
        "DoorSensor": [],
        "FireAlarmSensor": [],
        "WaterLevelSensor": [],
        "GeomagneticSensor": [],
        "RegionalPedestrianFlow": [
            {
                "id": "HCZ-HCS-01",
                "channel": "newlan"
            }
        ],
        "WaterPumpSensor": [],
        "SmokeDetectionSensor": [
            {
                "id": "D1530710043009",
                "channel": "sii"
            }
        ]
    },
    "dataModel": {
        "SmokeDetectionSensor": {
            "open": {"smoke": 200},
            "close": {"smoke": 12}
        }
    }
}
ID_MAPPING = data['ID_MAPPING']
data_model = data['dataModel']

if __name__ == '__main__':
    # select fe api env
    env_fe = {"url": "https://10.101.12.4:17998", "token": "063f2acb8048a8af15074f0387aeda1b"}
    # select gate way env
    env_gateway = {"url": "http://10.101.12.4:10099"}
    # select which data to create?
    # 1. status stuffgeo vortex saige camera etc
    status_devices = ['VehicleGeolocating', 'StuffGeolocating', 'ParkingLotSystem']
    # 2. events open or close
    events_devices = ['SmokeDetectionSensor']
    devices = status_devices + events_devices
    # devices = ['VehicleGeolocating', 'StuffGeolocating']
    status_generate(events_devices, env_fe, env_gateway, ID_MAPPING, data_model, True)
    # print(get_metadata(env_fe, 'api-key'))
    # select event number to create? maybe
    # TODO maybe set num\ town\ time ?
    # two part : need status? need events?
    # select date & time maybe
    # select town & district maybe
    # select how many devices? eg. 1 WellCoverSensor 3 DoorSensors
    # set device type data model
