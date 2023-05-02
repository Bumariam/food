from django.shortcuts import render, get_object_or_404
from .models import Restaurant, FastFood, Caffeine, MenuItem



def home(request):
    caffeine_list = Caffeine.objects.all()
    fastfood_list = FastFood.objects.all()
    restaurant_list = Restaurant.objects.all()
    context = {
        'caffeine_list': caffeine_list,
        'fastfood_list': fastfood_list,
        'restaurant_list': restaurant_list,
    }
    return render(request, 'home.html', context)


def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    context = {'restaurants': restaurants}
    return render(request, 'restaurant_list.html', context)

def restaurant_detail(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    return render(request, 'restaurant_detail.html', {'restaurant': restaurant})

def fastfood_list(request):
    fastfoods = FastFood.objects.all()
    context = {'fastfoods': fastfoods}
    return render(request, 'fastfood_list.html', context)

def fastfood_detail(request, pk):
    fastfood = get_object_or_404(FastFood, pk=pk)
    return render(request, 'fastfood_detail.html', {'fastfood': fastfood})

def caffeine_list(request):
    caffeine = Caffeine.objects.all()
    context = {'caffeine': caffeine}
    return render(request, 'caffeine_list.html', context)

def caffeine_detail(request, pk):
    caffeine = get_object_or_404(Caffeine, pk=pk)
    context = {'caffeine': caffeine}
    return render(request, 'caffeine_detail.html', context)
