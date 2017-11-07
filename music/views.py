
from django.http import Http404
from .models import Albums
#from django.template import loader
from django.shortcuts import render
from django.db import connection as conn
# Create your views here.

def index(request):
	all_albums = Albums.objects.all()
#	template = loader.get_template('music/index.html')
	context = {'all_albums' : all_albums}
	#return HttpResponse(template.render(context,request))
	return render(request,'music/index.html',context)

def details(request,Albums_id):
	try:
		album = Albums.objects.get(pk = Albums_id)
	except Albums.DoesNotExist:
		raise Http404("Albums does not exist")
	return render(request,'music/detail.html',{'album' : album})
