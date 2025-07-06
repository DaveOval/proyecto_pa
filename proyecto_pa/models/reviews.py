import reflex as rx

from datetime import datetime

from sqlmodel import Relationship, Field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .usuarios import Usuarios
    from .peliculas import Peliculas

class Reviews(rx.Model, table=True):
    __tablename__ = 'reviews'
    
    id: int = Field(default=None, primary_key=True)
    comentario: str
    calificacion: int = Field(ge=1, le=5)
    creado_en: datetime = Field(default_factory=datetime.now)
    
    # Relación con el usuario que escribió la review
    usuario_id: int = Field(foreign_key='usuarios.id')
    usuario: "Usuarios" = Relationship(back_populates='reviews')
    
    # Relación con la película que se está reseñando
    pelicula_id: int = Field(foreign_key='peliculas.id')
    pelicula: "Peliculas" = Relationship(back_populates='reviews')
    
    
    @classmethod
    def agregar_review(cls, comentario: str, calificacion: int, usuario_id: int, pelicula_id: int):
        return cls(
            comentario=comentario,
            calificacion=calificacion,
            usuario_id=usuario_id,
            pelicula_id=pelicula_id
        )