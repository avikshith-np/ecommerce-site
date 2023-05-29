from django.shortcuts import render

from store.models import Product

def FrontPage(request):
    return render(request, 'frontpage.html', {'products': Product.objects.all})