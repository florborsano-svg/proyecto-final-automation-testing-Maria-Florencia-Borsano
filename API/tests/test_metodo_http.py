import pytest
from metodo_http import( obtener_endpoint_inexistente, eliminar_publicacion, obtener_publicaciones, obtener_segunda_publicacion, crear_publicacion,obtener_primer_usuario,actualizar_primer_publicacion)

from  pytest_check import check #soft assert (aserciones suaves) #permite continuar los tests. aunque uno falle
import requests

from utils.helpers import logger

BASE = 'https://jsonplaceholder.typicode.com' #quito el /posts/ por si despues tengo que acceder /users

@pytest.fixture()
def post_url():
    return f"{BASE}/posts"

@pytest.fixture()
def users_url():
    return f"{BASE}/users" 

@pytest.fixture()
def users_url_1():
    return f"{BASE}/users/1" 

@pytest.fixture()
def endpoint_inexistente():
    return f"{BASE}/endpoint_inexistente" 

# 1) Tests para publicaciones
def test_get_publicaciones(post_url):
    res = obtener_publicaciones(post_url)
    # verificar que la peticion fue exitosa
    assert res.status_code == 200
    # convertir la respuesta a 1 lista 
    datos = res.json()

    # cuando actuo sobre todas las publicaciones, el get > json devuelve 1 lista
    assert isinstance(datos,list) # verificar que lo que devuelva la api con el get sea 1 lista

    #verificar longitud de la lista

    assert len(datos) > 0

    logger.info("test_get_publicaciones: Iniciando validación de estructura")

 # validar estructura: los nombres de los campos de la lista

    for post in datos:
        assert "userId" in post
        assert "id" in post
        assert "title" in post
        assert "body" in post
    
    logger.info("test_get_publicaciones: Iniciando validación de datos")
    # validar tipos de datos de la lista:
    for post in datos:
        assert post["userId"] > 0  #validar que el userId sea >0
        assert isinstance(post["body"],str) # validar que el body sea 1 string
        assert isinstance(post["id"],int) #validar que el id sea 1 entero

    #verificar contenido del primer elemento de la lista

    primer_post = datos[0]

    assert primer_post["userId"] == 1 
    assert primer_post["title"] == 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit'

def test_crear_publicacion(post_url):
     res = crear_publicacion(post_url)
     assert res.status_code == 201
     datos_agregados = res.json()
     print (datos_agregados)

     logger.info("test_crear_publicacion: Iniciando validación de estructura")
     #validar estructura
     assert isinstance(datos_agregados,dict)
     assert "id" in datos_agregados
     assert "title" in datos_agregados
     assert "body" in datos_agregados
     assert "userId" in datos_agregados

     #validar datos
     logger.info("test_crear_publicacion: Iniciando validación de datos")
     assert datos_agregados["id"] == 101
     assert datos_agregados["title"] == "Mi primer envio de datos"
     assert datos_agregados["body"] == "estoy probando el post"
     assert datos_agregados ["userId"] == 1


def test_obtener_segunda_publicacion(post_url):
     res = obtener_segunda_publicacion(post_url)
     assert res.status_code == 200
     datos = res.json()

     # validar estructura
     logger.info("test_obtener_segunda_publicacion: Iniciando validación de estructura")
     assert isinstance(datos,dict)
     assert "userId" in datos
     assert "id" in datos
     assert "title" in datos
     assert "body" in datos

     # valido contenido del elemento:
     logger.info("test_obtener_segunda_publicacion: Iniciando validación de datos")
     assert datos['userId'] == 1
     assert datos['id'] == 2
     assert datos['title'] == "qui est esse"
     assert datos['body'] == "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"

def test_actualizar_primer_publicacion(post_url):
     res = actualizar_primer_publicacion(post_url)
     assert res.status_code == 200

     datos = res.json()

     # valido estructura:
     logger.info("test_actualizar_primer_publicacion: Iniciando validación de estructura")
     assert isinstance(datos,dict)
     assert "userId" in datos
     assert "id" in datos
     assert "title" in datos
     assert "body" in datos

     # valido contenido del elemento:
     logger.info("test_actualizar_primer_publicacion: Iniciando validación de datos")
     assert datos['userId'] == 2
     assert datos['id'] == 1
     assert datos['title'] == "Datos actualizados"
     assert datos['body'] == "estoy probando el put"

def test_eliminar_publicacion(post_url):
     respuesta = eliminar_publicacion (post_url)
     assert respuesta.status_code == 200
     datos = respuesta.json()
     logger.info("test_eliminar_publicacion: Iniciando validación de estructura")
     assert isinstance(datos,dict)

############################################################################################

# 2) Tests para usuarios

def test_datos_primer_usuario(users_url):
        res = obtener_primer_usuario(users_url)
        assert res.status_code == 200 
    # pasa por todos los check aunque alguno falle, llega hasta el ultimo check y solo muestra los que fallaron
        datos = res.json()
        assert isinstance(datos,dict) # si actuo sobre 1 solo elemento el get > json devuelve 1 dict

        # validacion de estructura de algunos campos:
        logger.info("test_datos_primer_usuario: Iniciando validación de estructura")
        assert "name" in datos
        assert "email" in datos
        assert "username" in datos
        assert "address" in datos

        direccion = datos.get("address") # adress a su vez es un diccionario dentro del diccionario datos
        assert isinstance(direccion,dict)
        
        print(f"LA DIRECCION ES {direccion}")

        # validacion de datos
        logger.info("test_datos_primer_usuario: Iniciando validación de datos")

        assert direccion.get('street') == 'Kulas Light' # la calle dentro del diccionario direccion
               
        check.equal(datos.get("name"), "Leanne Graham", msg="Fallo en Nombre")
    
        
        check.equal(datos.get("email"), "Sincere@april.biz", msg="Fallo en Email")
    
        
        check.equal(datos.get("username"), "Bret", msg="Fallo en Username")

        # poner en consola "pytest -v -s" para imprimir los print


#el check o el assert puedo usar cualquiera ya que lo realiza 3 veces, 1 por cada valor
@pytest.mark.parametrize("campo,esperado",[
   ("name","Leanne Graham"),
   ("email","Sincere@april.biz"),
   ("username","Bret")
])
def test_obtener_usuario_usando_check(users_url_1,campo,esperado):
     respuesta = requests.get(users_url_1)
     assert respuesta.status_code == 200
     datos = respuesta.json()

    # validacion de estructura de algunos campos
     logger.info("test_obtener_usuario_usando_check: Iniciando validación de estructura")
     assert "name" in datos
     assert "email" in datos
     assert "username" in datos
     assert "address" in datos

    # validacion de contenido de datos     
     logger.info("test_obtener_usuario_usando_check: Iniciando validación de datos")
     assert datos[campo] == esperado
     check.equal(datos[campo],esperado)


# para verificar error en el get > endpoint inexistente que es 404
def test_obtener_endpoint_inexistente(endpoint_inexistente):
    respuesta = obtener_endpoint_inexistente(endpoint_inexistente)
    logger.info("test_obtener_endpoint_inexistente: Iniciando validación de status code")
    assert respuesta.status_code == 404
     
         
     

        



    
    
