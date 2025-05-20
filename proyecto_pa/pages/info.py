import reflex as rx

class ContadorEstado(rx.State):
    """State for the Contador component."""

    count: int = 0

    @rx.event
    def increment(self):
        self.count += 1
    @rx.event
    def decrement(self):
        self.count -= 1

@rx.page(route="/informacion", title="About us")
def pagina_info() -> rx.Component:
    
    return rx.container(
        rx.center(
            rx.vstack(
                rx.text('Cambio de estado', size="8"),
                rx.text(ContadorEstado.count , size="9", justify="center"),
                rx.button('Incrementar' , on_click=ContadorEstado.increment),
                rx.button('Decrementar' , on_click=ContadorEstado.decrement),
            )
        )
    )