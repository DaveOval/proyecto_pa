import reflex as rx
from ..components.navbar import navbar_dashboard
from ..models import Peliculas
from ..Auth import AuthState

class EstadoAgregarPelicula(AuthState):
    titulo_pelicula: str = ""
    descripcion_pelicula: str = ""
    fecha_lanzamiento: str = ""
    cargando: bool = False
    error: bool = False
    
    @rx.event
    def asignar_titulo_pelicula(self, titulo: str):
        self.titulo_pelicula = titulo
        
    @rx.event
    def asignar_descripcion_pelicula(self, descripcion: str):
        self.descripcion_pelicula = descripcion
        
    @rx.event
    def asignar_fecha_lanzamiento(self, fecha: str):
        self.fecha_lanzamiento = fecha
    
    @rx.event
    def agregar_pelicula(self):
        print("Agregando película...")
        self.cargando = True
        self.error = False
        
        if not self.titulo_pelicula or not self.descripcion_pelicula or not self.fecha_lanzamiento:
            print("Error: Todos los campos son obligatorios.")
            self.error = True
            self.cargando = False
            return
        
        # Obtener el ID del usuario autenticado
        usuario_id = self.usuario_actual.get('id', 1)  # Default a 1 si no hay usuario
        print(f"Usuario ID: {usuario_id}")
        
        nueva_pelicula = Peliculas.crear_pelicula(
            titulo_pelicula=self.titulo_pelicula,
            descripcion_pelicula=self.descripcion_pelicula,
            fecha_lanzamiento=self.fecha_lanzamiento,
            creador_por_id=usuario_id
        )
        
        with rx.session() as sesion:
            sesion.add(nueva_pelicula)
            sesion.commit()
        
        # Limpiar los campos después de agregar
        self.titulo_pelicula = ""
        self.descripcion_pelicula = ""
        self.fecha_lanzamiento = ""
        self.cargando = False
        
        return rx.redirect('/dashboard')

@rx.page(route="/agregar-pelicula", title="Agregar Película")
def pagina_agregar_pelicula() -> rx.Component:
    return rx.container(
        navbar_dashboard(),
        rx.center(
            rx.box(
                rx.vstack(
                    rx.heading('Agregar pelicula', size='8', margin_bottom='1rem'),
                    
                    rx.cond(
                        EstadoAgregarPelicula.error,
                        rx.text("Error: Por favor verifica que todos los campos estén completos.", color="red"),
                        rx.text("")
                    ),
                    
                    rx.input(
                        placeholder="Título de la película",
                        type="text",
                        width="100%",
                        id="titulo_pelicula",
                        value=EstadoAgregarPelicula.titulo_pelicula,
                        on_change=EstadoAgregarPelicula.asignar_titulo_pelicula
                    ),
                    
                    rx.text_area(
                        placeholder="Descripción de la película",
                        width="100%",
                        id="descripcion_pelicula",
                        value=EstadoAgregarPelicula.descripcion_pelicula,
                        on_change=EstadoAgregarPelicula.asignar_descripcion_pelicula
                    ),
                    
                    rx.input(
                        placeholder="Fecha de lanzamiento (YYYY-MM-DD)",
                        type="date",
                        width="100%",
                        id="fecha_lanzamiento",
                        value=EstadoAgregarPelicula.fecha_lanzamiento,
                        on_change=EstadoAgregarPelicula.asignar_fecha_lanzamiento
                    ),
                    
                    rx.button(
                        "Agregar Película",
                        on_click=EstadoAgregarPelicula.agregar_pelicula,
                        width="100%",
                        color_scheme="blue",
                    )
                ),
                padding="2rem",
                width="100%",
                max_width="600px",
            ),
            height="100vh",
        )
    )