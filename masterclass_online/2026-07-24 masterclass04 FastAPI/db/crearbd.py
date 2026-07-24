import sqlite3
from pathlib import Path


def main() -> None:
    script_dir = Path(__file__).resolve().parent
    candidates = [
        script_dir / "biblioteca_crear_bd.sql",
        script_dir / "biblioteca_crear_db.sql",
        script_dir.parent / "biblioteca_crear_bd.sql",
        script_dir.parent / "biblioteca_crear_db.sql",
    ]

    sql_file = next((path for path in candidates if path.exists()), None)

    if sql_file is None:
        raise FileNotFoundError(
            "No se encontró el archivo SQL 'biblioteca_crear_bd.sql' ni 'biblioteca_crear_db.sql'. "
            "Coloca el archivo en el directorio db o en el directorio padre."
        )

    db_file = script_dir / "biblioteca.db"

    with sql_file.open("r", encoding="utf-8") as file:
        sql_script = file.read()

    with sqlite3.connect(db_file) as connection:
        connection.executescript(sql_script)

    print(f"Base de datos creada en: {db_file}")


if __name__ == "__main__":
    main()
