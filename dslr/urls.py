from rest_framework.routers import DefaultRouter
from dslr import views
from django.urls import include, path

router = DefaultRouter()
router.register('readyonly/post', views.ReadOnlyPostViewSet)
router.register('post', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls))
]