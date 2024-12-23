"""
URL configuration for MituketAI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import ItemViewSet, RegisterViewSet, RegisterRankingViewSet,RegisterResultViewSet
from api.views import test_endpoint

# DefaultRouterを使用してルートを自動生成
router = DefaultRouter()
router.register(r'items', ItemViewSet, basename='item')
router.register(r'registers', RegisterViewSet, basename='register')
router.register(r'rankings', RegisterRankingViewSet, basename='register_ranking')  # 異なるbasenameを指定
router.register(r'results', RegisterResultViewSet, basename='result') 

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),  # routerのURLを含める
    path('api/test/', test_endpoint, name='test-endpoint'), # 通信テスト用
]