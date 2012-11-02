# -*- coding: utf-8 -*-
from places.models import Place
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404

def list_places(request):
    places_list = Place.objects.all().order_by('-creation_date')
    return render_to_response('places/list_places.html', {'title': "Places list (ordered by descending date)", 'places_list': places_list })

def list_places_order_by_views(request):
    places_list = Place.objects.all().order_by('-nr_views')
    return render_to_response('places/list_places.html', {'title': "Places list (ordered by descending number of views)", 'places_list': places_list })

def view_place(request, place_id):
    p = get_object_or_404(Place, pk=place_id)
    p.nr_views += 1
    p.save();
    return render_to_response('places/view_place.html', {'title': "Place details for \"%s\"" % p.name, 'place': p})