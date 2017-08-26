from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.utils.text import slugify
from django.views.generic import TemplateView
from django.http.response import HttpResponseForbidden
from content.models import Blog, BlogPost

from django.contrib.auth.mixins import LoginRequiredMixin

from content.forms import BlogForm


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        ctx = super(HomeView, self).get_context_data(**kwargs)

        if self.request.user.is_authenticated():
            if Blog.objects.filter(owner=self.request.user).exists():
                ctx['has_blog'] = True
                blog = Blog.objects.get(owner=self.request.user)
                ctx['blog'] = blog
                ctx['blog_posts'] = BlogPost.objects.filter(blog=blog)

        return ctx