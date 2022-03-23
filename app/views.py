from django.shortcuts import render
from django.views.generic import View
import requests
import random

API = 'https://countriesnow.space/api/v0.1/countries/capital'


class HomeView(View):
    @staticmethod
    def get(request, *args, **kwargs):
        response = requests.get(API)
        print('ASDFDF', response)
        countries = response.json().get('data', [])
        print('987654687', countries)
        country = random.choice(countries)

        context = {
            'country': country
        }
        return render(request, 'index.html', context)

    @staticmethod
    def post(request, *args, **kwargs):
        country = request.POST.get('country')
        capital = request.POST.get('capital')

        response = requests.get(API)
        countries = response.json().get('data', [])

        found_item = next(
            item for item in countries if item["name"] == country)

        context = {
            'country': found_item
        }

        if found_item['capital'].lower() == capital.lower():
            context['result'] = {
                'correct': True,
            }
        else:
            context['result'] = {
                'correct': False,
            }
        return render(request, 'index.html', context)
