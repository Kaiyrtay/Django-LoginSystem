from django.urls import path
from django.urls.base import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
# static files
from django.conf import settings
from django.conf.urls.static import static
# local view
from . import views
from .forms import LoginForm
app_name = "main"
urlpatterns = [
    path('', TemplateView.as_view(template_name="main/home.html"), name="homepage"),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.CustomLoginView.as_view(redirect_authenticated_user=True,
         template_name='main/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='main/logout.html'), name='logout'),
    path('password-reset/', views.ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy(
        'main:password_reset_complete'), template_name='main/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='main/password_reset_complete.html'), name='password_reset_complete'),
    path('profile/', views.profile, name='users-profile'),
    path('password-change/', views.ChangePasswordView.as_view(),
         name='password_change'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
