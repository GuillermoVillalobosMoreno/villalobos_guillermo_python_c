from django import forms
from .models import Productos
import datetime as dt

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['nombre', 'descripcion', 'precio']
        
    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get('nombre')
        descripcion = cleaned_data.get('descripcion')
        precio = cleaned_data.get('precio')
        fecha_registro = dt.date.today()
        estatus = True
        
        if not nombre or not descripcion or not precio:
            raise forms.ValidationError("Llena todos los campos antes de guardar")
        
        return cleaned_data