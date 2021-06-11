from django.shortcuts import render
from .models import Product
from .forms import ProductForm
# Create your views here.

def render_initial_data(request):
    initial_data = {
        'title' : 'initial title',
        'description' : 'initital description',
        'price' : 0.99
    }
    form = ProductForm(request.POST or None, initial=initial_data)
    context = { 'form' : form }
    return render(request, 'products/product_create.html', context)

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = { 'form': form }
    return render(request, 'products/product_create.html', context)
 
def product_detail_view(request, my_id):
    obj = Product.objects.get(id=my_id)
    context = {
        'object' : obj
    }
    return render(request, 'products/product_detail.html', context)

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list' : queryset
    }
    return render(request, 'products/product_list.html', context)
