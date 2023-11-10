import sqlite3

class base_datos:
    def __init__(self, database_name):
        self.database_name = database_name

    def create_table(self):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tabla (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                dato TEXT
            )
        ''')

        conn.commit()
        conn.close()

    def insert_data(self, dato):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        cursor.execute('INSERT INTO tabla (dato) VALUES (?)', (dato,))

        conn.commit()
        conn.close()
        return "Registro insertado correctamente"

    def get_data(self):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        cursor.execute('SELECT dato FROM tabla')
        datos = [row[0] for row in cursor.fetchall()]

        conn.close()
        return datos

if __name__ == "__main__":
    # Ejemplo de uso
    db_client = base_datos("mi_base_de_datos.db")

    # Crear la tabla
    db_client.create_table()

    # Insertar datos
    #db_client.insert_data("Dato 1")
    #db_client.insert_data("Dato 2")

    # Obtener los datos
    datos = db_client.get_data()
    print(datos)
