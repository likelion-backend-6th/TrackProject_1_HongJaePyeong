from django.urls import path

from library.books import views

app_name = 'books'

urlpatterns = [
    path('<int:id>/', views.book, name='book'),
    path('<int:id>/rent/', views.rent, name='rent'),
]