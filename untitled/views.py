from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    #html = t.render({'current_date':now})
    #html = t.render()
    #return HttpResponse(html)
    return render_to_response('current_datetime.html',{'current_date':now})


def hours_ahead(request):
    offset = 111;
    dt =datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render_to_response('hours_ahead.html', {'hour_offset': offset} ,{'next_time':dt})
