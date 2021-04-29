from datetime import datetime
from django.shortcuts import render
from .script import get_weather_data
import urllib


def weather(request):
    request.META.get('')
    city = request.GET.get('city')
    api_key = '0feb7dade373f6e98f005e66b1f845be'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    try:
        context = {
            'date': datetime.now,
            'celsius': 'NA-/',
            'city': 'Na-/',
            'country': 'NA-/',
            'fahrenheit': 'NA-/',
            'feel': 'NA-/',
            'wind_speed': 'NA-/',
            'weather': 'NA-/',
            'pressure': 'NA-/',
            'humidity': 'NA-/',
            'five_days_data': None,
            'visibility': 'NA-/'}
        if city is not None:
            data = get_weather_data(url)
            celsius = data['main']['temp_max'] - 273.15
            fahrenheit = celsius * 9 / 5 + 32
            city = data['name']
            country = data['sys']['country']
            feel = data['main']['feels_like']
            wind_speed = data['wind']['speed']
            pressure = data['main']['pressure']
            visibility = data['visibility']
            weather = data['weather'][0]['description']
            humidity = data['main']['humidity']
            context['date'] = datetime.now
            context['celsius'] = celsius
            context['fahrenheit'] = fahrenheit
            context['visibility'] = visibility
            context['city'] = city
            context['country'] = country
            context['feel'] = feel
            context['wind_speed'] = wind_speed
            context['pressure'] = pressure
            context['weather'] = weather
            context['humidity'] = humidity
            next_5_day_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&mode=json&appid={api_key}"
            next_5_day_url_response = get_weather_data(next_5_day_url)

            cel_5 = []
            fr_5 = []
            feel_5 = []
            wind_speed_5 = []
            weather_5 = []
            pressure_5 = []
            humidity_5 = []
            visibility_5 = []
            date_5 = []

            for i in range(0, 40):
                cel_5.append(next_5_day_url_response['list'][i:i + 1][0]['main']['temp_max'] - 273.15)
                fr_5.append(cel_5[i] * 9 / 5 + 32)
                wind_speed_5.append(next_5_day_url_response['list'][i:i + 1][0]['wind']['speed'])
                weather_5.append(next_5_day_url_response['list'][i:i + 1][0]['weather'][0]['main'])
                pressure_5.append(next_5_day_url_response['list'][i:i + 1][0]['main']['pressure'])
                humidity_5.append(next_5_day_url_response['list'][i:i + 1][0]['main']['humidity'])
                feel_5.append(next_5_day_url_response['list'][i:i + 1][0]['main']['feels_like'])
                visibility_5.append(next_5_day_url_response['list'][i:i + 1][0]['visibility'])
                date_5.append(next_5_day_url_response['list'][i:i + 1][0]['dt_txt'])

            five_days_data = list(
                zip(cel_5, fr_5, wind_speed_5, weather_5, pressure_5, humidity_5, visibility_5, date_5))
            context['five_days_data'] = five_days_data
        return render(request, 'home_page.html', context)
    except:
        return render(request, 'error.html')