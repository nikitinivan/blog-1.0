from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.utils.text import slugify
from django.views.generic import CreateView, UpdateView, DetailView
from django.http.response import HttpResponseForbidden
from content.models import Blog, BlogPost

from django.contrib.auth.mixins import LoginRequiredMixin

from content.forms import BlogForm, BlogPostForm

class NewBlogView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    form_class = BlogForm
    template_name = 'blog_settings.html'

    def form_valid(self, form):
        blog_obj = form.save(commit=False)
        blog_obj.owner = self.request.user
        blog_obj.slug = slugify(blog_obj.title)

        blog_obj.save()
        return HttpResponseRedirect(reverse('home'))

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if Blog.objects.filter(owner=user).exists():
            return HttpResponseForbidden('You can no create more than one blogs per account')
        else:
            return super(NewBlogView, self).dispatch(request, *args, **kwargs)



class UpdateBlogView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    form_class = BlogForm
    template_name = 'blog_settings.html'
    success_url = '/'
    model = Blog


class NewBlogPostView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    form_class = BlogPostForm
    template_name = 'blog_post.html'

    def form_valid(self, form):
        blog_post_obj = form.save(commit=False)
        blog_post_obj.blog = Blog.objects.get(owner=self.request.user)
        blog_post_obj.slug = slugify(blog_post_obj.title)
        blog_post_obj.is_published = True

        blog_post_obj.save()

        return HttpResponseRedirect(reverse('home'))


class UpdateBlogPostView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    form_class = BlogPostForm
    template_name = 'blog_post.html'
    success_url = '/'
    model = BlogPost

    def get_queryset(self):
        queryset = super(UpdateBlogPostView, self).get_queryset()
        return queryset.filter(blog__owner=self.request.user)



class BlogPostDetailsView(DetailView):
    model = BlogPost
    template_name = 'blog_post_detail.html'

