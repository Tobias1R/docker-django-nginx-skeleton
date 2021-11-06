"""{{ project_name }} URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/{{ docs_version }}/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

router = DefaultRouter()

urlpatterns = [
    #path(r'^admin/', admin.site.urls),
    re_path('^', include(router.urls)),

    path('openapi', get_schema_view(
        title="{{ project_name }}",
        description="api {{ project_name }}",
        version="1.0.0", 
    ), name='openapi-schema'),

    path('docs/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
        ), name='swagger-ui'),
]
