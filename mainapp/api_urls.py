from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'camps', views.RescueCampViewSet)
router.register(r'persons', views.PersonViewSet)


urlpatterns = [
    path('camplist/', views.CampList.as_view(), name='api_camplist'),
]

urlpatterns += router.urls

