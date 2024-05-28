from django.shortcuts import render
from .models import Category, Product
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
# Create your views here.


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list_product.html',
                  {'category': category, 'categories': categories, 'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    return render(request, 'shop/product/detail.html', {'product': product})


# class ProductList(ListView):
#     model = Product
#     template_name = 'shop/product/list.html'
#     context_object_name = 'products'
#
#     def get_queryset(self):
#         return Product.objects.all()
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(ProductList, self).get_context_data(*args, **kwargs)
#         context['categories'] = Category.objects.all()
#         return context
