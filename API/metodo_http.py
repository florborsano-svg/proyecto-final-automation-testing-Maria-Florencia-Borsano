import requests


#funciones: solicitudes (se puede usar try/except)

def obtener_publicaciones(post_url):
    respuesta = requests.get(post_url)
    return respuesta

def obtener_segunda_publicacion(post_url):
    respuesta = requests.get(f"{post_url}/2")
    return respuesta

def crear_publicacion(post_url):
    datos = {
    "title":"Mi primer envio de datos",
    "body":"estoy probando el post",
    "userId": 1
}
    respuesta = requests.post(post_url,json=datos)
    return respuesta

def obtener_primer_usuario(post_url):
    respuesta = requests.get(f"{post_url}/1")
    return respuesta


def actualizar_primer_publicacion(post_url):

    datos_actualizar = {   
        "id":1,
        "title":"Datos actualizados",
        "body":"estoy probando el put",
        "userId": 2
    }
    respuesta = requests.put(f"{post_url}/1",json = datos_actualizar)
    return respuesta

def eliminar_publicacion(post_url):
    return requests.delete(f"{post_url}/1")

#para que el get dé status_code de error
def obtener_endpoint_inexistente(url_inexistente):
    return requests.get(url_inexistente)

