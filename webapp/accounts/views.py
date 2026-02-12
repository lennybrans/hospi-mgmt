from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def profile(request):
    return render(request, 'profile.html')


class CustomLoginView(auth_views.LoginView):
    """Custom login view."""
    template_name = 'login.html'


class CustomLogoutView(auth_views.LogoutView):
    """Custom logout view."""
    template_name = 'logged_out.html'


class CustomPasswordChangeView(auth_views.PasswordChangeView):
    """Custom password change view."""
    template_name = 'password_change_form.html'


class CustomPasswordChangeDoneView(auth_views.PasswordChangeDoneView):
    """Custom password change done view."""
    template_name = 'password_change_done.html'


class CustomPasswordResetView(auth_views.PasswordResetView):
    """Custom password reset view."""
    template_name = 'password_reset_form.html'


class CustomPasswordResetDoneView(auth_views.PasswordResetDoneView):
    """Custom password reset done view."""
    template_name = 'password_reset_done.html'


class CustomPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    """Custom password reset confirm view."""
    template_name = 'password_reset_confirm.html'


class CustomPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    """Custom password reset complete view."""
    template_name = 'password_reset_complete.html'
