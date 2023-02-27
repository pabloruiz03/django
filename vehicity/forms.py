from django import forms
from .models import Cliente, Coche, Alquiler, Usuario


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['dni', 'nombre', 'apellido', 'email', 'telefono']
        widgets = {
            'dni': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su DNI'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su apellido'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su correo electrónico'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su número de teléfono'}),
        }


class CocheForm(forms.ModelForm):
    class Meta:
        model = Coche
        fields = ['matricula', 'marca', 'modelo', 'año', 'tarifa_diaria']
        widgets = {
            'matricula': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese la matrícula del coche'}),
            'marca': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la marca del coche'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el modelo del coche'}),
            'año': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el año del coche'}),
            'tarifa_diaria': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese la tarifa diaria del coche'}),
        }


class AlquilerForm(forms.ModelForm):
    class Meta:
        model = Alquiler
        fields = ['cliente', 'coche', 'fecha_inicio', 'fecha_fin', 'dni_cliente', 'matricula_coche']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'coche': forms.Select(attrs={'class': 'form-control'}),
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'dni_cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el DNI del cliente'}),
            'matricula_coche': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la matrícula del coche'}),
        }

class UsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirmacion_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['usuario', 'nombre', 'correo_electronico', 'password', 'confirmacion_password']
