from src.database.Connection import Connection

class Ranks:
    def __init__(self, fecha_inicio=None, fecha_fin=None, nombre_producto=None):
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.nombre_producto = nombre_producto
    
    def getDenseRank(self):
        try:
            self.connection = Connection()
            self.connection.connect()
            cursor = self.connection.connection.cursor()
            cursor.execute(
                f"SELECT * FROM obtener_ranking_productos_mas_vendidos('{self.fecha_inicio}', '{self.fecha_fin}')"
            )
            data = cursor.fetchall()
            self.connection.close()
            return data
        except Exception as e:
            return {"message": f"Error en la consulta: {e}"}

    def getDenseRankCompleto(self):
        try:
            self.connection = Connection()
            self.connection.connect()
            cursor = self.connection.connection.cursor()
            cursor.execute(
                f"SELECT * FROM obtener_ranking_completo_productos_mas_vendidos()"
            )
            data = cursor.fetchall()
            self.connection.close()
            return data
        except Exception as e:
            return {"message": f"Error en la consulta: {e}"}

    def getRank(self):
        try:
            self.connection = Connection()
            self.connection.connect()
            cursor = self.connection.connection.cursor()
            cursor.execute(
                f"SELECT * FROM obtener_ranking_productos_mas_vendidos_notdense('{self.fecha_inicio}', '{self.fecha_fin}')"
            )
            data = cursor.fetchall()
            self.connection.close()
            return data
        except Exception as e:
            return {"message": f"Error en la consulta: {e}"}


    def getRankCompleto(self):
        try:
            self.connection = Connection()
            self.connection.connect()
            cursor = self.connection.connection.cursor()
            cursor.execute(
                f"SELECT * FROM obtener_ranking_productos_mas_vendidos_notdense()"
            )
            data = cursor.fetchall()
            self.connection.close()
            return data
        except Exception as e:
            return {"message": f"Error en la consulta: {e}"}