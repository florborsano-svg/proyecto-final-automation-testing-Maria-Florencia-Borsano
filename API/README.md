# Automatización de Pruebas de API con Python y Pytest

Proyecto de automatización de pruebas sobre métodos HTTP (GET, POST, PUT, DELETE) desarrollado como proyecto final del curso de QA Automation.

## API utilizada: https://jsonplaceholder.typicode.com/posts y /users

## 🛠️ Tecnologías utilizadas
* **Lenguaje:** Python 3.11+
* **Framework de testing:** Pytest
* **Librería HTTP:** Requests utilizados en `metodo_http.py`

## 📁 Estructura del proyecto
```text
API/
├── metodo_http.py          # Funciones con las peticiones HTTP a la API
├── pytest.ini              # Configuración de rutas para Pytest
├── .gitignore              # Archivos ignorados por Git
└── logs/                   # se graban los logs en archivo suit.log
└── tests/
    ├── __init__.py
    └── test_metodo_http.py # Casos de prueba automatizados
└── utils/
    ├──helpers.py           # Configuracion del logging
```

## 🚀 Instalación y configuración

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/florborsano-svg/proyecto-final-automation-testing-Maria-Florencia-Borsano
   cd API
   ```

2. **Instalar las dependencias:**
   ```bash
   pip install requests
   ```
   

## 🧪 Ejecución de las pruebas

Para correr toda la suite de pruebas con detalle en consola, ejecutá desde la raíz del proyecto:
```bash
pytest -v -s 
```

## 📋 Casos de prueba cubiertos
* **GET:** Obtención de listado de publicaciones, publicación específica y primer usuario.
* **POST:** Creación de una nueva publicación.
* **PUT / PATCH:** Actualización de la primera publicación.
* **DELETE:** Eliminación de una publicación existente.
* **Manejo de errores:** Validación de respuesta ante un endpoint inexistente (404).

---
Desarrollado por *Maria Florencia Borsano**
