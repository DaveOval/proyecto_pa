import reflex as rx
from ..Auth import AuthState

def navbar_dashboard() -> rx.Component:
    return rx.hstack(
        rx.heading("🍿 PopcornHour", size="6"),

        rx.spacer(),

        rx.hstack(
            rx.link("Inicio", href="/dashboard", padding_x="1rem", font_weight="500"),
            rx.link("Agregar Post", href="/agregar-post", padding_x="1rem", font_weight="500"),
            spacing="2",
        ),

        rx.spacer(),

        rx.button("Cerrar sesión", on_click=AuthState.cerrar_sesion, color_scheme="red"),

        padding="1rem",
        bg="blue.600",
        color="white",
        box_shadow="md",
        position="sticky",
        top="0",
        z_index="1000",
        width="100%",
    )
