from typing import Optional

from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect

from users.forms import CreateUserForm
from users.models import User


def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        # Obtiene el nombre de usuario enviado en la solicitud
        username = request.POST["username"]

        # Obtiene la contraseña enviada en la solicitud
        password = request.POST["password"]

        # Autentica al usuario con las credenciales proporcionadas
        user: Optional[User] = authenticate(request, username=username, password=password)

        if user is None:
            # Define un mensaje de error en caso de autenticación fallida
            context = {"error": "Nombre de usuario o contraseña incorrectos"}

            # Renderiza la plantilla "users/login.html" con el mensaje de error
            return render(request, "users/login.html", context)

        # Inicia sesión para el usuario autenticado
        login(request, user)

        # Redirecciona al usuario a la página principal
        return redirect("/")

    # Renderiza la plantilla "users/login.html"
    return render(request, "users/login.html")


def register_view(request):
    # Comprueba si el usuario que realiza la solicitud está autenticado (logueado)
    # sí lo está, redirecciona al "dashboard"
    if request.user.is_authenticated:
        return redirect("dashboard")

    # Inicializa una instancia del formulario CreateUserForm
    form: CreateUserForm = CreateUserForm(request.POST or None)

    if request.method == "POST":
        # Si el formulario es válido
        if form.is_valid():

            # Hashea la contraseña del usuario para seguridad en caso de hack
            # El login asume que la contraseña esta hasheada, si no se hace esto no funcionará el login
            form.password = make_password(form.password)

            # Guarda el formulario, creando un nuevo usuario en la base de datos
            form.save()

            # Redirecciona al usuario a la página de inicio de sesión
            return redirect("login")

        else:
            # Por cada error en el formulario
            for field in form.errors:
                # Agrega las clases CSS "is-invalid" y "active" a los campos erróneos para resaltarlo en la interfaz
                form[field].field.widget.attrs['class'] += ' is-invalid active'

    # Renderiza la plantilla "users/register.html" y pasa el formulario como variable de contexto
    return render(request, "users/register.html", {"form": form})
