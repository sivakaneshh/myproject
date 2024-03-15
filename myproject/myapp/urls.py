# myapp/urls.py

from django.urls import path
from .views import home, user_login,maincanteen,misccanteen,signup,user_logout,checkout,conformation,addmin,inventory,addmin_login,additems

urlpatterns = [
    path('', home, name='home'),
    path('login.html/', user_login, name='login'),
    path('maincanteen.html/', maincanteen, name='maincanteen'),
    path('misccanteen.html/', misccanteen, name='misccanteen'),
    path('index.html/',home, name='index'),
    path('signup.html/', signup, name='signup'),
    path('logout.html/', user_logout, name="logout"),
    path('checkout.html/', checkout, name="checkout"),
    path('conformation.html/',conformation, name='conformation'),
    path('inventory.html/',inventory,name='inventory'),
    path('addmin.html/',addmin,name='addmin'),
    path('addmin_login', addmin_login, name="addmin_login"),
    path('additems', additems, name="additems")
]
