""" from django.test import TestCase
from api.models import Usuario, Informacion, Contactame

class TestUsuarioModel(TestCase):
    #La contraseña debe ser mayor a 8 caracteres
    def test_contraseña_corta(self):
        contraseña_corta = Usuario(contrasena='1_Ali1230')
        assert len(contraseña_corta.contrasena)  > 8, "La contraseña debe ser mayor a 8 caracteres"
        assert len(contraseña_corta.contrasena)  < 15, "La contraseña debe contener menos de 15 caracteres"

    def test_creacion_varios_usuarios(self):

        # Crear varios usuarios que no repitan el usuario y correo electronico
        Usuario.objects.create(id_usuario='Martina$#!', correo='1234@gmail.com', contrasena='plmk')
        Usuario.objects.create(id_usuario='Mar!', correo='julieta@teschi.edu.mx', contrasena='123456789')

        # Verificar que la cantidad de usuarios es correcta
        assert Usuario.objects.count() == 2

    def test_campos_varios_usuarios(self):
        user1 = Usuario.objects.create(id_usuario='1_Ali', correo='poiuytt@gmail.com', contrasena='plmk')
        user2 = Usuario.objects.create(id_usuario='Martina$#!', correo='julieta@teschi.edu.mx', contrasena='123456789')
        user3 = Usuario.objects.create(id_usuario='-Sandra', correo='1234@gmail.com', contrasena='qwert$')

        # Valida el usuario registrado (logeo)
        assert user1.id_usuario == '1_Ali'
        assert user1.correo == 'poiuytt@gmail.com'
        assert user1.contrasena == 'plmk'

        assert user2.id_usuario == 'Martina$#!'
        assert user2.correo == 'julieta@teschi.edu.mx'
        assert user2.contrasena == '123456789'

        assert user3.id_usuario == '-Sandra'
        assert user3.correo == '1234@gmail.com'
        assert user3.contrasena == 'qwert$'

    #Verifica que los datos a almacenar en la tabla de graficas sea correctos 
    def test_creacion_informacion(self):
        Informacion.objects.create( #NO PUEDE INSERTAR EN NINGUN CAMPO NUMEROS 
            nombre='Elizabeth Contreras Marquez',
            pregunta1='Si',
            pregunta2='No',
            pregunta3='Requisitos y ejemplos',
            pregunta4='Recursos descargables',
            pregunta5='No concocer la información',
            pregunta6='Falta de comunicación',
            pregunta7='Opción'
        )
        self.assertEqual(Informacion.objects.count(), 1)

    #Verifica que los datos a almacenar en la tabla de contactos sean correctos, 
    # que el numero no se pase del rango y que el correo elecctronico tenga @
    def test_creacion_mensaje(self):
        Contactame.objects.create(
            nombre='E1234',
            correo_electronico='elizabeth@gmail.com',
            telefono='1234567899',
            mensaje='No me gusta la aplicación Y tengo algunas sugerencias'
        )
        self.assertEqual(Contactame.objects.count(), 1)

    #Valida que el numero telefonico tenga 10 digitos 
    def test_telefono_exacto(self):
        telefono_exacto = Contactame(telefono='5567654321')
        assert len(telefono_exacto.telefono)  == 10   
    
    #valida que el correo electronico tenga @
    def test_correo_con_arroba_contacto(self):
        correo_E = Contactame(correo_electronico='elicontreras201@gmail.com')
        assert '@' in correo_E.correo_electronico, "El correo electrónico debe contener '@'"

    def test_correo_con_arroba_usuario(self):
        correo_usuario = Usuario(correo='elicontreras201@gmail.com')
        assert '@' in correo_usuario.correo, "El correo electrónico debe contener '@'"
         """