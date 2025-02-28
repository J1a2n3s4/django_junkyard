from django.shortcuts import render
from .models import product
from django.http import HttpResponse
from django.template import loader

def main(request):
  template = loader.get_template('main.html')
  content = {
    "products": product.objects.all().values()
  }
  return HttpResponse(template.render(content, request))