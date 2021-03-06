from django.views.generic import TemplateView
from django.template import loader
from django.http import HttpResponseNotFound

from blog.models import Blog
from event.models import Event
from place.models import Place


class IndexView(TemplateView):
    """Index page."""

    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['blogs'] = Blog.objects.last_published()
        context['events'] = Event.objects.last_published()
        context['places'] = Place.objects.last_published()
        return context


def handler404(request):
    template = loader.get_template('404.html')
    return HttpResponseNotFound(template.render())