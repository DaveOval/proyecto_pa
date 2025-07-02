import reflex as rx

from appconfig import APP_NAME, URL_POSTGRES_URL


config = rx.Config(
    app_name = APP_NAME,
    db_url=URL_POSTGRES_URL,
)