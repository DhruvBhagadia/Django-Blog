from django.conf.urls import url
from . import views
from .feed import PostsFeed
from django.contrib.auth import views as auth_views
app_name='blog'

urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^post_list/$', views.post_list_view, name='post_list_view'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
        views.post_detail_view, name='post_detail_view'),
    url(r'^login/$', auth_views.login,{'template_name':'blog/post/login.html'}, name='login'),
    #url(r'^$', views.post_list_view, name='post_list_view'),
    url(r'^new-post/$', views.new_post),
    url(r'^delete_post/(?P<post>[-\w]+)/$',views.delete_post, name='delete_post'),
    url(r'^feed/$', PostsFeed(), name='post_feed'),
    url(r'^signup/$', views.signup, name='signup'),
]
