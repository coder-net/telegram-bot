import app


API = 'https://api.openweathermap.org/data/2.5/weather'
appid = 'd88a41cccbd9e035b21b3ba6f0aa1242'


def get_weather(lat, lon):
    p = {
        'appid': appid,
        'lat': lat,
        'lon': lon
    }
    try:
        res = app.requests.get(API, params=p).json()
    except:
        return 'Something go wrong. Try again'

    l = [
        'City: {}\n'.format(res['name']),
        '*{}*\n'.format(res['weather'][0]['main']),
        'Temperature: {} C (Min: {}, Max: {})'.format(
            res['main']['temp'] - 273.15,
            res['main']['temp_min'] - 273.15,
            res['main']['temp_max'] - 273.15
        ),
        'Humidity: {} %'.format(res['main']['humidity']),
        'Wind speed: {} m/s'.format(res['wind']['speed'])
    ]
    return '\n'.join(l)

