from PlanB.device_type import SmokeDetectionSensor


def send_data(device_type, isopen):
    return {
        'SmokeDetectionSensor': lambda switch: {"smoke": 200} if switch else {"smoke": 20},
        'WaterPressureSensor': lambda switch: {"pressure": 0.3} if switch else {"pressure": 0.001},
        'RegionalPedestrianFlow': lambda switch: {"num_enter": 12, "num_leave": 23, "num_stay": 24},
    }[device_type](isopen)
