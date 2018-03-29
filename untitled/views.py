from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
import datetime
import pymysql

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


def book_list(request):
    db = pymysql.connect( port=3306,user='root',password='root',db='test',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    cusor = db.cursor()
    cusor.execute("select * from org")
    for row in cusor.fetchall():
        id = row
    return render_to_response('book_list.html',{'id':id})