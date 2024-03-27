from django.urls import path
from . import views

urlpatterns = [
    path('user/create/', views.UserCreateView.as_view(), name='user_create'),
    path('user/<int:pk>/update/', views.UserUpdateView.as_view(), name='user_update'),
    path('user/list/', views.user_list, name='user_list'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
]
