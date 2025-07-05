# Controlar toda la información de los usuarios

import reflex as rx

import bcrypt

from sqlmodel import Field, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .peliculas import Peliculas
    from .reviews import Reviews

class Usuarios(rx.Model, table=True):
    __tablename__ = "usuarios"
    
    id: int = Field(default=None, primary_key=True)
    nombre: str
    email: str
    password: str
    role: str = Field(default='user')
    status: str = Field(default='active')
    
    # Relación con películas creadas por el usuario
    peliculas_creadas: list["Peliculas"] = Relationship(
        back_populates="creador_por",
        sa_relationship_kwargs={"cascade": "all, delete-orphan"}
    )
    
    # Relación con reviews escritas por el usuario
    reviews: list["Reviews"] = Relationship(
        back_populates="usuario",
        sa_relationship_kwargs={"cascade": "all, delete-orphan"}
    )
    
    @classmethod
    def crear_usuario(cls,  nombre_usuario, correo_usuario, pass_usuario):
        
        # Encriptar la contraseña
        pass_codificada = pass_usuario.encode()
        pass_hasheada = bcrypt.hashpw(pass_codificada, bcrypt.gensalt())

        return cls( nombre=nombre_usuario, email=correo_usuario, password=pass_hasheada.decode())