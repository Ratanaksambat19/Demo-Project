from django.urls import path
from useracc import views

app_name = 'useracc'

urlpatterns = [
    path('movie/', views.movie, name = 'movie'),
    path('soccer/', views.soccer, name = 'soccer'),
    path('travel/', views.travel, name = 'travel')
]