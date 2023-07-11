from django.urls import path
from .views import *

urlpatterns = [
    path('', Register, name='register'),
    path('login/', Login, name='login'),
    path('overview/', Overview, name='overview'),
    path('barthai/', BarThai, name='barthai'),
    path('bareng/', BarEng, name='bareng'),
    path('editbarthai/', EditBarThai, name='editbarthai'),
    path('editbareng/', EditBarEng, name='editbareng'),
    path('newbarthai/', NewBarThai, name='newbarthai'),
    path('newbareng/', NewBarEng, name='newbareng'),
    path('tesst/', Test, name='test'),

]