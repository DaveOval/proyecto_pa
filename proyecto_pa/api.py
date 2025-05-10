from reflex.server.fastapi import app
from fastapi.responses import JSONResponse

@app.get("/api/products")
async def get_products():
    productos = [
        {"id": 1, "name": "Producto 1", "price": 10.0},
        {"id": 2, "name": "Producto 2", "price": 20.0},
        {"id": 3, "name": "Producto 3", "price": 30.0},
    ]
    return JSONResponse(content=productos)

