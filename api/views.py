
from rest_framework.views import APIView


# Create your views here.
class Home(APIView):
    template_name='index.html'
    def get(self,request):
        return render(request,self.template_name)
    
class Ejemplo2(APIView):
    template_name='ejemplos2.html'
    def get(self,request):
        return render(request,self.template_name)

class Descarga(APIView):
    template_name='descarga.html'
    def get(self,request):
        return render(request,self.template_name)
    
class Constancia(APIView):
    template_name='constancia.html'
    def get(self,request):
        return render(request,self.template_name)
    
class Aceptacion(APIView):
    template_name='aceptacion.html'
    def get(self,request):
        return render(request,self.template_name)

class Horas(APIView):
    template_name='horas.html'
    def get(self,request):
        return render(request,self.template_name)

class Ine(APIView):
    template_name='ine-curp.html'
    def get(self,request):
        return render(request,self.template_name)

class Presentacion(APIView):
    template_name='presentacion.html'
    def get(self,request):
        return render(request,self.template_name)
    
class Solicitud1(APIView):
    template_name='solicitud_ex1.html'
    def get(self,request):
        return render(request,self.template_name)
    
class Solicitud2(APIView):
    template_name='solicitud_ex2.html'
    def get(self,request):
        return render(request,self.template_name)

class Termino(APIView):
    template_name='termino.html'
    def get(self,request):
        return render(request,self.template_name)
    
class Chat(APIView):
    template_name='chat.html'
    def get(self,request):
        return render(request,self.template_name)
    
class Calendario(APIView):
    template_name='calendario.html'
    def get(self,request):
        return render(request,self.template_name)

class Informar(APIView):
    template_name='informar.html'
    def get(self,request):
        return render(request,self.template_name)
 
class Ejemplo(APIView):
    template_name='ejemplos.html'
    def get(self,request):
        return render(request,self.template_name)
   
class Contacto(APIView):
    template_name='contacto.html'
    def get(self,request):
        return render(request,self.template_name)
   

class Pag2(APIView):
    template_name='registro.html'
    def get(self,request):
        return render(request,self.template_name)

class Inicio(APIView):

    template_name='principal.html'
    def get(self,request):
        grafica_data = grafica(request)
        tuvista_data = tuvista1(request)
        tuvista_data2 = tuvista2(request)
        tuvista_data3 = tuvista3(request)
        tuvista_data4 = tuvista4(request)
        tuvista_data5 = tuvista5(request)
        
        # Combina los contextos de ambas vistas en un solo diccionario
        context = {**grafica_data, **tuvista_data, **tuvista_data2, **tuvista_data3, **tuvista_data4, **tuvista_data5}
    
        return render(request,self.template_name, context)
    
    
class Recupera(APIView):
    template_name='recuperar.html'
    def get(self,request):
        return render(request,self.template_name)
    
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
from .models import Usuario, Informacion

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

from django.shortcuts import render
from .models import Informacion


def grafica(request):
    total = Informacion.objects.all()
    return {'total': total}

#Grafica de barras
def tuvista1(request):
    # Realiza una consulta que cuente las filas con 'SI' en la columna pregunta1
    count1 = Informacion.objects.filter(pregunta2="Si").count()
    return {'count_si': count1}

def tuvista2(request):
    # Realiza una consulta que cuente las filas con 'NO' en la columna pregunta1
    count2 = Informacion.objects.filter(pregunta2="No").count()
    return {'count_no': count2}


#Grafica pie
def tuvista3(request):
    # Realiza una consulta que cuente las filas con 'SI' en la columna pregunta1
    count3 = Informacion.objects.filter(pregunta6="Computadora").count()
    return {'count_compu': count3}

def tuvista4(request):
    # Realiza una consulta que cuente las filas con 'NO' en la columna pregunta1
    count4 = Informacion.objects.filter(pregunta6="Teléfono móvil").count()
    return {'count_tel': count4}

def tuvista5(request):
    # Realiza una consulta que cuente las filas con 'NO' en la columna pregunta1
    count4 = Informacion.objects.filter(pregunta6="Tableta").count()
    return {'count_tablet': count4}

def HomePage(request):
    return render(request, 'principal.html')
