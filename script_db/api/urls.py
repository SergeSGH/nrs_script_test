from django.urls import path, include


urlpatterns = [
    path('', include('data_collect.urls')),
]
