from django.urls import path
from .views import Home, areaForm, doseForm, Final, update_data, about


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('forms/area', areaForm, name='areaForm'),
    path('forms/dose', doseForm, name='doseForm'),
    path('final', Final.as_view(), name='final'),
    path('about-us', about, name='about'),
    path('update', update_data, name='update_data'),
]
