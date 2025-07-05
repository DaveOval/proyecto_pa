import reflex as rx

from datetime import date

from sqlmodel import Relationship, Field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .usuarios import Usuarios
    from .reviews import Reviews

class Peliculas(rx.Model, table=True):
    __tablename__ = "peliculas"
    
    id: int = Field(default=None, primary_key=True)
    titulo: str
    descripcion: str = Field(default="")
    fecha_lanzamiento: date = Field(default=None)

    # Relación con el usuario que creó la película
    creador_por_id: int = Field(foreign_key="usuarios.id")
    creador_por: "Usuarios" = Relationship(back_populates="peliculas_creadas")
    
    created_at: date = Field(default_factory=date.today)
    
    # Relación con las reviews de esta película
    reviews: list["Reviews"] = Relationship(
        back_populates="pelicula",
        sa_relationship_kwargs={"cascade": "all, delete-orphan"}
    )