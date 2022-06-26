from django.urls import path

from .views import OnePageView, UpdateDB, UpdateDL

urlpatterns = (
    path('', OnePageView, name='index'),
    path('records/update_data/', UpdateDB, name='updatedb'),
    path('records/update_deadlines/', UpdateDL, name='updatedl'),
)
