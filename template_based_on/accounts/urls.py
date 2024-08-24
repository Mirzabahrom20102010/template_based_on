from django.contrib.auth.views import (LoginView, LogoutView, PasswordChangeView,
                                       PasswordChangeDoneView,
                                       PasswordResetView, PasswordResetDoneView,
                                       PasswordResetConfirmView, PasswordResetCompleteView)
from django.urls import path
# from .views import user_register, edit_user, admin_page_view
from .views import SignUpView2, profile_view, EditUserView


app_name='accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login_page'),
    path('logout/', LogoutView.as_view(), name='log_out_page'),
    # path('signup/', user_register, name='user_register'),
    path('signup/', SignUpView2.as_view(), name='user_register'),
    # path('admin_page/', admin_page_view, name='admin_page'),

    # path('profile/edit/', edit_user, name='user_information'),
    path('profile/edit/', EditUserView.as_view(), name='edit_user_information'),
    path('user-profile/', profile_view, name="user_profile")
]
