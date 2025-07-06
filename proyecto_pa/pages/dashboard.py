import reflex as rx
from ..Auth import AuthState
from ..components.navbar import navbar_dashboard
from sqlmodel import select
from ..models import Peliculas
from typing import List

from proyecto_pa.state.app_state import AppState

class EstadoDashboard(rx.State):
    peliculas: List[Peliculas] = []
    cargando: bool = False
    error: bool = False
    
    def obtener_peliculas(self):
        self.cargando = True
        
        try:
            with rx.session() as sesion:
                resultado = sesion.exec(select(Peliculas))
                self.peliculas = resultado.all()
        
        except Exception as e:
            self.error = True
            print(f"Error al obtener las peliculas: {e}")
        finally:
            self.cargando = False
            

@rx.page(
    route="/dashboard", 
    title="Dashboard", 
    on_load=[AuthState.verificar_token, EstadoDashboard.obtener_peliculas]
)
def paginaDashboard() -> rx.Component:

    return rx.container(
        navbar_dashboard(),
        rx.cond(
            EstadoDashboard.cargando,
            rx.center(rx.text("Cargando...")),
            rx.vstack(
                rx.heading("Películas", size='6', align='center'),
                rx.foreach(
                    EstadoDashboard.peliculas,
                    lambda pelicula: rx.box(
                        rx.link(
                            rx.text(f"Título: {pelicula.titulo}", color="blue", text_decoration="underline"),
                            href=f"/pelicula/{pelicula.id}",
                            on_click=lambda: [AppState.set_pelicula_detalles_id(pelicula.id), AppState.set_user_id_state(AuthState.usuario_actual.get('id', 1))],
                        ),
                        rx.text(f"Descripción: {pelicula.descripcion}"),
                        rx.text(f"Fecha de Lanzamiento: {pelicula.fecha_lanzamiento}"),
                        margin_bottom='1rem',
                        padding='1rem',
                        border='1px solid #ccc',
                        border_radius='8px'
                    ),
                ),
            )
        ),
        width='100%',
    )