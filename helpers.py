import requests
import json

def get_geoobject_params(toponym_to_find):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym_to_find,
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)

    if not response:
        pass


    json_response = response.json()
    #print(json.dumps(json_response, ensure_ascii=False, indent=4))
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    # Координаты центра топонима:
    toponym_coordinates = toponym["Point"]["pos"]
    #print(toponym_coordinates)
    toponym1 = toponym['boundedBy']["Envelope"]

    toponym_coordinates1 = [toponym1["lowerCorner"], toponym1['upperCorner']]
    spns = []
    for sp in toponym_coordinates1:
        p = sp.split(' ')
        for i in range(2):
            p[i] = float(p[i])
        spns.append(p)
    deltas = [spns[1][0] - spns[0][0], spns[1][1] - spns[0][1]]
    toponym_longitude, toponym_lattitude = toponym_coordinates.split(" ")
    #print(deltas)
    for i in range(2):
        deltas[i] = str(deltas[i])

    return {
        "ll": ",".join([toponym_longitude, toponym_lattitude]),
        "spn": ",".join(deltas),
        "l": "map",
        "pt": ','.join(toponym_coordinates.split(' ')) + ',pm2rdl'
    }