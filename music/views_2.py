from django.shortcuts import render
from django.http import HttpResponse
from .models import Albums
from django.db import connection as conn
# Create your views here.

def index(request):
	cursor = conn.cursor()
	#var storing the results of the database call
	#all_albums = Albums.objects.all()
	cursor.execute("select * from music_albums")
	all_albums = cursor.fetchall()
	
	html = ''
	for album in all_albums:
		url = '/music/' + str(album.id) + '/'
		html += '<a href = "'+ url +'">'+album.artist+'</a><br>'
	
	return HttpResponse(html)

def detail(request,Albums_id):
	return HttpResponse("<h2>Details for album id" + str(Albums_id) + "</h2>")
