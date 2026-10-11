from django.urls import path
from . import views
urlpatterns=[
  path('',views.flights,name='flights'),
  path('hotels/',views.hotels,name='hotels'),
  path('trains/',views.trains,name='trains'),
]