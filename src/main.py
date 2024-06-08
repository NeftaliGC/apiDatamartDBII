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
############################################################################################################

# Dense Ranking de ventas - TESTEADO
@app.get("/denserankingVentas")
def resumen_ventas_producto(fecha_inicio: str, fecha_fin: str):
    fun = Functions()
    return fun.dense_rank_producto(fecha_inicio, fecha_fin)

@app.get("/denserankingVentasGrafico")
def resumen_ventas_productoGrafico(fecha_inicio: str, fecha_fin: str):
    fun = Functions()
    buf = fun.get_graphic_dense_ranking(fun.dense_rank_producto(fecha_inicio, fecha_fin))
    if isinstance(buf, dict):
        return buf
    return StreamingResponse(buf, media_type='image/png')

@app.get("/denserankingCompletoVentas")
def resumen_completo_ventas_producto():
    fun = Functions()
    return fun.dense_rank_completo_producto()

@app.get("/denserankingCompletoVentasGrafico")
def resumen_completo_ventas_productoGrafico():
    fun = Functions()
    buf = fun.get_graphic_dense_ranking(fun.dense_rank_completo_producto())
    if isinstance(buf, dict):
        return buf
    return StreamingResponse(buf, media_type='image/png')
############################################################################################################


# Ranking de ventas - TESTEADO
@app.get("/rankingVentas")
def resumen_ventas_producto(fecha_inicio: str, fecha_fin: str):
    fun = Functions()
    return fun.rank_producto(fecha_inicio, fecha_fin)

@app.get("/rankingVentasGrafico")
def resumen_ventas_productoGrafico(fecha_inicio: str, fecha_fin: str):
    fun = Functions()
    buf = fun.get_graphic_rank_producto(fecha_inicio, fecha_fin)
    if isinstance(buf, dict):
        return buf
    return StreamingResponse(buf, media_type='image/png')

@app.get("/rankingCompletoVentas")
def resumen_completo_rank_producto():
    fun = Functions()
    return fun.rank_completo_producto()

@app.get("/rankingCompletoVentasGrafico")
def resumen_completo_rank_productoGrafico():
    fun = Functions()
    buf = fun.get_graphic_rank_completo_producto()
    if isinstance(buf, dict):
        return buf
    return StreamingResponse(buf, media_type='image/png')
############################################################################################################

# Resumen de ventas por farmacia - TESTEADO
@app.get("/resumenVentasFarmacia")
def resumen_ventas_farmacia(fecha_inicio: str, fecha_fin: str):
    fun = Functions()
    return fun.resumen_ventas_farmacia(fecha_inicio, fecha_fin)

@app.get("/resumenVentasFarmaciaGrafico")
def resumen_ventas_farmaciaGrafico(fecha_inicio: str, fecha_fin: str):
    fun = Functions()
    buf = fun.get_graphic_resumen_ventas_farmacia(fecha_inicio, fecha_fin)
    if isinstance(buf, dict):
        return buf
    return StreamingResponse(buf, media_type='image/png')

@app.get("/resumenCompletoVentasFarmacia")
def resumen_completo_ventas_farmacia():
    fun = Functions()
    return fun.resumen_completo_ventas_farmacia()

@app.get("/resumenCompletoVentasFarmaciaGrafico")
def resumen_completo_ventas_farmaciaGrafico():
    fun = Functions()
    buf = fun.get_graphic_venta_farmacia()
    if isinstance(buf, dict):
        return buf
    return StreamingResponse(buf, media_type='image/png')

############################################################################################################


# Desglose de ventas por producto - TESTEADO
@app.get("/desgloseVentasProducto")
def desglose_ventas_producto(fecha_inicio: str, fecha_fin: str):
    fun = Functions()
    return fun.desglose_ventas_producto(fecha_inicio, fecha_fin)

@app.get("/desgloseVentasProductoGrafico")
def desglose_ventas_productoGrafico(fecha_inicio: str, fecha_fin: str):
    fun = Functions()
    buf = fun.get_graphic_ventas_producto(fecha_inicio, fecha_fin)
    if isinstance(buf, dict):
        return buf
    return StreamingResponse(buf, media_type='image/png')

@app.get("/desgloseCompletoVentasProducto")
def desglose_completo_ventas_producto():
    fun = Functions()
    return fun.desglose_completo_ventas_producto()

@app.get("/desgloseCompletoVentasProductoGrafico")
def desglose_completo_ventas_productoGrafico():
    fun = Functions()
    buf = fun.get_graphic_desglose_completo()
    if isinstance(buf, dict):
        return buf
    return StreamingResponse(buf, media_type='image/png')

