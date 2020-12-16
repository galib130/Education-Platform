from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name='index.html'

class InPage(TemplateView):
    template_name='in.html'


class OutPage(TemplateView):
    template_name='out.html'




