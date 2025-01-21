from django.http import HttpResponse
from django.views.generic import TemplateView


def index(request):
    return HttpResponse("Hello, world")

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):  
    template_name = 'about.html'
