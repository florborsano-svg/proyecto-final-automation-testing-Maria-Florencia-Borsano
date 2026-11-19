import pytest
from pathlib import Path #para encontrar archivo csv


#esperas explicitas: para darle exclusividad a 1 elemento para esperar para encontrarlo en el DOM
# por ejemplo boton de Add to cart a Remove
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from pages.LoginPage import LoginPage
from pages.InventoryPage import InventoryPage
from pages.CartPage import CartPage

from pages.ChechOutPage import CheckOutPage

from pages.CheckoutOverview import CheckoutOverview
import csv
import json

from data.datos import datos_checkout #mayor seguridad que esté en otro archivo


from utils.helpers import logger

RUTA_CSV = ( 
    Path(__file__).resolve().parents[1] # _file_ : ruta donde esta parado el archivo test_saucedemo.py || parents[1] sube 2 niveles 0 y 1, ahi quedo en el raiz "Prelab..."
    /"data" 
    /"usuarios.csv" #guarda la ruta absoluta del archivo, usando la libreria pathlib
)


RUTA_JSON = ( 
    Path(__file__).resolve().parents[1] # _file_ : ruta donde esta parado el archivo test_saucedemo.py || parents[1] sube 2 niveles 0 y 1, ahi quedo en el raiz "Prelab..."
    /"data" 
    /"productos.json"
) 



def leer_datos_csv():
    datos = [] #lista vacia en donde voy a incrustar los datos del archivo csv, para que phyton lo interprete
    with open(RUTA_CSV,mode = 'r', newline='',encoding='utf-8') as archivo: # with: abre y cierra archivo, mode = 'r' en modo lectura, newline = interprete linea vacia como quiera
       lectura = csv.DictReader(archivo) #CONVERTIR CADA FILA DE texto plano a 1 lista con N diccionario/tupla, primer fila es la clave (usuario,password)
       #print(lectura)
       for fila in lectura:
            usuario = fila['usuario']
            password = fila['password']
            debe_funcionar = fila['debe_funcionar'] 
            datos.append((usuario,password,debe_funcionar))            
    #print(datos)
    return datos

def leer_datos_json():
    datos = [] #lista vacia en donde voy a incrustar los datos del archivo json, para que phyton lo interprete
    lista_productos = []
    with open(RUTA_JSON,mode = 'r', encoding='utf-8') as archivo: # with: abre y cierra archivo, mode = 'r' en modo lectura, 
        datos = json.load(archivo)
    # print(lectura)
    for fila in datos:
        producto = fila['producto']        
        lista_productos.append((producto))
    return lista_productos




#usando archivo datos.py
#@pytest.mark.parametrize("usuario,password,nombre,apellido,codigo_postal",datos_compra) #para pasarle los datos desde el archivo datos.py
#def test_compra_completa(driver,usuario,password,nombre,apellido,codigo_postal): #se pueden agregar assert 

#usando archivo csv
@pytest.mark.parametrize("usuario,password,debe_funcionar",leer_datos_csv())
def test_login_desde_csv(driver,usuario,password,debe_funcionar): #con el primer set de datos de usuarios.csv: caso negativo
    logger.info("Iniciando login con usuario: %s", usuario)
    login = LoginPage(driver)

    logger.info("Completando credenciales...")
    login.hacer_login(usuario,password)
   
   
    if debe_funcionar == 'True':
        WebDriverWait(driver,10).until(
            EC.url_contains('inventory.html')
         )
        logger.info("Verificando redireccion exitosa")       
        assert "inventory.html" in driver.current_url        
    else:
        logger.info("Verificando redireccion fallida con usuario incorrecto OK")
        

#usando archivo json
@pytest.mark.parametrize("producto",leer_datos_json())
def test_agregar_producto_json(driver,producto):
        inventario = InventoryPage(driver)
        productos = inventario.obtener_productos()
        for i in range(len(productos)): # recorro la lista de productos de la web hasta encontrar la que viene en productos.json
            nombre = inventario.obtener_nombre_producto(i)
            if nombre == producto:
                inventario.agregar_un_producto(i)
                logger.info(f"Agregando producto: {producto}, y esta en la posicion {i} (comenzando desde 0), del inventario de productos de la web")
                break
        print(f"El nombre del producto es: {nombre} y esta en la posicion {i} del inventario de productos de la web")

def test_cantidad_productos_en_carrito(driver):
        inventario = InventoryPage(driver)
        contador = inventario.obtener_contador_carrito()
        logger.info("Verificando contador de carrito: %s",contador)
        assert contador == '2'
        print(f"Hay {contador} producto/s en el carrito")
        

def test_abrir_carrito(driver):
    inventario = InventoryPage(driver)
    inventario.abrir_carrito()
    assert "cart.html" in driver.current_url
    logger.info("Abriendo pagina de carrito")

def test_carrito(driver):
    carrito = CartPage(driver)
    assert carrito.obtener_titulo() == 'Your Cart'
    assert carrito.boton_continuar_compra_visible()

@pytest.mark.parametrize("nombre,apellido,codigo_postal",datos_checkout) #tomo los datos del archivo externo datos.py
def test_checkout(driver,nombre,apellido,codigo_postal):
    checkout = CartPage(driver)
    checkout.ir_a_checkout() 
    completar_datos = CheckOutPage(driver)
    assert completar_datos.obtener_titulo() == 'Checkout: Your Information'
    completar_datos.completar_datos(nombre,apellido,codigo_postal)
    logger.info("Completando datos para checkout")
    completar_datos.continuar()     

def test_OverView(driver):
    overview = CheckoutOverview(driver)
    assert overview.obtener_titulo() == 'Checkout: Overview'
    assert overview.boton_cancel_visible() == True

    overview.finalizar_compra()

    logger.info("Finalizando compra")
    texto_encontrado = overview.obtener_confirmacion()

    # assert exitoso:
    assert texto_encontrado == "Thank you for your order!",f"El mensaje de éxito no coincide. Muestra '{texto_encontrado}'"    
 
    # assert fallido para que falle y guarde captura en reporte:
    
    assert texto_encontrado == "Pongo otro texto para forzar el error y que guarde captura para el reporte",f"El mensaje de éxito no coincide. Muestra '{texto_encontrado}'"
    
  
