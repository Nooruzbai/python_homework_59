from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts.user.register import RegisterView
from accounts.user.views import UserProfileView, UserListView

app_name = 'accounts'


urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name="registration"),
    path("profile/<int:pk>/", UserProfileView.as_view(), name="user_profile_view"),
    path('user/list/', UserListView.as_view(), name='user_list_view')
]
