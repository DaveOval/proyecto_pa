"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from proyecto_pa.pages.info import pagina_info
from proyecto_pa.pages.login import pagina_login
from proyecto_pa.pages.signup import pagina_signup
from proyecto_pa.pages.dashboard import paginaDashboard

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

app = rx.App()

app.add_page(index)
app.add_page(pagina_info)
app.add_page(pagina_login)
app.add_page(pagina_signup)
app.add_page(paginaDashboard)