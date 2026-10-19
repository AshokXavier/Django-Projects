from django.urls import path
from . import views

urlpatterns = [
  path('',views.register,name='form'),
  path('details/',views.pet_details,name='pet_details'),
  path('delete/<int:id>',views.delete,name='delete'),
  path('update/<int:id>',views.update,name='update')
]
