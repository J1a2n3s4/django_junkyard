from django.shortcuts import render
from .models import product
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
def main(request):
  template = loader.get_template('main.html')
  content = {
    "products": product.objects.all().values()
  }
  return HttpResponse(template.render(content, request))

def login_page(request):
  template = loader.get_template('login.html')
  content = {}
  if request.method == "POST":
    user_name = request.POST["user"]
    password = request.POST["password"]
    user = authenticate(request, username=user_name, password=password)
    if user is not None:
        login(request, user)
        return redirect("/")
    else:
        content["error"] = "Niezgodny login lub brak zalogowanego użytkownika"
  return HttpResponse(template.render(content, request))


def register_redirect(one, two):
  redirect("register")

def register(request):
  template = loader.get_template('register.html')
  content = {}
  if request.method == "POST":
    name = request.POST["name"]
    mail = request.POST["mail"]
    password1 = request.POST["password"]
    password2 = request.POST["password2"]
    content["error"] = ""
    if not User.objects.filter(username = name).exists() and password1 == password2:
      user = User.objects.create_user(name,mail,password1)
      user.save()
      content["error"] = ""
      return redirect("/login")
    else:
        content["error"] = "Invalid register."
  return HttpResponse(template.render(content, request))


def product_page(request, name_url):
  content = {
    "x": product.objects.get(link = name_url)
  }
  return render(request, 'product.html', context=content)

def buy(request, name_url):
  if request.user.is_authenticated:
    content = {
    "x": product.objects.get(link = name_url)
    }
    if request.POST.get('usun') == 'true':
      product.objects.get(link = name_url).delete()

      return redirect('/')
    return render(request, 'buy.html', context=content)
  else:
    return render(request, 'login.html')

