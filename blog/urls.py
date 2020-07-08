from django.urls import path

from .views import PostList, PostDetail
app_name = 'blog'
urlpatterns = [
    path('list/', PostList.as_view(), name='list'),
    path('post/<int:pk>', PostDetail.as_view(), name='detail')

]
