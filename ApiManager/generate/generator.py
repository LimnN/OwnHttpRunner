from ApiManager.generate.prepare import send_status, get_token, set_body


def area_lua_generate():
    # for area lua event
    # RegionalPedestrianFlow
    pass


def status_generate(devices, fe_env, gateway_env, ID_MAPPING, isopen=False):
    # for status data generate
    # StuffGeolocating VehicleGeolocating ParkingLotSystem CameraPeopleCountingSystem
    # ID_MAPPING = read_json(user)
    success = 0
    fail = 0
    for device in devices:
        if not ID_MAPPING[device]:
            fail += 1
        else:
            device_type = device
            device_id = ID_MAPPING[device][0]['id']
            device_channel = ID_MAPPING[device][0]['channel']
            token = get_token(gateway_env, device_channel, fe_env)
            body = set_body(device_type, device_id, isopen)
            result = send_status(gateway_env, token, body)
            if result['result'] == 'success':
                success += 1
            else:
                fail += 1
    result = {"success": success, "fail": fail}
    return result
