from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.views.generic.base import TemplateView
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('home/', TemplateView.as_view(template_name='home.html'), name='home'),
    path('create_account', views.SignUpView.as_view(), name='create_account'),
    path('',include('calapp.urls')),
]