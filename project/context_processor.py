import requests

def weather_context(request):
    api_key = '01da91d1819f2d67733e0d2c76216220'
    city = 'Warsaw'
    weather = {
        'temperature': 'N/A',
        'description': 'N/A',
        'city': 'N/A'
    }
    try:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=pl&appid={api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = {
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'city': data['name']
            }
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
    
    return {'weather': weather}
