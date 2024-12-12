from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.HomeControllerView.as_view() , name='home'),
]