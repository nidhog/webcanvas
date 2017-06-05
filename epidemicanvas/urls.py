from django.conf.urls import url, include

from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'actions', views.ActionViewSet)
router.register(r'artists', views.ArtistViewSet)
router.register(r'sessions', views.SessionViewSet)
router.register(r'contributions', views.ContributionViewSet)

urlpatterns = [
    url('api/v1/', include(router.urls)),
    url('api/v1/update_session_image', views.update_image, name='update_session_image'),
    url('api/v1/get_actions', views.get_actions, name='get_actions'),
    url('api/v1/update_session/(?P<pk>\d+)/$', views.SessionUpdateName.as_view(), name='update_session'),
    url(r'^/', views.index, name='index'),
]
