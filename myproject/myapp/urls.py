# myapp/urls.py

from django.urls import path
from .views import home, user_login,maincanteen,misccanteen,signup,user_logout,maincheckout, misccheckout,conformation,addmin,inventory,addmin_login,additems

urlpatterns = [
    path('', home, name='home'),
    path('login/', user_login, name='login'),
    path('maincanteen/', maincanteen, name='maincanteen'),
    path('misccanteen/', misccanteen, name='misccanteen'),
    path('index/',home, name='index'),
    path('signup/', signup, name='signup'),
    path('logout/', user_logout, name="logout"),
    path('main_checkout/', maincheckout, name="main_checkout"),
    path('misc_checkout/', misccheckout, name="misc_checkout"),
    path('conformation/',conformation, name='conformation'),
    path('inventory/',inventory,name='inventory'),
    path('addmin/',addmin,name='addmin'),
    path('addmin_login/', addmin_login, name="addmin_login"),
    path('additems/', additems, name="additems")
]
