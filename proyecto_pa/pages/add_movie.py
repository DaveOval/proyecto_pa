import reflex as rx
from ..components.navbar import navbar_dashboard

class EstadoAgregarPelicula(rx.State):
    titulo_pelicula: str = ""
    descripcion_pelicula: str = ""
    fecha_lanzamiento: str = ""
    cargando: bool = False
    error: bool = False
    
    
    @rx.event
    def agregar_pelicula(self):
        print("Agregando película...")
        self.cargando = True


@rx.page(route="/agregar-pelicula", title="Agregar Película")
def pagina_agregar_pelicula() -> rx.Component:
    return rx.container(
        navbar_dashboard(),
        rx.center(
            rx.box(
                rx.vstack(
                    rx.heading('Agregar pelicula', size='8', margin_bottom='1rem'),
                    
                    rx.input(
                        placeholder="Título de la película",
                        type="text",
                        width="100%",
                        id="titulo_pelicula"
                    ),
                    
                    rx.text_area(
                        placeholder="Descripción de la película",
                        width="100%",
                        id="descripcion_pelicula"
                    ),
                    
                    rx.input(
                        placeholder="Fecha de lanzamiento (YYYY-MM-DD)",
                        type="date",
                        width="100%",
                        id="fecha_lanzamiento"
                    ),
                    
                    rx.cond(
                        EstadoAgregarPelicula.cargando,
                        rx.button(
                            rx.hstack(
                                rx.spinner(loading=True),
                                rx.text("Agregando..."),
                            ),
                            disabled=True,
                            width="100%",
                            color_scheme="blue",
                        ),
                        rx.button(
                            "Agregar Película",
                            on_click=EstadoAgregarPelicula.agregar_pelicula,
                            width="100%",
                            color_scheme="blue",
                        )
                    )
                ),
                padding="2rem",
                width="100%",
                max_width="600px",
                
            ),
            height="100vh",
        )
    )