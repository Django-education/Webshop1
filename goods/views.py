from django.shortcuts import render
from .models import Product
<<<<<<< HEAD
from django.core.paginator import Paginator


def index(request):
    size_const = 6
    all_products = Product.objects.all()

    paginator = Paginator(all_products, size_const)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

=======


def index(request):
>>>>>>> 9800cbb47d5bb33a0326cecb50d2a383689eee45
    return render(request, 'goods/index.html', context={
        'page_name': 'Каталог',
        'page_app': 'goods',
        'page_view': 'index',
<<<<<<< HEAD
        'products': page_obj
    })
=======
        'all_products': Product.objects.all()
    })
>>>>>>> 9800cbb47d5bb33a0326cecb50d2a383689eee45
