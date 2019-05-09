from ApiManager.generate.generator import status_generate

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
    status_generate(devices, env_fe, env_gateway, False)

    # select event number to create? maybe
    # TODO
    # two part : need status? need events?
    # select date & time maybe
    # select town & district maybe
    # select how many devices? eg. 1 WellCoverSensor 3 DoorSensors
