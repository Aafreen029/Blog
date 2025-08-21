
from django.urls import path
from Accounts import views

urlpatterns = [
    
    path('signup/',views.signup, name='signup'),
    path('login/',views.loginViews, name='login'),
    path('logout/',views.logoutViews, name='logout'),
    
]
