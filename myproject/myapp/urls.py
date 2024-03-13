# myapp/urls.py

from django.urls import path
from .views import index, login,maincanteen,misccanteen,signup

urlpatterns = [
    path('', index, name='index'),
    path('login.html/', login, name='login'),
    path('maincanteen.html/', maincanteen, name='maincanteen'),
    path('misccanteen.html/', misccanteen, name='misccanteen'),
    path('index.html/',index, name='index'),
    path('signup.html/', signup, name='signup'),
]
