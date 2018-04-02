from django.conf.urls import url,include
from . import views
from .feed import PostsFeed

urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^post_list/$', views.post_list_view, name='post_list_view'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$', views.post_detail_view, name='post_detail_view'),
    url(r'^feed/$', PostsFeed(), name='post_feed'),
    #url(r'^$',views.main_page),
    #url(r'^login/$',include( 'django.contrib.auth.views.login')),
    #url(r'^edit-post/(?P<pk>\d+)/$', views.edit_post, name='edit_post'),
    url(r'^new-post/$', views.new_post, name='new_post'),
]
