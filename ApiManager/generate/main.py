# from ApiManager.generate.generator import status_generate
from ApiManager.generate.prepare import get_metadata

if __name__ == '__main__':
    # select fe api env
    env_fe = {"url": "https://10.101.12.4:17998", "token": "063f2acb8048a8af15074f0387aeda1b"}
    # select gate way env
    env_gateway = {"url": "http://10.101.12.4:10099"}
    # select which data to create?
    # 1. status stuffgeo vortex saige camera etc
    status_devices = ['VehicleGeolocating', 'StuffGeolocating', 'ParkingLotSystem']
    # 2. events open or close
    events_devices = ['SmokeDetectionSensor', 'WaterPressureSensor']
    devices = status_devices + events_devices
    # devices = ['VehicleGeolocating', 'StuffGeolocating']
    # status_generate(devices, env_fe, env_gateway, True)
    print(get_metadata(env_fe, 'api-key'))
    # select event number to create? maybe
    # TODO maybe set num\ town\ time ?
    # two part : need status? need events?
    # select date & time maybe
    # select town & district maybe
    # select how many devices? eg. 1 WellCoverSensor 3 DoorSensors
    # set device type data model
