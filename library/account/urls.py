from django.urls import path

from library.account import views

app_name = 'account'

urlpatterns = [
    path('register/', views.login, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('my_rentals/', views.login, name='my_rentals'),
]
