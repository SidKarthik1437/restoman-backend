from django.urls import path
from . import views

urlpatterns = [
    path("", views.getRoutes, name="routes"),
    # path("rest/", views.getRests, name="rests"),
    # path("rest/create", views.createRest, name="create-resr"),
    # path("rest/<str:pk>/update/", views.updateProb, name="update-resr"),
    # path("rest/<str:pk>/delete/", views.deleteProb, name="delete-resr"),
    # path("rest/<str:pk>/", views.getRest, name="rest"),

]
