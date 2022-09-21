from django.shortcuts import render
from mywatchlist.models import WatchlistMovie
from django.http import HttpResponse
from django.core import serializers

# TODO: Create your views here.
def show_watchlist(request):
    data_watchlist = WatchlistMovie.objects.all()
    context = {
        'watchlist': data_watchlist,
        'nama': 'Hanin',
        'student_id': '2106751234',
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = WatchlistMovie.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = WatchlistMovie.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = WatchlistMovie.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = WatchlistMovie.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_html(request):
    data = WatchlistMovie.objects.all()
    return HttpResponse(serializers.serialize("html", data), content_type="application/html")