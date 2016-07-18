from django.shortcuts import render
from .models import Category, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    all_cats = Category.objects.all()
    context = {
        'all_cats': all_cats,
    }
    return render(request, 'shop/index.html', context)


def cat_detail(request, category_id):
    products_list = Product.objects.filter(category=category_id).order_by("-timestamp")
    category = Category.objects.get(pk=category_id)

    paginator = Paginator(products_list, 6)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)

    context = {
        'products': products,
        'products_num': products_list.count(),
        'category': category,
        'num_pages': range(1, products.paginator.num_pages+1)
    }
    return render(request, 'shop/cat_detail.html', context)


def pro_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    context = {
        'product': product,
    }
    return render(request, 'shop/pro_detail.html', context)

# def index(request):
#     return render(request, 'shop/base.html', {})
