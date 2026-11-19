import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pathlib import Path
import re
import base64
import pytest_html

@pytest.fixture(scope="module") #esto hace que los test se ejecuten uno atras del otro
def driver():
    service = Service(ChromeDriverManager().install())

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    
    # Desactivar el popup de contraseñas comprometidas
    # credentials_enable_service: Apaga el gestor de contraseñas nativo
    # profile.password_manager_leak_detection: Apaga la detección de filtraciones de Google
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_leak_detection": False,
        "profile.password_manager_enabled": False
    }
    options.add_experimental_option("prefs", prefs)
    
    # Adicionalmente, desactiva infobars generales de Chrome
    options.add_argument("--disable-infobars")

# 🌟 ESTA LÍNEA CLAVE evita que Chrome se cierre al terminar Python
    options.add_experimental_option("detach", True) 

    driver = webdriver.Chrome(service=service, options=options)

    #driver = webdriver.Chrome(service=service)
    driver.get("https://www.saucedemo.com/")

    yield driver 

    driver.quit()

#Personalizar el titulo del reporte (hook)
def pytest_html_report_title(report):
    report.title = "Proyecto Final: Reporte de automatización - Sauce Demo"

# funcion para captura de pantallas en los reportes cuando falla 1 test
#decorador crear hook rapper, esperar hasta que el proceso suceda y crear captura
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    resultado = yield 
    reporte = resultado.get_result()
    # reporte.when # en que fase estamos:

    #reporte.setup: inicializacion
    #reporte.call: armado de reporte
    #reporte.teardown finalizacion

    if reporte.when == "call" and reporte.failed: # cuando se esta ejecutando el test y hay un fallo: hago captura
        #necesito comunicarme con el driver de selenium para hacer la captura
        driver = item.funcargs.get("driver") #diccionario: donde almacena los fixture utilizados por el test
        #item.funcargs["driver]" devuelve un keyerror, en cambio el gte devuelve none, conviene poner get para que no corte la ejecucion
        if driver:
            carpeta = Path("reports/screenshots") #ruta 
            carpeta.mkdir(parents=True, exist_ok=True) #crea carpeta , si no existe reports, lo crea y si ya existe no generes error}
            nombre = re.sub( #para darle nombre al screenshot
                r"[^a-zA-Z0-9_-]",
                "_",
                item.nodeid
            )
            #screenshots/test_saucedemo....png
            ruta_captura = carpeta / f"{nombre}.png"

            driver.save_screenshot(str(ruta_captura)) # guardamos captura en la carpeta

            imagen_base64 = base64.b64encode( #la pasa a base64
                ruta_captura.read_bytes()
            ).decode("utf-8")

            
           

            extras = getattr(reporte,"extras",[]) #es una lista de capturas
            
            #las agrego al reporte con append
                             
            extras.append(
                pytest_html.extras.png(
                    imagen_base64,
                    name = "captura de error"
                )
            )

            reporte.extras = extras