import reflex as rx
from ..Auth import AuthState


@rx.page(route="/dashboard", title="Dashboard", on_load=AuthState.verificar_token)
def paginaDashboard() -> rx.Component:

    return rx.container(
        rx.cond(
            AuthState.esta_cargando,
            rx.text("Cargando..."),
            rx.text("Bienvenido usuario"),
        )
    )