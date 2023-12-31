"""
URL configuration for craftelectro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from craft_app import views
from django.urls import path
from craft_app.views import page_one, page_two, page_three
from django.views.generic import TemplateView  # Добавьте импорт TemplateView


urlpatterns = [
    path('', page_one, name='page_one'),
    path('about/', page_two, name='page_two'),
    path('contact/', page_three, name='page_three'),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain'))
    ]
