# 2026-06-17 Masterclass

## Gestor de dependencias
**Mise** como gestor de dependencias y también para administrar diferentes versiones de python

## UV Sustituto de pip
Para instalar en windows:
```shell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/0.11.21/install.ps1 | iex"
```

Para inicializar un proyecto
```shell
uv init --python 3.12.13
```

### instalar dependencias
```shell
uv add colorama
```

### Arrancar el proyecto
```shell
uv run main.py
```

## Enlaces
* mise.jdx.dev => Gestor de dependencias para python y node
* Repositorio del curso:https://github.com/Baxone/python_avanzado.git
* https://docs.astral.sh/uv/ => Gestor de dependencias