import requests

# TODO Add Map to site


def getMap(api: str, lat: float, long: float, pins: list, save=False):
    baseurl = f'https://dev.virtualearth.net/REST/V1/Imagery/Map/Road/{lat}%2C{long}/13?mapSize=800,600'
    api = f'&key={api}'
    for pin in pins:
        baseurl += f'&pushpin={pin[0]},{pin[1]};66;{pin[2]}'
    baseurl += api
    if save:
        r = requests.get(baseurl)
        with open('img.png', 'wb') as f:
            f.write(r.content)
    return baseurl
