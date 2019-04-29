class EventGenerator(object):

    def __init__(self, fe_env, gateway_env):
        self.fe_env = fe_env
        self.gateway_env = gateway_env

    def set_env(self):
        """
        fe-api env needed is : HOST PORT SSLTOKEN
        gateway env needed is : HOST PORT CHANNEL-TOKEN
        :return:
        """
        pass

    def set_devicetype(self):
        pass

    def set_idmapping(self):
        pass

    def set_rule(self):
        pass

    def execute(self):
        """
        send a status need : HOST PORT CHANNEL-TOKEN & BODY
        BODY contain DATA deviceType deviceID & timestamp
        :return:
        """
        pass
