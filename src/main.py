from fastapi import FastAPI
from src.functions.functions import Functions

app = FastAPI()

@app.get("/")
def read_root():
    fun = Functions()
    print(fun)
    return fun.connect()

@app.get("/resumenVentasProducto")
def resumen_ventas_producto(fecha_inicio: str, fecha_fin: str, nombre_producto: str):
    fun = Functions()
    return fun.resumen_ventas_producto(fecha_inicio, fecha_fin, nombre_producto)
