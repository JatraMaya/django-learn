from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.

def index(req):
    items = Item.objects.all()
    ctx = {'items': items}
    return render(req, 'food/index.html', ctx)

class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'items'

def item(req):
    return HttpResponse('<h1>This is the item view</h1>')

def detail(req, id):
    item = Item.objects.get(id=id)
    ctx = {'item': item}
    return render(req, 'food/details.html', ctx)

class FoodDetail(DetailView):
    model = Item
    template_name = 'food/details.html'

def create_item(req):
    form = ItemForm(req.POST or None)

    if form.is_valid():
        form.save()
        return redirect("food:Index")

    return render(req, 'food/item-form.html', {'form': form})

def edit_item(req, id):
    item = Item.objects.get(id=id)
    form = ItemForm(req.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect("food:Index")

    return render(req, 'food/item-form.html', {'form': form, 'item': item})

def delete_item(req, id):
    item = Item.objects.get(id=id)

    if req.method == 'POST':
        item.delete()
        return redirect("food:Index")

    return render(req, 'food/delete-item.html', {'item': item})

