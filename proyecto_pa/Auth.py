# Este archivo controlara los inicios de sesion de los usuarios y cokies

import reflex as rx

class AuthState(rx.State):
    auth_token: str = rx.Cookie( name='Authtoken', secure=True )

    @rx.event
    def guardar_token(self, token: str):
        self.auth_token = token

