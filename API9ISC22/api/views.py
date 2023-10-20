
from rest_framework.views import APIView


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
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
from .models import Usuario  

def ingresa_usuario(request):
    if request.method == "POST":
        id_usuario = request.POST.get('id_usuario')
        
        correo = request.POST.get('correo')
        contrasena = request.POST.get('contrasena')
        confirmar_contrasena = request.POST.get('confirmar_contrasena')
        
        if Usuario.objects.filter(id_usuario=id_usuario).exists():  #Validar si el usuario ya existe
            messages.error(request, 'Usuario duplicado')
            return render(request, "registro.html")
        
        if contrasena == confirmar_contrasena:
            cuenta = Usuario(id_usuario=id_usuario, correo=correo, contrasena=contrasena)
            cuenta.save()

            template = render_to_string('email_template.html', {
                'id_usuario': id_usuario,
                
                'correo': correo,
            })

            correo = EmailMessage(
                subject='Confirmacion de registro',
                body=template,
                from_email=settings.EMAIL_HOST_USER,
                to=[correo]
            )

            correo.fail_silently = False
            correo.send()
            messages.success(request, 'Registro exitoso. \n Se ha enviado un correo de confirmación')
            return redirect('index')  
        else:
            messages.error(request, 'Las contraseñas no coinciden')
            return render(request, "registro.html")
    
    return redirect('index')  
    


from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Usuario  # Importa el modelo Usuario 

def login_view(request):
    if request.method == 'POST':
        id_usuario = request.POST['id_usuario']  
        contrasena = request.POST['contrasena']

        # Busca un usuario
        try:
            usuario = Usuario.objects.get(id_usuario=id_usuario)  
        except Usuario.DoesNotExist:
            usuario = None

        if usuario is not None and usuario.contrasena == contrasena:
            # autentica al usuario
            request.session['user_id'] = usuario.id  # Almacena el ID del usuario en la sesión
            return redirect("principal")  # ir a la página de inicio 
        else:
            # Si las credenciales no son válidas, muestra un mensaje de error
            messages.error(request, 'Credenciales inválidas. Inténtalo de nuevo')

    return render(request, "index.html")  # regresar al login
