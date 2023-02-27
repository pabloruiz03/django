from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClienteForm, CocheForm, AlquilerForm
from .models import Cliente, Coche, Alquiler, Usuario


def index(request):
    return render(request, 'index.html')


def sobre_nosotros(request):
    return render(request, 'sobre_nosotros.html')


def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente_list.html', {'clientes': clientes})


def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            cliente = Cliente(dni=data['dni'], nombre=data['nombre'], apellido=data['apellido'], email=data['email'],
                              telefono=data['telefono'])
            cliente.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'cliente_form.html', {'form': form})


def editar_cliente(request, dni):
    cliente = Cliente.objects.get(pk = dni)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'cliente_edit.html', {'form': form})


def borrar_cliente(request, dni):
    cliente = get_object_or_404(Cliente, pk=dni)
    cliente.delete()
    return redirect('listar_clientes')


def listar_coches(request):
    coches = Coche.objects.all()
    return render(request, 'coche_list.html', {'coches': coches})


def agregar_coche(request):
    if request.method == 'POST':
        form = CocheForm(request.POST)
        if form.is_valid():
            coche = form.save(commit=False)
            coche.save()
            return redirect('listar_coches')
    else:
        form = CocheForm()
    return render(request, 'coche_form.html', {'form': form})


def editar_coche(request, matricula):
    coche = Coche.objects.get(matricula=matricula)
    if request.method == 'POST':
        form = CocheForm(request.POST, instance=coche)
        if form.is_valid():
            form.save()
            return redirect('listar_coches')
    else:
        form = CocheForm(instance=coche)
    return render(request, 'coche_edit.html', {'form': form})


def borrar_coche(request, matricula):
    coche = get_object_or_404(Coche, pk=matricula)
    coche.delete()
    return redirect('listar_coches')


def listar_alquileres(request):
    alquileres = Alquiler.objects.all()
    return render(request, 'alquilar_list.html', {'alquileres': alquileres})


def agregar_alquiler(request):
    if request.method == 'POST':
        form = AlquilerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_alquileres')
    else:
        form = AlquilerForm()
    return render(request, 'alquilar_form.html', {'form': form})


def editar_alquiler(request, pk):
    alquiler = get_object_or_404(Alquiler, pk=pk)
    if request.method == 'POST':
        form = AlquilerForm(request.POST, instance=alquiler)
        if form.is_valid():
            form.save()
            return redirect('listar_alquileres')
    else:
        form = AlquilerForm(instance=alquiler)
    return render(request, 'alquilar_edit.html', {'form': form})


def borrar_alquiler(request, pk):
    alquiler = get_object_or_404(Alquiler, pk=pk)
    alquiler.delete()
    return redirect('listar_alquileres')

# def gravatar_url(email, size=40):
#     return "https://www.gravatar.com/avatar/%s?%s" % (
#         hashlib.md5(email.lower().encode('utf-8')).hexdigest(), urlencode({'s': str(size)}))

def iniciar_sesion(request):
    if request.method == 'POST':
        usuario = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if usuario is not None:
            login(request, usuario)
            return redirect('index')
        else:
            mensaje_error = "Nombre de usuario o contraseña incorrectos."
    else:
        mensaje_error = None
    return render(request, 'login.html', {'error': mensaje_error})

def registrar_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            nombre = request.POST['nombre']
            correo_electronico = request.POST['correo_electronico']
            nuevo_usuario = Usuario(usuario=usuario, nombre=nombre, correo_electronico=correo_electronico)
            nuevo_usuario.save()
            usuario_autenticado = authenticate(request, username=usuario.username, password=request.POST['password1'])
            if usuario_autenticado is not None:
                login(request, usuario_autenticado)
                return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})