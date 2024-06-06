import psycopg2
import json

class Connection:
    def __init__(self):
        with open("src/config/config.json") as file:
            data = json.load(file)

        self.Host = data[0].get("Host")
        self.User = data[0].get("User")
        self.Password = data[0].get("Password")
        self.Database = data[0].get("Database")
        self.Port = data[0].get("Port")

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=self.Host,
                user=self.User,
                password=self.Password,
                database=self.Database,
                port=self.Port
            )
            schema_status = self.changeSchema("farma")
            print(schema_status)
            
            return {"message": f"Conexión exitosa en schema"}
        except Exception as e:
            return {"message": f"Error en la conexión: {e}"}

    def changeSchema(self, schema):
        try:
            self.connection.set_session(autocommit=True)
            cursor = self.connection.cursor()
            cursor.execute(f"SET search_path TO {schema}")
            return {"message": "Schema cambiado"}
        except Exception as e:
            return {"message": f"Error al cambiar el schema: {e}"}

    def close(self):
        if self.connection:
            self.connection.close()
            print("Conexión cerrada")