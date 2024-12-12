from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactUsView.as_view(), name='contact_us'),
    path('api/', views.ContactUsListView.as_view(), name='contact_us_api'),
]
