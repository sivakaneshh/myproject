# myapp/urls.py

from django.urls import path
from .views import home, user_login,maincanteen,misccanteen,signup,user_logout,conformation,addmin,inventory,addmin_login,additems,maincheckout,misccheckout

urlpatterns = [
    path('', home, name='home'),
    path('login.html/', user_login, name='login'),
    path('maincanteen.html/', maincanteen, name='maincanteen'),
    path('misccanteen.html/', misccanteen, name='misccanteen'),
    path('index.html/',home, name='index'),
    path('signup.html/', signup, name='signup'),
    path('logout.html/', user_logout, name="logout"),
    path('conformation.html/',conformation, name='conformation'),
    path('inventory.html/',inventory,name='inventory'),
    path('addmin.html/',addmin,name='addmin'),
    path('addmin_login', addmin_login, name="addmin_login"),
    path('additems.html', additems, name="additems"),
    path('maincheckout.html', maincheckout, name='maincheckout'),
    path('miscchekout.html', misccheckout, name='misccheckout')

]
