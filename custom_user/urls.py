from django.urls import path
from . import views
#from . forms import LoginForm

app_name = 'users'
urlpatterns = [
    path('registration/', views.Registration.as_view(), name='registration'),
    path('login/', views.NewLoginView.as_view(), name='login'),
    path('users_list/', views.UserListView.as_view(), name='user_list'),
]