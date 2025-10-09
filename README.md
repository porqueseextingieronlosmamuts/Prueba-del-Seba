# Registro de Visitas

Este proyecto es una aplicación web desarrollada con Django para gestionar el registro de visitas. Permite crear, listar, editar y eliminar registros de visitas, almacenando la información en una base de datos SQLite.

## ¿Qué hace?
- Permite registrar nuevas visitas con datos relevantes (nombre, motivo, hora de entrada y salida, etc.). La hora de salida se calcula automáticamente sumando 2 horas a la hora de entrada.
- Muestra una lista de todas las visitas registradas.
- Permite ver el detalle de cada visita.
- Permite editar y eliminar visitas existentes.

## ¿Cómo funciona?
- **Backend:** Utiliza Django como framework principal. La lógica de negocio está en la app `Visitas`, que contiene modelos, vistas, formularios y URLs. El modelo `Visita` incluye una propiedad que muestra la hora de entrada y la hora de salida (2 horas después de la entrada) en un solo campo para facilitar la visualización.
- **Base de datos:** Usa SQLite por defecto (`db.sqlite3`).
- **Frontend:** Utiliza plantillas HTML ubicadas en `Visitas/templates/Visitas/` para mostrar la información y formularios al usuario.
- **Rutas:** Las URLs están definidas en `Registro/urls.py` y `Visitas/urls.py`.

## ¿Cuándo funciona?
- Funciona correctamente cuando se ejecuta el servidor de desarrollo de Django (`python manage.py runserver`).
- Requiere tener Python y Django instalados.
- La base de datos debe estar migrada (usar `python manage.py migrate`).

## ¿Por qué funciona?
- Utiliza el patrón Modelo-Vista-Template de Django, separando la lógica de datos, la lógica de negocio y la presentación.
- Django gestiona la seguridad, las migraciones de base de datos y la validación de formularios.
- El código está estructurado en módulos claros: modelos para la base de datos, vistas para la lógica, formularios para la entrada de datos y plantillas para la interfaz de usuario.

## Estructura del proyecto
```
Registro/
├── db.sqlite3
├── manage.py
├── Registro/
│   ├── settings.py
│   ├── urls.py
│   └── ...
└── Visitas/
    ├── models.py
    ├── views.py
    ├── forms.py
    ├── urls.py
    ├── templates/
    │   └── Visitas/
    │       ├── base.html
    │       ├── lista_visitas.html
    │       ├── nueva_visita.html
    │       ├── detalle_visita.html
    │       ├── editar_visita.html
    │       └── eliminar_visita.html
    └── ...
```

## Instalación y uso
1. Clona el repositorio.
2. Crea y activa un entorno virtual con `python -m venv venv` y actívalo:
    - En Windows: `venv\Scripts\activate`
    - En Linux/Mac: `source venv/bin/activate`
3. Instala las dependencias: `pip install django`.
4. Realiza las migraciones: `python manage.py migrate`.
5. Ejecuta el servidor: `python manage.py runserver`.
6. Accede a la aplicación en `http://127.0.0.1:8000/`.

## Contacto
Para dudas o sugerencias, contacta al autor del repositorio.
