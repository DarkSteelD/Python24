from django.shortcuts import render
from models import restaurant
def restaurants_list(request):
    restaurants = Restaurant.objects.all()
    context = {
        'restaurants': restaurants,
    }
    return render(request, 'restaurants/list.html', context)
def restaurant_detail(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    context = {
        'restaurant': restaurant,
    }
    return render(request, 'restaurants/detail.html', context)
def restaurant_create(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('restaurants_list')
    else:
        form = RestaurantForm()
    context = {
        'form': form,
    }
    return render(request, 'restaurants/create.html', context)

def restaurant_edit(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    if request.method == 'POST':
        form = RestaurantForm(request.POST, instance=restaurant)
        if form.is_valid():
            form.save()
            return redirect('restaurants_list')
    else:
        form = RestaurantForm(instance=restaurant)
    context = {
        'form': form,
    }
    return render(request, 'restaurants/edit.html', context)

def restaurant_delete(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    restaurant.delete()
    return redirect('restaurants_list')