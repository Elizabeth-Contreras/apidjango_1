from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib import messages
""" from .models import Usuario #Importar el modelo Usuario (Corresponde a la tabla)
from .forms import Registroform """
# Create your views here.
class Home(APIView):
    template_name='index.html'
    def get(self,request):
        return render(request,self.template_name)
    
class Pag2(APIView):
    template_name='registro.html'
    def get(self,request):
        return render(request,self.template_name)
    

class Inicio(APIView):
    template_name='principal.html'
    def get(self,request):
        return render(request,self.template_name)
    
class Recupera(APIView):
    template_name='recuperar.html'
    def get(self,request):
        return render(request,self.template_name)
    
from django.shortcuts import render, redirect
from .forms import UsuarioForm

def registro_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():  
            form.save()
            messages.success(request, 'Registro exitoso')
            return render (request, "index.html",{'form': form})
        else:
            messages.error(request, 'Registro duplicado')
            return render(request, "registro.html", {'form': form, 'errors': form.errors})
    else:
            form = UsuarioForm()
        
    return render(request, "registro.html", {'form': form})


from django.contrib.auth import authenticate, login
""" def login_view(request):
    if request.method == 'POST':
        username = request.POST['id_usuario']  
        password = request.POST['contrasena']

        # Utiliza la función authenticate para verificar las credenciales del usuario
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Si las credenciales son válidas, autentica al usuario utilizando la función login
            login(request, user)
            return redirect("principal")  # Redirige a la página de inicio después de iniciar sesión
        else:
            # Si las credenciales no son válidas, muestra un mensaje de error
            messages.error(request, 'Credenciales inválidas. Inténtalo de nuevo.')
    
    return render(request, "index.html")  # Renderiza la página de inicio de sesión

 """

from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Usuario  # Importa el modelo Usuario desde tu aplicación

def login_view(request):
    if request.method == 'POST':
        id_usuario = request.POST['id_usuario']  
        contrasena = request.POST['contrasena']

        # Busca un usuario en tu tabla  Usuario con el nombre de usuario proporcionado
        try:
            usuario = Usuario.objects.get(id_usuario=id_usuario)  # Cambia 'nombre' a 'nombre_usuario' si es necesario
        except Usuario.DoesNotExist:
            usuario = None

        if usuario is not None and usuario.contrasena == contrasena:
            # Si se encuentra un usuario y la contraseña coincide, autentica al usuario
            request.session['user_id'] = usuario.id  # Almacena el ID del usuario en la sesión
            return redirect("principal")  # Redirige a la página de inicio después de iniciar sesión
        else:
            # Si las credenciales no son válidas, muestra un mensaje de error
            messages.error(request, 'Credenciales inválidas. Inténtalo de nuevo')

    return render(request, "index.html")  # Renderiza la página de inicio de sesión
