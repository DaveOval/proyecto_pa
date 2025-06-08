import reflex as rx


@rx.page(route="/dashboard", title="Dashboard")
def paginaDashboard() -> rx.Component:
    return rx.container(
        rx.center(
            rx.heading('Bienvenido usuario', size='8'),
        )
    )