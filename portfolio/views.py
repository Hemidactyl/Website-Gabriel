from django.shortcuts import render
from django.views import generic

class PortfolioView(generic.TemplateView):
    template_name = 'portfolio/portfolio.html'
