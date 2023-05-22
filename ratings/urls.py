from django.urls import path
from . import views

app_name = 'ratings'

urlpatterns = [ 
    path('<str:location_name>', views.location_rating, name='location_rating'),
    path('<str:location_name>/add_rating', views.add_rating, name='add_rating')
]