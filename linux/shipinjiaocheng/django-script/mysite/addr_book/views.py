from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render_to_response

from addr_book.models import People

def hello(request):
    return HttpResponse("Hello World")

def current_time(request):
    import datetime
    now = datetime.datetime.now()
    return HttpResponse(now)

def current_time2(request):
    import datetime
    now = datetime.datetime.now()
    c = Context({'time':now})
    return render_to_response('time.html',c)

def insert(request):
    if request.POST:
        post = request.POST
        new_people = People(
	    name = post["name"],
	    phone = post["phone"],
	    email = post["email"],
	    address = post["address"])
	if post["sex"] == 'M':
	    new_people.sex = True
	else:
	    new_people.sex = False
	new_people.save()
    return render_to_response('insert.html')


def list(request):
    people_list = People.objects.all()
    c = Context({'people_list':people_list,})
    return render_to_response('list.html',c)
