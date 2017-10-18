"""Blog view."""
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from blog.models import Blog


class IndexList(ListView):
    """Index list for blogs."""

    model = Blog
    context_object_name = 'blogs'


class BlogView(DetailView):
    """Blog view class."""

    model = Blog


class BlogCreate(CreateView):
    """Create blog post."""

    model = Blog
    fields = ['title', 'image', 'annotation', 'content', 'event', 'place']


class BlogUpdate(UpdateView):
    """Update blog post."""

    model = Blog
