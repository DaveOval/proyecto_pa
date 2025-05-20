import reflex as rx

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


@rx.page(route="/login", title="Iniciar sesión")
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
                    on_click=EstadoLogin.mostrar_info,
                ),
            )
        )
    )
