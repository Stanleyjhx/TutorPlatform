"""TutorPlatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url, include
from django.urls import path

from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    url('admin/', admin.site.urls),
    path('api-user/',include('person.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('swagger-docs/', get_swagger_view(title='TutorPlatform API')),
    path('docs/', include_docs_urls(title='TutorPlatform API', authentication_classes=[], permission_classes=[])),

]
