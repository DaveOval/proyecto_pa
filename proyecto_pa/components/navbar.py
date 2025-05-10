import reflex as rx

def navbar():
    return rx.hstack(
        rx.link("Inicio", href="/"),
        rx.link("Acerca de", href="/about"),
        spacing="4",
        padding="1em",
        bg="gray.100",
    )
