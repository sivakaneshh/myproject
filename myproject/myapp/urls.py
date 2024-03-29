# myapp/urls.py

from django.urls import path
from .views import home, user_login,maincanteen,misccanteen,signup,user_logout,main_checkout, misc_checkout,conformation,addmin,inventory,addmin_login,additems,payment_failed

urlpatterns = [
    path('', home, name='home'),
    path('login/', user_login, name='login'),
    path('maincanteen/', maincanteen, name='maincanteen'),
    path('misccanteen/', misccanteen, name='misccanteen'),
    path('index/',home, name='index'),
    path('signup/', signup, name='signup'),
    path('logout/', user_logout, name="logout"),
    path('main_checkout/', main_checkout, name="maincheckout"),
    path('misc_checkout/', misc_checkout, name="misccheckout"),
    path('conformation/',conformation, name='conformation'),
    path('inventory/',inventory,name='inventory'),
    path('addmin/',addmin,name='addmin'),
    path('addmin_login/', addmin_login, name="addmin_login"),
    path('additems/', additems, name="additems"),
    path('payment_failed/', payment_failed, name="payment_failed"),
]
