from reflex import Var
import reflex as rx
from ..models import Peliculas, Reviews
from sqlmodel import select
from ..components.navbar import navbar_dashboard
from proyecto_pa.state.app_state import AppState

class EstadoDetallePelicula(rx.State):
    pelicula: Peliculas = Peliculas()
    cargando: bool = False
    pelicula_id: int = 0
    usuario_id: int = 0
    error: str = ""
    
    async def cargar_pelicula(self):
        self.cargando = True
        
        app_state = await self.get_state(AppState)
        pelicula_id = app_state.pelicula_detalles_id
        self.usuario_id = app_state.user_id_state
        print(f"ID de Película: {pelicula_id}, ID de Usuario: {self.usuario_id }")
        
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
            
    # variables para agregar review
    review_text: str = ""
    review_rating: int = 0
    estado_cargando_review: bool = False

    @rx.event
    def asignar_review_text(self, review_text: str):
        self.review_text = review_text
    @rx.event
    def asignar_review_rating(self, review_rating: str):
        self.review_rating = review_rating
        
    @rx.event
    async def enviar_review(self):
        self.estado_cargando_review = True
        
        if not self.review_text or not self.review_rating:
            print("Por favor, completa todos los campos.")
            self.estado_cargando_review = False
            return
        if int(self.review_rating) < 1 or int(self.review_rating) > 5:
            print("La calificación debe estar entre 1 y 5.")
            self.estado_cargando_review = False
            return
        
        nueva_review = Reviews.agregar_review(
            comentario= self.review_text,
            calificacion= int(self.review_rating),
            usuario_id= int(self.usuario_id),
            pelicula_id= self.pelicula.id
        )
        
        with rx.session() as sesion:
            sesion.add(nueva_review)
            sesion.commit()
            
        self.review_text = ""
        self.review_rating = 0
        self.estado_cargando_review = False
        
        await self.cargar_pelicula()
        
            
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
            rx.box(         
                rx.vstack(
                    rx.heading(EstadoDetallePelicula.pelicula.titulo, size='4', align='center'),
                    rx.text(f"Descripción: {EstadoDetallePelicula.pelicula.descripcion}"),
                    rx.text(f"Fecha de Lanzamiento: {EstadoDetallePelicula.pelicula.fecha_lanzamiento}"),
                    width='100%',
                    padding='1rem',
                    border='1px solid #ccc',
                    border_radius='8px'
                ),
                rx.vstack(
                    rx.heading('Agregar Review', size='5', align='center'),
                    rx.text(
                        "Escribe tu review sobre la película:",
                        font_size='md',
                        font_weight='bold',
                        margin_bottom='0.5rem'
                    ),
                    rx.text_area(
                        placeholder='Escribe tu review aquí...',
                        value=EstadoDetallePelicula.review_text,
                        on_change=EstadoDetallePelicula.asignar_review_text,
                        width='100%'
                    ),
                    rx.text(
                        "Calificación (1-5):",
                        font_size='md',
                        font_weight='bold',
                        margin_bottom='0.5rem'
                    ),
                    rx.input(
                        placeholder='Calificación (1-5)',
                        type='number',
                        value=EstadoDetallePelicula.review_rating,
                        on_change=EstadoDetallePelicula.asignar_review_rating,
                        width='100%',
                        max=5,
                        min=1
                    ),
                    rx.cond(
                        EstadoDetallePelicula.estado_cargando_review,
                        rx.button(
                            rx.hstack(
                                rx.spinner(loading=True),
                                rx.text("Enviando..."),
                            ),
                            disabled=True,
                            width="100%",
                            color_scheme="blue",
                        ),
                        rx.button(
                            "Enviar Review",
                            on_click=EstadoDetallePelicula.enviar_review,
                            width="100%",
                            color_scheme="blue",
                        )
                    ),
                    border='1px solid #ccc',
                    border_radius='8px',
                    padding='1rem',
                    margin_top='1rem',
                ),
            )
        ),
    )