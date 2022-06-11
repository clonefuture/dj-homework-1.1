from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def lst_stations():
    # with open(os.path.join(settings.BASE_DIR, 'data-398-2018-08-30.csv'), encoding='UTF-8') as csvfile:
    with open(settings.BUS_STATION_CSV, encoding='UTF-8') as csvfile:
        reader = csv.DictReader(csvfile)
        stations_lst = []
        for row in reader:
            stations = {'Name': row['Name'], 'Street': row['Street'], 'District': row['District']}
            stations_lst.append(stations)
        return stations_lst


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    stations = lst_stations()
    paginator = Paginator(stations, 10)
    page_number = request.GET.get('page', 1)
    stations = paginator.get_page(page_number)
    context = {
        'page': stations,
        'bus_stations': stations,
    }
    return render(request, 'stations/index.html', context)
