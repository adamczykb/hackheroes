from django.conf.urls import url
from . import views


app_name = 'mapa'

urlpatterns = [
    # city detail view
    url(r'^point/(?P<pk>[0-9]+)$',
        views.PointDetail.as_view(), name='point-detail'),
]