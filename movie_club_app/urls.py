from django.urls import path
from . import views, views_users, views_meetings, views_films, views_theatres

from django.contrib.auth import views as auth_views

app_name = 'movie_club_app'

urlpatterns = [
    path('', views.homepage, name='homepage'),

    path('user/profile/<int:user_pk>/', views_users.user_profile, name='user_profile'),
    path('user/profile/', views_users.my_user_profile, name='my_user_profile'),
    path('user/profile/edit', views_users.edit_user_profile, name='edit_user_profile'),
    path('user/password/', views_users.change_password, name='change_password'),

    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/', views_users.register, name='register'),

    path('films/list/', views_films.currently_out, name='currently_out'),
]