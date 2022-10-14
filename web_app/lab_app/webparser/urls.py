from django.urls import path

from . import views

urlpatterns = [
    path("", views.ParserView.as_view({'post': 'list'})),
]