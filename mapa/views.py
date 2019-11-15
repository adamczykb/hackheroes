import cursor as cursor
from django.views.generic import DetailView
from .models import Point
from django.shortcuts import render
from django.db import connection
def PointDetail(request):
    cursor = connection.cursor()
    cursor.execute(
        "select id, name, ST_X(geometry) as x,ST_Y(geometry) as y, description, mphone from public.mapa_point where active=TRUE order by id ")
    nav = cursor.fetchall()
    return render(request, 'main/point-detail.html',{ 'tab':nav})


def addPointDetail(request):
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO mapa_point (name,geometry,active,description,mphone) VALUES ('"+request.POST['title']+"',ST_SetSRID(ST_MakePoint('"+ request.POST['lng'] +"', '"+request.POST['lat']+"'), 4326),'true','"+request.POST['description']+"','"+request.POST['telephone']+"')"
    )
    cursor.execute(
        "select id, name, ST_X(geometry) as x,ST_Y(geometry) as y, description, mphone from public.mapa_point where active=TRUE order by id ")
    nav = cursor.fetchall()
    return render(request, 'main/point-detail.html',{ 'tab':nav})