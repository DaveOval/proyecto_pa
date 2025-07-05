# Controlar toda la información de los usuarios

import reflex as rx

import bcrypt

from sqlmodel import Field

class Usuarios(rx.Model, table=True):
    __tablename__ = "usuarios"
    id: int = Field(default=None, primary_key=True)
    nombre: str
    email: str
    password: str
    role: str = Field(default='user')
    status: str = Field(default='active')
    
    @classmethod
    def crear_usuario(cls,  nombre_usuario, correo_usuario, pass_usuario):
        # Encriptar la contraseña
        pass_codificada = pass_usuario.encode()
        pass_hasheada = bcrypt.hashpw(pass_codificada, bcrypt.gensalt())

        return cls( nombre=nombre_usuario, email=correo_usuario, password=pass_hasheada.decode())