# Este archivo controlara los inicios de sesion de los usuarios y cokies
import jwt 

import reflex as rx

from appconfig import LLAVE_SECRETA

class AuthState(rx.State):
    auth_token: str = rx.Cookie( name='auth_token', secure=True )
    esta_cargando: bool = False

    @rx.event
    def guardar_token(self, token: str):
        self.auth_token = token

    @rx.event
    def verificar_token(self):
        print("Verificando token...")
        self.esta_cargando = True

        
        if not self.auth_token or len(self.auth_token) == 0:
            print("El usuario no tiene token")
            self.esta_cargando = False
            return rx.redirect("/login")
        
        else:
            try:
                token_decoficiado = jwt.decode(self.auth_token, LLAVE_SECRETA, algorithms=['HS256'])
                print(token_decoficiado)
                self.esta_cargando = False
                return None
            except jwt.ExpiredSignatureError:
                print("El token ha expirado")
                self.esta_cargando = False
                return rx.redirect("/login")
            except jwt.InvalidTokenError:
                print("El token no es valido")
                self.esta_cargando = False
                return rx.redirect("/login")
            
    @rx.event
    def verificar_usuario(self):
        if not self.auth_token or len(self.auth_token) == 0:
            print("El usuario no tiene token... quedate en inicio de sesion")

        else:
            try:
                token_decoficiado = jwt.decode(self.auth_token, LLAVE_SECRETA, algorithms=['HS256'])
                return rx.redirect("/dashboard")
            
            except jwt.PyJWTError:
                print("El token no es valido")
    
    @rx.event
    def cerrar_sesion(self):
        print('Cerrando sesion...')
        self.auth_token = ""
        rx.remove_cookie("auth_token")
        
        return rx.redirect("/login")

