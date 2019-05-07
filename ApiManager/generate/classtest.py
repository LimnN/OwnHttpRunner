class EventGenerator(object):
    def __init__(self, status_devices, event_devices, fe_env, gateway_env):
        self.statue_devices = status_devices
        self.event_devices = event_devices
        self.fe_env = fe_env
        self.gateway_env = gateway_env

    def event_generate(self, status_devices, isopen):
        pass

    def status_generate(self, status_devices):
        pass

    def execute(self):
        pass


if __name__ == '__main__':
    pass
