import sys
from io import BytesIO
import json
from helpers import get_geoobject_params
import requests
from PIL import Image


toponym_to_find = " ".join(sys.argv[1:])


map_api_server = "http://static-maps.yandex.ru/1.x/"

response = requests.get(map_api_server, params=get_geoobject_params(toponym_to_find))

Image.open(BytesIO(
    response.content)).show()
