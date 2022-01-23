from django.contrib import admin
from django.urls import path, include
from frexco.views import FruitsViewSet, RegionsViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('fruit', FruitsViewSet, basename='Fruit')
router.register('region', RegionsViewSet, basename='Region')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
