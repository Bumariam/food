from django.shortcuts import render, get_object_or_404
from .models import Restaurant, FastFood, Caffeine, MenuItem

# view
def home(request):
    caffeine_list = Caffeine.objects.all()
    fastfood_list = FastFood.objects.all()
    restaurant_list = Restaurant.objects.all()
    menu_items = MenuItem.objects.all()
    context = {
        'caffeine_list': caffeine_list,
        'caffeine_detail': caffeine_detail,
        'fastfood_list': fastfood_list,
        'restaurant_list': restaurant_list,
        'menu_items': menu_items,
    }
    return render(request, 'home.html', context)


def restaurant_list(request):
    restaurant = Restaurant.objects.all()
    context = {'restaurant': restaurant}
    return render(request, 'restaurant_list.html', context)




def restaurant_detail(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    menu_items = MenuItem.objects.filter(restaurant=restaurant)
    context = {
        'restaurant': restaurant,
        'menu_items': menu_items,
    }
    return render(request, 'restaurant_detail.html', context)


# def restaurant_detail(request, pk):
#     restaurant = get_object_or_404(Restaurant, pk=pk)
#     return render(request, 'restaurant_detail.html', {'restaurant': restaurant})
#

def fastfood_list(request):
    fastfood = FastFood.objects.all()
    context = {'fastfood': fastfood}
    return render(request, 'fastfood_list.html', context)


def fastfood_detail(request, pk):
    fastfood = get_object_or_404(FastFood, pk=pk)
    menu_items = MenuItem.objects.filter(fastfood=fastfood)
    context = {
        'fastfood': fastfood,
        'menu_items': menu_items,
    }
    return render(request, 'fastfood_detail.html', context)





def caffeine_list(request):
    caffeine = Caffeine.objects.all()
    context = {'caffeine': caffeine}
    return render(request, 'caffeine_list.html', context)


def caffeine_detail(request, pk):
    caffeine = get_object_or_404(Caffeine, pk=pk)
    menu_items = MenuItem.objects.filter(caffeine=caffeine)
    context = {
        'caffeine': caffeine,
        'menu_items': menu_items,
    }
    return render(request, 'caffeine_detail.html', context)




