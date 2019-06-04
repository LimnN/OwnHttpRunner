from ApiManager.generate.generator import status_generate

ID_MAPPING = {
    "AreaDustMonitor": {
        "close": {},
        "id_channel": [],
        "open": {}
    },
    "BedMat": {
        "close": {},
        "id_channel": [],
        "open": {}
    },
    "CameraMonitor": {
        "close": {},
        "id_channel": [],
        "open": {}
    },
    "CameraPeopleCountingSystem": {
        "close": {},
        "id_channel": [],
        "open": {}
    },
    "DistributionBoxSensor": {
        "close": {},
        "id_channel": [],
        "open": {}
    },
    "DoorSensor": {
        "close": {},
        "id_channel": [],
        "open": {}
    },
    "ElectronicFenceCard": {
        "close": {},
        "id_channel": [],
        "open": {}
    },
    "ElevatorSensor": {
        "close": {
            "direction": 1,
            "speed": 0.2,
            "floor": 3,
            "trouble_type": []
        },
        "id_channel": [
            {
                "id": "MX000579",
                "channel": "telecom"
            }
        ],
        "open": {
            "direction": 1,
            "speed": 0.2,
            "floor": 3,
            "trouble_type": [2, 1]
        }
    },
    "FireAlarmSensor": {
        "close": {},
        "id_channel": [],
        "open": {}
    },
    "GeomagneticSensor": {
        "close": {},
        "id_channel": [],
        "open": {}
    },
    "ParkingLotSystem": {
        "close": {},
        "id_channel": [],
        "open": {}
    },
    "PuddleSensor": {
        "close": {},
        "id_channel": [],
        "open": {}
    },
    "RegionalPedestrianFlow": {
        "close": {},
        "id_channel": [],
        "open": {}
    },
    "SmokeDetectionSensor": {
        "close": {
            "smoke": 12
        },
        "id_channel": [
            {
                "channel": "sii",
                "id": "D1530710043009"
            }
        ],
        "open": {
            "smoke": 200
        }
    },
    "StuffGeolocating": {
        "close": {
            "latitude": 31.2310654404,
            "work_status": True,
            "working_hours": 3,
            "name": "\u5434\u96ef\u7ee2",
            "longitude": 121.4537033905
        },
        "id_channel": [
            {
                "channel": "paidanSystem",
                "id": "paidan-test"
            }
        ],
        "open": {}
    },
    "TemperatureHumiditySensor": {
        "close": {},
        "id_channel": [],
        "open": {}
    },
    "TemperatureSmokeSensor": {
        "close": {},
        "id_channel": [],
        "open": {}
    },
    "TrashBin": {
        "close": {
            "garbage": 89
        },
        "id_channel": [
            {
                "channel": "unicom",
                "id": "863703037668410"
            }
        ],
        "open": {
            "garbage": 12
        }
    },
    "VehicleGeolocating": {
        "close": {},
        "id_channel": [],
        "open": {}
    },
    "WaterLevelSensor": {
        "close": {},
        "id_channel": [],
        "open": {}
    },
    "WaterPressureSensor": {
        "close": {
            "pressure": 0.5
        },
        "id_channel": [
            {
                "channel": "sii",
                "id": "D1538040276673"
            }
        ],
        "open": {
            "pressure": 0.2
        }
    },
    "WaterPumpSensor": {
        "close": {},
        "id_channel": [],
        "open": {}
    },
    "WeChatDoorOpen": {
        "close": {},
        "id_channel": [],
        "open": {}
    },
    "WellCoverSensor": {
        "close": {
            "door_status": True,
            "signal": 98,
            "water_level": [100],
            "water_level_status": False
        },
        "id_channel": [
            {
                "id": "863703039111716",
                "channel": "unicom"
            }
        ],
        "open": {
            "door_status": True,
            "signal": 98,
            "water_level": [400],
            "water_level_status": True
        }
    }
}

if __name__ == '__main__':
    # select fe api env
    env_fe = {"url": "https://10.101.12.4:17998", "token": "063f2acb8048a8af15074f0387aeda1b"}
    # select gate way env
    env_gateway = {"url": "http://10.101.12.4:10099"}
    # select which data to create?
    # 1. status stuffgeo vortex saige camera etc
    status_devices = ['VehicleGeolocating', 'StuffGeolocating', 'ParkingLotSystem']
    # 2. events open or close
    events_devices = ['WaterPressureSensor', 'WellCoverSensor', 'ElevatorSensor']
    devices = status_devices + events_devices
    # devices = ['VehicleGeolocating', 'StuffGeolocating']
    status_generate(events_devices, env_fe, env_gateway, ID_MAPPING, 'open')
    # print(get_metadata(env_fe, 'api-key'))
    # select event number to create? maybe
    # TODO maybe set num\ town\ time ?
    # two part : need status? need events?
    # select date & time maybe
    # select town & district maybe
    # select channel maybe
    # select how many devices? eg. 1 WellCoverSensor 3 DoorSensors
