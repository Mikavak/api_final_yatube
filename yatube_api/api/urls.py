from rest_framework.routers import SimpleRouter
from .views import PostList, GroupList, CommentList
from django.urls import include, path


router_v1 = SimpleRouter()
router_v1.register('v1/posts', PostList)
router_v1.register('v1/groups', GroupList)
router_v1.register(
    r'v1/posts/(?P<post_id>[\d]+)/comments', CommentList,
    basename='comments')


urlpatterns = [
    path('', include(router_v1.urls))
    ]
