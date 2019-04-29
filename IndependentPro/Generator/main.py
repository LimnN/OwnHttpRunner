from IndependentPro.Generator.event_generator import EventGenerator
from IndependentPro.Generator.utils import get_token

if __name__ == "__main__":
    gateway = {"url": "http://10.101.12.4:10099"}
    fe = {"url": "https://10.101.12.4:17998", "token": "063f2acb8048a8af15074f0387aeda1b"}
    device_types = ['WellCoverSensor', 'WaterPressureSensor', 'SmokeDetectionSensor']
    gen = EventGenerator(gateway, fe, device_types)
    gen.set_devicetypes2ids()
