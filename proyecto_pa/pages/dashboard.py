import reflex as rx
from ..Auth import AuthState
from ..components.navbar import navbar_dashboard

@rx.page(route="/dashboard", title="Dashboard", on_load=AuthState.verificar_token)
def paginaDashboard() -> rx.Component:

    return rx.container(
        navbar_dashboard(),
        rx.container(
            rx.center( 
                rx.vstack(
                    rx.heading('Bienvenido', size='6', align='center'),
                    width='100%',
                )
            )
            
        ),
        width='100%',
    )