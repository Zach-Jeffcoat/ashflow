from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('create', views.create),
    path('<id>', views.show),
    path('all', views.allShows),
    path('<id>/edit', views.editShow),
    path('<id>/update', views.updateShow),
    path('<id>/destroy', views.destroyShow),
]