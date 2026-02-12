from django.urls import path

from accounts import views as vw

urlpatterns = [
    path(
        'accounts/login/',
        vw.CustomLoginView.as_view(),
        name='login'
    ),
    path(
        'accounts/logout/',
        vw.CustomLogoutView.as_view(),
        name='logout'
    ),
    path(
        'accounts/password_change/',
        vw.CustomPasswordChangeView.as_view(),
        name='password_change'
    ),
    path(
        'accounts/password_change/done/',
        vw.CustomPasswordChangeDoneView.as_view(),
        name='password_change_done'
    ),
    path(
        'accounts/password_reset/',
        vw.CustomPasswordResetView.as_view(),
        name='password_reset'
    ),
    path(
        'accounts/password_reset/done/',
        vw.CustomPasswordResetDoneView.as_view(),
        name='password_reset_done'
    ),
    path(
        'accounts/reset/<uidb64>/<token>/',
        vw.CustomPasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),
    path(
        'accounts/reset/done/',
        vw.CustomPasswordResetCompleteView.as_view(),
        name='password_reset_complete'
    ),
]
