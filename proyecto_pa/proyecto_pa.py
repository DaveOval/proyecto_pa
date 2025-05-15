"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

class ContadorEstado(rx.State):
    """State for the Contador component."""

    count: int = 0

    @rx.event
    def increment(self):
        self.count += 1
    @rx.event
    def decrement(self):
        self.count -= 1


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )

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


app = rx.App()
app.add_page(index)
app.add_page(pagina_info, route="/info")
