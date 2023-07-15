"""
URL configuration for Books_Library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import welcome_page, show_books, inactive_books, single_book, add_book, update_book, book_hard_delete, book_soft_delete, form_view
from user_app import views

urlpatterns = [
    path('books/admin/', admin.site.urls),
    path('books/home/', welcome_page, name="home_page"),
    path('books/show_books/', show_books, name="show_books"),
    path('books/inactive_books/', inactive_books, name="inactive_books"),
    path('books/single_book/<int:bid>/', single_book, name="single_book"),
    path('books/add_book/', add_book, name="add_book"),
    path('books/update_book/<int:bid>/', update_book, name="update_book"),
    path('books/hard_delete/<int:bid>/', book_hard_delete, name="hard_delete"),
    path('books/soft_delete/<int:bid>/', book_soft_delete, name="soft_delete"),
    path('books/form_view/', form_view, name="form_view"),
    
    # User_app urls:
    path("user/signup/", views.user_signup, name="user_signup"),
    path("user/login/", views.user_login, name="user_login"),
    path("user/logout/", views.user_logout, name="user_logout"),
]
