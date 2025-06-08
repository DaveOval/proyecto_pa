import reflex as rx

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

@rx.page(route="/signup", title="Registrarse")
def pagina_signup() -> rx.Component:
    return rx.container(
        rx.center(
            rx.vstack(
                rx.heading("Registrarse"),
                rx.input(
                    placeholder='Nombre',
                    type='text',
                    value=EstadoSignup.nombre,
                    on_change=EstadoSignup.asignarNombre,
                ),
                rx.input(
                    placeholder='Correo electrónico',
                    type='email',
                    value=EstadoSignup.email,
                    on_change=EstadoSignup.asignarCorreo,
                ),
                rx.input(
                    placeholder='Contraseña',
                    type='password',
                    value=EstadoSignup.password,
                    on_change=EstadoSignup.asignarPassword,
                ),
                rx.button(
                    'Crear cuenta',
                    on_click=EstadoSignup.mostrar_info,
                )
            )
        )
    )