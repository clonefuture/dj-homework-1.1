from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'books_list.html'
    sort = request.GET.get('sort')
    phones = Phone.objects.all()
    if sort == 'name':
        phones = phones.order_by('name')
    elif sort == 'min_price':
        phones = phones.order_by('price')
    elif sort == 'max_price':
        phones = phones.order_by('-price')
    else:
        phones = Phone.objects.all()
    return render(request, template, {'phones': phones})


def show_product(request, slug):
    template = 'product.html'
    ob_phone = Phone.objects.filter(slug=slug)
    phone = ob_phone.get()
    context = {
        'name': phone.name,
        'image': phone.image,
        'price': phone.price,
        'release_date': phone.release_date,
        'lte_exists': phone.lte_exists
        }
    return render(request, template, context)
