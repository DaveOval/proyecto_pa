import reflex as rx
from ..models.usuarios import Usuarios
from sqlmodel import select
import bcrypt

from ..Auth import AuthState

import datetime

import jwt

LLAVE_SECRETA = 'llave_secreta'

class EstadoLogin(rx.State):
    # Creamos un atributo por cada dato que nos interesa capturar
    email: str = ""
    password: str = ""

    @rx.event
    def asignarCorreo(self, correo_ingresado: str):
        # Asignamos el valor del input al atributo email
        self.email = correo_ingresado

    @rx.event
    def asignarPassword(self, password_ingresada: str):
        # Asignamos el valor del input al atributo password
        self.password = password_ingresada

    @rx.event
    def mostrar_info(self):
        print(f"Correo: {self.email}")
        print(f"Contraseña: {self.password}")
        # Mostramos el valor de los atributos
        if self.email == "admin@admin.com" or self.password == "123":
            print("Bienvenido admin")
            self.email = ""
            self.password = ""
        else:
            print("Error: Credenciales incorrectas")
            self.email = ""
            self.password = ""

    def buscar_usuario(self):
        
        with rx.session() as sesion:

            usuario_registrado = sesion.exec(
                select(Usuarios).where(Usuarios.email == self.email)
            ).first()

        return usuario_registrado

    def verificar_password(self, password_db):

        return bcrypt.checkpw(self.password.encode(), password_db.encode())
    
    @rx.event
    def iniciar_sesion(self):
        print("Iniciando sesion")
        usuario = self.buscar_usuario()
        print(usuario)

        if usuario and self.verificar_password(usuario.password):
            print("Inicio de sesion exitoso")

            datos_token = {
                'user_id': usuario.id,
                'user_name': usuario.nombre,
                'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)
            }

            # Creamos una credencial
            token = jwt.encode(datos_token, LLAVE_SECRETA ,algorithm='HS256')

            yield AuthState.guardar_token(token)
            return rx.redirect("/dashboard")

        else:
            print("Error: Credenciales incorrectas")



@rx.page(route="/login", title="Iniciar sesión", on_load=AuthState.verificar_usuario)
def pagina_login() -> rx.Component:
    return rx.container(
        rx.center(
            rx.vstack(
                rx.heading("Iniciar sesión", size="8"),
                rx.input(
                    placeholder="Correo electrónico",
                    type="email",
                    value=EstadoLogin.email,
                    on_change=EstadoLogin.asignarCorreo
                ),
                rx.input(
                    placeholder="Contraseña",
                    type="password",
                    value=EstadoLogin.password,
                    on_change=EstadoLogin.asignarPassword
                ),
                rx.button(
                    "Iniciar sesión",
                    on_click=EstadoLogin.iniciar_sesion,
                ),
            )
        )
    )
