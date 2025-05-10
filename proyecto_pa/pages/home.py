import reflex as rx
from proyecto_pa.components.navbar import navbar
from proyecto_pa.state import ProductoState

def home():
    return rx.container(
        navbar(),
        rx.heading("Catálogo de Productos"),
        rx.button("Cargar productos", on_click=ProductoState.cargar_productos),
        rx.foreach(
            ProductoState.productos,
            lambda p: rx.box(
                rx.text(f"{p['nombre']} - ${p['precio']}"),
                border="1px solid gray",
                padding="0.5em",
                margin_bottom="0.5em"
            )
        ),
        padding="2em",
    )
