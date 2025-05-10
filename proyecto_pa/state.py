import reflex as rx
import requests

class ProductoState(rx.State):
    productos: list[dict] = []

    @rx.event
    def cargar_productos(self):
        try:
            respuesta = requests.get("http://localhost:3000/api/productos")
            if respuesta.status_code == 200:
                self.productos = respuesta.json()
        except Exception as e:
            print("Error al obtener productos:", e)
