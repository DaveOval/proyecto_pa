import reflex as rx
from ..Auth import AuthState


@rx.page(route="/dashboard", title="Dashboard")
def paginaDashboard() -> rx.Component:
    return rx.container(
        rx.center(
            rx.heading('Bienvenido usuario', size='8'),
            rx.text(AuthState.auth_token)
        )
    )