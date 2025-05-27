from django.shortcuts import render, get_object_or_404
from .models import Module, Menu


# Create your views here.

def home(request): 
    menus = Menu.objects.all()

    return render(request, 'home.html', {'menus': menus})

def menu_detail(request, id):
    menu = get_object_or_404(Menu, id=id)
    modules = menu.modules.filter(is_active=True).order_by('order')
    menus = Menu.objects.all() 
    return render(request, 'home.html', {
        'menus': menus,       
        'modules': modules, 
    })
