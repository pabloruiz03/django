from django import forms
from .models import Cliente, Coche, Alquiler, Usuario


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class CocheForm(forms.ModelForm):
    class Meta:
        model = Coche
        fields = '__all__'


class AlquilerForm(forms.ModelForm):
    class Meta:
        model = Alquiler
        fields = ['cliente', 'coche', 'fecha_inicio', 'fecha_fin']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
        }


class UsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirmacion_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['usuario','nombre', 'correo_electronico', 'password', 'confirmacion_password']
