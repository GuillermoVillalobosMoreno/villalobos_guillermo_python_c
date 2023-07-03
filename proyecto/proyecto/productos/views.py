from django.shortcuts import render, redirect
from .forms import ProductoForm
from .models import Productos

def productos(request):
    productos = Productos.objects.all()
    form = ProductoForm()

    if request.method == 'POST':
        form = ProductoForm(request.POST)
        print('hello post method')
        print(form)
        if form.is_valid():
            print('hello post method valid')
            print(form)
            form.save()
            

    return render(request, 'productos.html', {'productos': productos, 'form': form})
