from django.urls import path
from users.views import UserListView
from authentication.views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='user-login'),
    path('', UserListView.as_view(), name='user-list'),
]