from django.urls import path, include
from user import views
from django.views.generic.base import TemplateView  # new
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
app_name = 'user'
urlpatterns = [
    path('order-management', views.orderManagement.as_view(), name='order-management'),
    path('accounts/', include('django.contrib.auth.urls')),  # new
    path('accounts/signup', views.signup, name='signup'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),  # new
    path('editProfile', views.editProfile.as_view(), name='edit-profile'),
    path('password-change/', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('user:password_change_done')), name='password_change'),

]
