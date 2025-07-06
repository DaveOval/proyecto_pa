import reflex as rx

class AppState(rx.State):
    pelicula_detalles_id: int = 0
    user_id_state: int = 0

    def set_pelicula_detalles_id(self, pelicula_id: int):
        self.pelicula_detalles_id = pelicula_id
        
    def set_user_id_state(self, user_id: int):
        self.user_id_state = user_id