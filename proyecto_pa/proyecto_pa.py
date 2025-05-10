import reflex as rx
from proyecto_pa.pages import home, about

import proyecto_pa.api 

app = rx.App()
app.add_page(home.home, route="/", title="Inicio")
app.add_page(about.about, route="/about", title="Acerca de")
