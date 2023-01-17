"""admin_sportbot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import SimpleRouter

from tgbot.views import home_page
from django.views.generic.base import TemplateView
router = SimpleRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home_page, name='home'),
    path("home", TemplateView.as_view(template_name='home.html'), name='home'),
    path("index", TemplateView.as_view(template_name='index.html'), name='index'),
    path("statistics", TemplateView.as_view(template_name='statistics.html'), name='statistics'),
    path("users", TemplateView.as_view(template_name='users.html'), name='users')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += router.urls
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


