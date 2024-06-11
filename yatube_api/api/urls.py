from rest_framework.routers import SimpleRouter
from .views import PostList, GroupList
from django.urls import include, path


router_v1 = SimpleRouter()
router_v1.register('v1/posts', PostList)
router_v1.register('v1/groups', GroupList)


urlpatterns = [
    path('', include(router_v1.urls))
    ]
