# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from models import Album
from django.shortcuts import render
# Create your views here.
def index(request):
    all_albums = Album.objects.all()
    context = {
        'all_albums': all_albums,
    }
    return render(request, 'mainpage/index.html', context)

def detail(request, album_id):
    return HttpResponse("<h2>Details for album id:</h2>"+ str(album_id))
