from django.shortcuts import render
import requests
from .models import CITY
from .forms import CityForm

# Create your views here.


def index(request):
    appid = 'c91453e58c1a3c1575a734032a0e49a1'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = CITY.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"]
        }

        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form' : form}

    return render(request, 'pogoda1/index.html', context)