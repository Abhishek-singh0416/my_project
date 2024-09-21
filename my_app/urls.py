from django.contrib import admin
from django.urls import path , include
from my_app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path("",views.index,name="index"),
    path("sign_in",views.sign_in,name="sign_in"),
    # path("account_view",views.account_view,name="account_view"),
    # path("back",views.back,name="back"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    

    path('login/', views.login_view, name='login'),

]
