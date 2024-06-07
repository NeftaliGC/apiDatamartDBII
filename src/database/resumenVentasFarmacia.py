from src.database.Connection import Connection

class ResumenVentasFarmacia:

    def __init__(self, fecha_inicio=None, fecha_fin=None, nombre_producto=None):
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.nombre_producto = nombre_producto

    def getResumenVentasFarmacia(self):
        try:
            self.connection = Connection()
            self.connection.connect()
            cursor = self.connection.connection.cursor()
            cursor.execute(
                f"SELECT * FROM resumen_ventas_farmacia('{self.fecha_inicio}', '{self.fecha_fin}', '{self.nombre_producto}')"
            )
            data = cursor.fetchall()
            self.connection.close()
            return data
        except Exception as e:
            return {"message": f"Error en la consulta: {e}"}

    def getResumenCompletoVentasFarmacia(self):
        try:
            self.connection = Connection()
            self.connection.connect()
            cursor = self.connection.connection.cursor()
            cursor.execute(
                f"SELECT * FROM resumen_completo_ventas_farmacia()"
            )
            data = cursor.fetchall()
            self.connection.close()
            return data
        except Exception as e:
            return {"message": f"Error en la consulta: {e}"}
