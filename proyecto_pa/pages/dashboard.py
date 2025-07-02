import reflex as rx
from ..Auth import AuthState



@rx.page(route="/dashboard", title="Dashboard", on_load=AuthState.verificar_token)
def paginaDashboard() -> rx.Component:

    return rx.container(
        rx.cond(
            AuthState.esta_cargando,
            rx.center(
                rx.text("Cargando...", align='center'),
            ),
            rx.container(
                rx.center( 
                    rx.vstack(
                        rx.heading('Bienvenido', size='6', align='center'),
                        rx.button('Cerrar sesion', on_click=AuthState.cerrar_sesion, color_scheme="red", margin_left='10')
                    )
                )
            )
        )
    )