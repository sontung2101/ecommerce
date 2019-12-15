from django.urls import path, include
from user import views
from django.views.generic.base import TemplateView  # new

app_name = 'user'
urlpatterns = [
    # path('login', views.loginClass.as_view(), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),  # new
    path('accounts/signup', views.signup, name='signup'),  # new
    path('', TemplateView.as_view(template_name='home.html'), name='home'),  # new
]
