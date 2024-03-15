# myapp/urls.py

from django.urls import path
from .views import index, user_login,maincanteen,misccanteen,signup,user_logout,checkout
urlpatterns = [
    path('', index, name='index'),
    path('login.html/', user_login, name='login'),
    path('maincanteen.html/', maincanteen, name='maincanteen'),
    path('misccanteen.html/', misccanteen, name='misccanteen'),
    path('index.html/',index, name='index'),
    path('signup.html/', signup, name='signup'),
    path('logout.html/', user_logout, name="logout"),
    path('checkout.html/', checkout, name="checkout"),
]
