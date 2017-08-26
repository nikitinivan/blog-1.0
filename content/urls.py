from django.conf.urls import url
from content.views import NewBlogView, UpdateBlogView, NewBlogPostView, UpdateBlogPostView, \
    BlogPostDetailsView

urlpatterns = [
    url(r'^new/$', NewBlogView.as_view(), name='new_blog'),
    url(r'^(?P<pk>\d+)/update/$', UpdateBlogView.as_view(), name='update_blog'),
    url(r'post/new/$', NewBlogPostView.as_view(), name='new_blog_post'),
    url(r'post/(?P<pk>\d+)/update/$', UpdateBlogPostView.as_view(), name='update_blog_post'),
    url(r'post/(?P<pk>\d+)/$', BlogPostDetailsView.as_view(), name='blog_post_details'),
]

