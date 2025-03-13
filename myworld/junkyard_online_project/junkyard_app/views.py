from django.shortcuts import render
from .models import product, kontakt
from django.http import HttpResponse
from django.template import loader

def main(request):
  template = loader.get_template('main.html')
  content = {
    "products": product.objects.all().values()
  }
  return HttpResponse(template.render(content, request))

def product_page(request, name_url):
  if request.method == "POST":
    telefon = request.POST.get('telefon')
    mail = request.POST.get('mail')
    kontakt(tel = telefon, email = mail).save()

  template = loader.get_template('main.html')
  content = {
    "x": product.objects.get(link = name_url)
  }
  return render(request, 'product.html', context=content)