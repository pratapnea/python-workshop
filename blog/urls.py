from django.conf.urls import url, include
from .views import post_list, post_new

urlpatterns = [
	url(r'^$', post_list, name = 'post_list'),
	url(r'^new-post/$', post_new, name = 'post_new'),
	url(r'^post_details/?P<pk>\d+)/$', post_detail, name = 'post_detail'),
]