# Propósito del proyecto:

Testear el correcto funcionamiento de la web https://www.saucedemo.com , contemplando el proceso de Login, navegación y verificación del catálogo y la interacción con productos, utilizando objetos como estructura principal para los tests.

## 🛠️ Tecnologías utilizadas
- Python como lenguaje principal
- Pytest para estructura de testing
- Selenium WebDriver para automatización
- Git y GitHub para control de versiones

## 📦 Instalación
1. Clona el repositorio:
   ```bash
   git clone https://github.com/florborsano-svg/proyecto-final-automation-testing-Maria-Florencia-Borsano
   cd Tests-UI
   ```
2. Instala las dependencias:
   - Desde la terminal "pip install selenium"
   - Desde la terminal "pip install webdriver-manager"
   - Desde la terminal "pip install pytest"
   - Desde la terminal "pip install pytest-HTML"


## 📊 Datos Externos 

El proyecto utiliza fuentes de datos externas para parametrizar los casos de prueba y evitar valores fijos (*hardcoded*) en el código.

* **Ubicación:** Todos los archivos de prueba se encuentran en la carpeta `data/` 
* **Formato utilizado:** Archivos `.csv` , `.json` codificados en UTF-8, y datos.py.

### Archivos principales

| Archivo | Propósito | Campos principales |
| `usuarios.csv` | Credenciales para pruebas de login exitoso y fallido. | `usuario`, `password`, `debe_funcionar` |
| `productos.json` | Datos para validar el flujo de búsqueda y carrito. | `nombre`|
| `datos.py` | Datos que se utilizan en el proceso de checkout. | `nombre` | `apellido` | `Codigo Postal` | 


## 🚀 Comando para ejecutar las pruebas
"pytest -v"

## 👤 Autor
Maria Florencia Borsano - [https://github.com/florborsano-svg](https://github.com)

