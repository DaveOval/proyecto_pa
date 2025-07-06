from reflex import Var
import reflex as rx
from ..models import Peliculas
from sqlmodel import select
from ..components.navbar import navbar_dashboard
from proyecto_pa.state.app_state import AppState

class EstadoDetallePelicula(rx.State):
    pelicula: Peliculas = Peliculas()
    cargando: bool = False
    pelicula_id: int = 0

    async def cargar_pelicula(self):
        self.cargando = True
        
        app_state = await self.get_state(AppState)
        pelicula_id = app_state.pelicula_detalles_id
        
        try:
            with rx.session() as sesion:
                resultado = sesion.exec(select(Peliculas).where(Peliculas.id == pelicula_id))
                self.pelicula = resultado.first()
                if not self.pelicula:
                    print(f"No se encontró la película con ID: {pelicula_id}")
                
        except Exception as e:
            print(f"Error al cargar la película: {e}")
            
        finally:
            self.cargando = False
            
@rx.page(
    route="/pelicula/[id]",
    title="Detalle de Película",
    on_load=[EstadoDetallePelicula.cargar_pelicula],
)
def detalle_pelicula() -> rx.Component:
    return rx.container(
        navbar_dashboard(),
        rx.cond(
            EstadoDetallePelicula.cargando,
            rx.center(rx.text("Cargando...")),
            rx.vstack(
                rx.heading(EstadoDetallePelicula.pelicula.titulo, size='4', align='center'),
                rx.text(f"Descripción: {EstadoDetallePelicula.pelicula.descripcion}"),
                rx.text(f"Fecha de Lanzamiento: {EstadoDetallePelicula.pelicula.fecha_lanzamiento}"),
                width='100%',
                padding='1rem',
                border='1px solid #ccc',
                border_radius='8px'
            ),
        ),
    )