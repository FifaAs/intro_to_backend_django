from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.context_processors import auth
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from .models import Post, Thread
from .forms import PostForm

@login_required
def index_category(request):
    if request.method == 'GET':
        form = PostForm()
        categories = Category.objects.all()
        return render(request, 'shop/index.html',
                      {
                          'categories': categories,
                          'form': form
                      })
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')


@login_required
@permission_required('shop.change_category')
def update_category(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == 'GET':
        form = CategoryForm(instance=category)
        return render(request, 'shop/update_category.html',
                      {
                          'category': category,
                          'form': form
                      })
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
        return redirect('/')


@login_required
@permission_required('shop.delete_category')
def delete_category(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
        category.delete()
        return redirect('/')
    except Product.DoesNotExist as e:
        return redirect('index')


@login_required
def category_details(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == 'GET':
        form = ProductForm()
        products = Product.objects.filter(category=category_id)
        return render(request, 'posts/category_details.html',
                      {
                          'products': products,
                          'category': category,
                          'form': form
                      })
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            price = form.cleaned_data.get('price')
            amount = form.cleaned_data.get('amount')
            description = form.cleaned_data.get('description')
            image = form.cleaned_data.get('image')
            product = Product(
                name=name,
                price=price,
                amount=amount,
                description=description,
                category=Category.objects.get(id=category_id),
            )
            product.image.save(image.name, image)
            product.save()
        return redirect('category_details', category_id)


@login_required
@permission_required('shop.change_product')
def update_product(request, category_id, product_id):
    category = Category.objects.get(id=category_id)
    product = Product.objects.get(id=product_id)
    if request.method == 'GET':
        form = ProductForm(instance=product)
        return render(request, 'shop/update_product.html',
                      {
                          'product': product,
                          'category': category,
                          'form': form
                      })
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
        return redirect('category_details', category_id)


@login_required
def products_details(request, category_id, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'posts/post-details.html', {'product': product})


@login_required
@permission_required('shop.delete_product')
def delete_product(request, category_id, product_id):
    try:
        product = Product.objects.get(id=product_id)
        product.delete()
        return redirect('category_details', category_id)
    except Product.DoesNotExist as e:
        return redirect('index')


def log_in(request):
    if request.method == 'POST':
        redirect_url = request.GET.get('next', '/')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(redirect_url)
    return render(request, "auth/login.html")


@login_required
def log_out(request):
    logout(request)
    return redirect("index")