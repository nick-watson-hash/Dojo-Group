from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.db.models import Q
import bcrypt


# Category View
# Retrieve Category objects
def allProdCat(request, c_slug=None):
    c_page = None
    products_list = None
    if c_slug != None:
        c_page = get_object_or_404(Category, slug = c_slug)
        products_list = Product.objects.filter(category = c_page, available = True)
    else:
        products_list = Product.objects.all().filter(available = True)
    # PAGINATION web pages for products
    paginator = Paginator(products_list, 3)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)
    # Checks for user_id in request.session
    login_check = ""
    if 'user_id' in request.session:
        login_check = User.objects.get(id=request.session['user_id'])
    context = {
        'category':c_page,
        'products':products,
        'current_user':login_check
    }
    return render(request, 'struct/category.html', context)

# Product Details
def ProdCatDetail(request, c_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=c_slug, slug=product_slug)
    except Exception as e:
        raise e
    context = {
        'product':product
    }
    return render(request, 'struct/product.html', context)

# Search Function
def searchProducts(request):
    if request.method == 'POST':
        product_scan = request.POST['product_scan']
        search_results = Product.objects.all().filter(Q(name__contains=product_scan) | Q(description__contains=product_scan))
    context = {
        'product_scan':product_scan,
        'search_results':search_results
    }
    return render(request, 'search.html', context)

# Registration Page
def registrationPage(request):
    return render(request, 'struct/register.html')

# Profile Page
def profilePage(request):
    if 'user_id' not in request.session:
        return redirect('/')
    # Checks for user_id in request.session
    if 'user_id' in request.session:
        login_check = User.objects.get(id=request.session['user_id'])
    context = {
        'current_user':login_check
    }
    return render(request, 'struct/profile.html', context)

# Update Profile Page
def editProfile(request):
    errors = User.objects.edit_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/profile')
    else:
        # Checks for user_id in request.session
        if 'user_id' in request.session:
            profile_edit = User.objects.get(id=request.session['user_id'])
    profile_password = profile_edit.password
    profile_edit.email = request.POST['email_edit']
    profile_password = request.POST['password_edit']
    profile_password = bcrypt.hashpw(profile_password.encode(), bcrypt.gensalt()).decode()
    profile_password.save()
    profile_edit.save()
    return redirect('/profile')

# Account Creation
def createAccount(request):
    if request.method != 'POST':
        return redirect('/')
    errors = User.objects.registration_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/register')
    else:
        new_password = request.POST['password']
        new_passwordHash = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            username = request.POST['username'],
            password = new_passwordHash,
        )
        request.session['user_id'] = new_user.id
        return redirect('shop_app:allProdCat')

# Login Page
def loginPage(request):
    return render(request, 'struct/login.html')

# Login Function
def signIn(request):
    if request.method != 'POST':
        return redirect('/')
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/login')
    logged_in = User.objects.filter(username=request.POST['login_username'])
    request.session['user_id'] = logged_in[0].id
    return redirect('/')

# Log Out
def logOut(request):
    request.session.flush()
    return redirect('/')

# Delete Account
def accountDelete(request):
    destroy = User.objects.get(id=request.session['user_id'])
    destroy.delete()
    request.session.flush()
    return redirect('/')