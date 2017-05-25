from django.conf.urls import url, include

from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'sessions', views.SessionViewSet)
router.register(r'artists', views.ArtistViewSet)

urlpatterns = [
    url('api/v1/', include(router.urls)),
    url(r'^', views.index, name='index'),
]
