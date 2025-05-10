import reflex as rx
from proyecto_pa.components.navbar import navbar

def about():
    return rx.vstack(
        navbar(),
        rx.heading("Acerca de Nosotros"),
        rx.text("Esta es una página informativa creada con Reflex."),
        padding="2em"
    )
