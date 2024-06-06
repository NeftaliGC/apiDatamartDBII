from fastapi import FastAPI
from src.functions.functions import Functions
from fastapi.responses import FileResponse, StreamingResponse
import matplotlib.pyplot as plt
import os

app = FastAPI()

@app.get("/")
def read_root():
    fun = Functions()
    print(fun)
    return fun.connect()

@app.get("/test")
def test():
    return {"message": "Funciona correctamente"}
    
@app.get("/resumenVentasProducto")
def resumen_ventas_producto(fecha_inicio: str, fecha_fin: str, nombre_producto: str):
    fun = Functions()
    return fun.resumen_ventas_producto(fecha_inicio, fecha_fin, nombre_producto)

@app.get("/resumenCompletoVentasProducto")
def resumen_completo_ventas_producto():
    fun = Functions()
    return fun.resumen_completo_ventas_producto()

@app.get("/resumenVentasFarmacia")
def resumen_ventas_farmacia(fecha_inicio: str, fecha_fin: str, nombre_producto: str):
    fun = Functions()
    return fun.resumen_ventas_farmacia(fecha_inicio, fecha_fin, nombre_producto)

@app.get("/resumenCompletoVentasFarmacia")
def resumen_completo_ventas_farmacia():
    fun = Functions()
    buf = fun.get_graphic_venta_farmacia()
    if isinstance(buf, dict):
        return buf
    return StreamingResponse(buf, media_type='image/png')

@app.get("/desgloseVentasProducto")
def desglose_ventas_producto(fecha_inicio: str, fecha_fin: str, nombre_producto: str):
    fun = Functions()
    return fun.desglose_ventas_producto(fecha_inicio, fecha_fin, nombre_producto)

@app.get("/desgloseCompletoVentasProducto")
def desglose_completo_ventas_producto():
    fun = Functions()
    buf = fun.get_graphic_desglose()
    if isinstance(buf, dict):
        return buf
    return StreamingResponse(buf, media_type='image/png')

