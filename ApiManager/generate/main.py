import os
import json
import time
from ApiManager.generate.generator import status_generate
from ApiManager.generate.prepare import disable_rule, create_rule, create_point, create_device

if __name__ == '__main__':
    here = os.path.abspath(os.path.dirname(__file__))
    file = here + '\\init_data.json'
    with open(file, encoding='utf-8') as data:
        source = data.read()
    data = json.loads(source)
    print(data)
    print(type(data))

    rule = data['rules'][0]['rule_json']
    point = data['rules'][0]['point']
    device = data['rules'][0]['device']

    # select fe api env
    env_fe = {"url": "https://10.101.12.4:17998", "token": "063f2acb8048a8af15074f0387aeda1b"}
    # select gate way env
    env_gateway = {"url": "http://10.101.12.4:10099"}
    env_screen = {"url": "http://10.101.12.4:17999"}

    disable_rule(env_screen)
    create_rule(env_screen, rule)
    point_name = create_point(env_fe, point)
    time.sleep(5)
    create_device(env_fe, device, point_name)

    ID_MAPPING = {
        device['deviceType']: {
            "close": {
                "door_status": False
            },
            "id_channel": [
                {
                    "id": device['deviceID'],
                    "channel": device['channel']
                }
            ],
            "open": {
                "door_status": True
            }
        }
    }

    # select which data to create?
    # 1. status stuffgeo vortex saige camera etc
    status_devices = ['VehicleGeolocating', 'StuffGeolocating', 'ParkingLotSystem']
    # 2. events open or close
    events_devices = ['WaterPressureSensor', 'WellCoverSensor', 'ElevatorSensor']
    devices = status_devices + events_devices
    # devices = ['VehicleGeolocating', 'StuffGeolocating']
    status_generate(["RegisterDoorSensor"], env_fe, env_gateway, ID_MAPPING, 'close')
    # print(get_metadata(env_fe, 'api-key'))
