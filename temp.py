import pymysql

def test_local_pymysql(user="root", password=""):
    print(f"Probando conexión local con PyMySQL (usuario='{user}', contraseña='{'***' if password else 'vacía'}')...")
    try:
        conn = pymysql.connect(
            host="127.0.0.1",
            port=3306,
            user=user,
            password=password,
            connect_timeout=3
        )
        print("¡Conectado exitosamente con PyMySQL!")
        
        with conn.cursor() as cursor:
            cursor.execute("SELECT VERSION()")
            version = cursor.fetchone()
            print(f"Versión de MariaDB: {version[0]}")
            
            print("Probando creación de base de datos 'pruebas_local'...")
            cursor.execute("CREATE DATABASE IF NOT EXISTS pruebas_local")
            cursor.execute("USE pruebas_local")
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS test_local (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    mensaje VARCHAR(255)
                )
            """)
            cursor.execute("INSERT INTO test_local (mensaje) VALUES ('Conexión local exitosa con PyMySQL')")
            conn.commit()
            
            cursor.execute("SELECT * FROM test_local")
            print("Filas encontradas:")
            for row in cursor.fetchall():
                print(f" - {row}")
                
            cursor.execute("DROP TABLE test_local")
            print("Limpieza completada.")
        conn.close()
        return True
    except Exception as e:
        print(f"Error de conexión local con PyMySQL: {type(e).__name__} - {e}")
        return False

test_local_pymysql()