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
            return {"message": "Conexión exitosa"}
        except Exception as e:
            return {"message": f"Error en la conexión: {e}"}

    def close(self):
        if self.connection:
            self.connection.close()
            print("Conexión cerrada")