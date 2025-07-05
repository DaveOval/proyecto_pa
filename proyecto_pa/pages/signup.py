import reflex as rx

from ..models.usuarios import Usuarios
from sqlmodel import select

from ..Auth import AuthState

class EstadoSignup(rx.State):
    email: str = ""
    password: str = ""
    nombre: str = ""

    @rx.event
    def asignarCorreo(self, correo_ingresado: str):
        self.email = correo_ingresado


    @rx.event
    def asignarPassword(self, pass_ingresado):
        self.password = pass_ingresado

    @rx.event
    def asignarNombre(self, nombre_ingresado: str):
        self.nombre = nombre_ingresado

    @rx.event
    def mostrar_info(self):
        print(f"Correo: {self.email}")
        print(f"Contraseña: {self.password}")
        print(f"Nombre: {self.nombre}")

    def buscar_usuario(self):
        
        with rx.session() as sesion:

            usuario_registrado = sesion.exec(
                select(Usuarios).where(Usuarios.email == self.email)
            ).first()

        return usuario_registrado

    @rx.event
    def registrar_cuenta(self):

        usuario_registrado = self.buscar_usuario()

        if usuario_registrado:
            print("Usuario registrado")
            self.email = ''

        else:
            nuevo_usuario = Usuarios.crear_usuario(
                self.nombre,
                self.email,
                self.password
            )

            with rx.session() as sesion:
                sesion.add(nuevo_usuario)
                sesion.commit()
            return rx.redirect('/login')



@rx.page(route="/signup", title="Registrarse", on_load=AuthState.verificar_usuario)
def pagina_signup() -> rx.Component:
    return rx.container(
        rx.center(
            rx.box(
                rx.vstack(
                    rx.heading("Registrarse", size="8", margin_bottom="1rem"),
                    
                    rx.input(
                        placeholder='Nombre',
                        type='text',
                        value=EstadoSignup.nombre,
                        on_change=EstadoSignup.asignarNombre,
                        width='100%',
                    ),
                    rx.input(
                        placeholder='Correo electrónico',
                        type='email',
                        value=EstadoSignup.email,
                        on_change=EstadoSignup.asignarCorreo,
                        width='100%',
                    ),
                    rx.input(
                        placeholder='Contraseña',
                        type='password',
                        value=EstadoSignup.password,
                        on_change=EstadoSignup.asignarPassword,
                        width='100%',
                    ),
                    rx.button(
                        'Crear cuenta',
                        on_click=EstadoSignup.registrar_cuenta,
                        width='100%',
                        color_scheme='blue',
                    ),
                    
                    rx.link(
                        rx.text("Inicia sesión aquí"),
                        href="/login",
                        color_scheme="blue",
                    ),
                ),
                padding="2rem",
                width="100%",
                max_width="400px",
                box_shadow="lg",
                border_radius="lg",
            ),
            height="100vh",
        )
    )