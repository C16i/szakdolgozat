from django.shortcuts import render, redirect, get_object_or_404
from .models import Termek
from .forms import TermekForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# Create your views here.
def homepage(request):
    return render(request,'homepage.html')

def shop(request):
    return render(request, 'shop.html')

def termek_create(request):
    if request.method == "POST":
        form = TermekForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('termek-list') #atiranyit a listazas oldalra
    else:
        form = TermekForm()
    return render(request,'termek_form.html',{'form':form})
                
def termek_list(request):
    termekek = Termek.objects.all()
    return render(request, 'termek_list.html', {'termekek': termekek})
    
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