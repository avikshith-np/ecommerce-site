from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product
from store.forms import ProductForm

def FrontPage(request):
    return render(request, 'frontpage.html', {'products': Product.objects.all})

def crud_operations(request):
    if request.method == 'POST':
        # Add Product
        if 'add_name' in request.POST and 'add_price' in request.POST:
            name = request.POST['add_name']
            price = request.POST['add_price']
            image = request.FILES.get('add_image')  # Get the uploaded image file
            product = Product(name=name, price=price, image=image)
            product.save()
            return redirect('crud_operations')
        
        # Edit Product
        if 'edit_select' in request.POST and 'edit_name' in request.POST and 'edit_price' in request.POST:
            product_id = request.POST['edit_select']
            name = request.POST['edit_name']
            price = request.POST['edit_price']
            image = request.FILES.get('edit_image')  # Get the uploaded image file
            product = get_object_or_404(Product, pk=product_id)
            product.name = name
            product.price = price
            if image:
                product.image = image  # Update the image only if a new image is provided
            product.save()
            return redirect('crud_operations')

        # Remove Product
        if 'remove_select' in request.POST:
            product_id = request.POST['remove_select']
            product = get_object_or_404(Product, pk=product_id)
            product.delete()
            return redirect('crud_operations')
    
    # Fetch all products
    products = Product.objects.all()
    form = ProductForm()
    return render(request, 'crud_operations.html', {'products': products, 'form': form})