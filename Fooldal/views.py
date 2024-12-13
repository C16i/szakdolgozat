from django.shortcuts import render, redirect, get_object_or_404
from .models import Termek,Cart,CartItem
from .forms import TermekForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def homepage(request):
    return render(request,'homepage.html')

def shop(request):
    return render(request, 'shop.html')

@login_required
def termek_create(request):
    if request.method == "POST":
        form = TermekForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('termek-list') #atiranyit a listazas oldalra
    else:
        form = TermekForm()
    return render(request,'termek_form.html',{'form':form})

@login_required               
def termek_list(request):
    termekek = Termek.objects.all()
    return render(request, 'termek_list.html', {'termekek': termekek})
    
@login_required
def termek_update(request, pk):
    termek = get_object_or_404(Termek, pk=pk)
    if request.method == "POST":
        form = TermekForm(request.POST, instance=termek)
        if form.is_valid():
            form.save()
            return redirect('termek-list')
    else:
        form = TermekForm(instance=termek)
    return render(request, 'termek_form.html', {'form': form})

@login_required
def termek_delete(request, pk):
    termek = get_object_or_404(Termek, pk=pk)
    if request.method == "POST":
        termek.delete()
        return redirect('termek-list')
    return render(request, 'termek_confirm_delete.html', {'termek': termek})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sikeres regisztráció!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form' :form})

@login_required
def profile(request):
    return render(request,'profile.html')

@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    if created:
        print("Új kosarat hoztunk létre.")
    return render(request, 'cart.html', {'cart': cart})

@login_required
def add_to_cart(request, product_id):
    # Lekérdezi a terméket az adatbázisból
    product = get_object_or_404(Termek, id=product_id)

    # Lekérdezi vagy létrehozza a felhasználó kosarát
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Lekérdezi vagy létrehozza a kosártételt
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    # Ha már létezik a tétel, növeli a darabszámot
    if not created:
        cart_item.quantity += 1
    cart_item.save()

    return redirect('termek-list')  # Visszairányít a termékek listájához

def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    item.delete()
    return redirect('view_cart')

def order(request):
    return render (request,'order.html')