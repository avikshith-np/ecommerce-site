from django.shortcuts import render, get_object_or_404, redirect
#from django.contrib.auth.decorators import login_required

from .models import Product
from .forms import ProductForm


def cart(request):
    cart = request.session.get('cart', {})
    product_ids = cart.keys()
    products = Product.objects.filter(id__in=product_ids)
    total_quantity = sum(cart.values())
    total_price = sum(product.price * quantity for product, quantity in zip(products, cart.values()))
    print("Cart: ", cart)

    return render(request, 'cart.html', {'products': products, 'total_quantity': total_quantity, 'total_price': total_price})

def add_to_cart(request, product_id):
    #product = get_object_or_404(Product, pk=product_id)
    cart = request.session.get('cart', {})
    cart[product_id] = cart.get(product_id, 0) + 1
    request.session['cart'] = cart
    return redirect('frontpage')

def update_cart(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    cart = request.session.get('cart', {})

    quantity = int(request.POST.get('quantity', 0))
    if quantity > 0:
        cart[product_id] = quantity
    else:
        del cart[product_id]

    request.session['cart'] = cart

    return redirect('cart')

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    product = get_object_or_404(Product, pk=product_id)
    print("Cart: ", cart)
    product_id = str(product_id)
    if product_id in cart:
        print("Yes. In Cart")
        del cart[product_id]
        print("Deleted", product.name)
        request.session['cart'] = cart
    else:
        print("No. Not in Cart")
    return redirect('cart')

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cart')
    else:
        form = ProductForm()
    return render(request, 'store/add_product.html', {'form': form})

def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('cart')
    else:
        form = ProductForm(instance=product)
    return render(request, 'store/edit_product.html', {'form': form, 'product': product})

def remove_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('cart')
    return render(request, 'store/remove_product.html', {'product': product})