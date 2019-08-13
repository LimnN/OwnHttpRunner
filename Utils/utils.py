def brackets_match(string, sign):
    match_map = {'{': '}'}
    count = 0
    stack = ''
    unit = []
    for char in string:
        if char == sign:
            count += 1
            stack += char
            continue
        elif char == match_map[sign]:
            count -= 1
            stack += char
            if count == 0:
                print(stack)
                unit.append(stack)
                stack = ''
                continue
            else:
                continue
        else:
            stack += char
            continue
    return unit


if __name__ == '__main__':
    string1 = '{"data": {"primeID": "shcg.5f60b158-6a77-4a5c-9837-6524210d59a5", "args": {}, "data": {' \
              '"town": {"areaID": 33, "areaCategory": "街道", "areaName": "北站街道"}, "working_hours": 7.0, ' \
              '"name": "孟维纳", "district": "静安区", "isVirtual": false, "timestamp": "2019-07-29T11:45:46+0800", ' \
              '"isSensor": false, "exists": true, "setup_time": "2018-06-22T18:32:28+0800", "work_status": true, ' \
              '"lastActiveTS": "2019-06-23T22:13:14+0800", "address": "", "department": "城管中队", ' \
              '"vendor": "孟维纳", "area_district": {"areaID": 39, "areaCategory": "区", "areaName": "静安区"}, ' \
              '"channel": "shcg", "location": {"lat": 31.264292908157767, "lon": 121.45778235534962}}, ' \
              '"messageType": "StuffGeolocating", "messageClass": "joined-status"}, "result": "success"}{' \
              '"data": {"primeID": "shcg.47bb86ea-beec-497e-859e-e86bd1220125", "args": {}, "data": {"town": ' \
              '{"areaID": 33, "areaCategory": "街道", "areaName": "北站街道"}, "working_hours": 4.0, "name": "梁晓", ' \
              '"district": "静安区", "isVirtual": false, "timestamp": "2019-07-29T11:45:45+0800", "isSensor": false, ' \
              '"exists": true, "setup_time": "2018-06-22T18:32:28+0800", "work_status": false, "lastActiveTS": ' \
              '"2019-06-23T22:13:14+0800", "address": "", "department": "城管中队", "vendor": "梁晓", ' \
              '"area_district": {"areaID": 39, "areaCategory": "区", "areaName": "静安区"}, "channel": "shcg", ' \
              '"location": {"lat": 31.299138051831683, "lon": 121.47774665934915}}, "messageType": ' \
              '"StuffGeolocating", "messageClass": "joined-status"}, "result": "success"}'
    brackets_match(string1, '{')
