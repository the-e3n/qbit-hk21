from django.urls import path
from .views import Home, areaForm, doseForm, Final


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('forms/area', areaForm, name='areaForm'),
    path('forms/dose', doseForm, name='doseForm'),
    path('final', Final.as_view(), name='final'),
]
