
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckOutPage:
    
    def __init__(self,driver): #para crear la clase
        self.driver = driver # el constructor

#locators

        self.first_name = (By.ID,'first-name')

        self.last_name = (By.ID,'last-name')

        self.postal_code = (By.ID,'postal-code')

        self.continue_button = (By.ID,'continue')

        self.titulo = (By.CLASS_NAME,'title')

    def ingresar_nombre(self,nombre): # debo poner el wait porque sino falla el test en mi computadora, tal vez al profesor no le falle porque su maquina es mas rapida
        #print(f"\n El test falló porque está varado en esta URL: {self.driver.current_url}")
        #self.driver.find_element(*self.first_name).send_keys(nombre)
        elemento = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.first_name)
        )
        elemento.send_keys(nombre)


    def ingresar_apellido(self,apellido):
        self.driver.find_element(*self.last_name).send_keys(apellido)


    def ingresar_codigo_postal(self,codigo_postal):
        self.driver.find_element(*self.postal_code).send_keys(codigo_postal)

    def completar_datos(self,nombre,apellido,codigo_postal):
        self.ingresar_nombre(nombre)
        self.ingresar_apellido(apellido)
        self.ingresar_codigo_postal(codigo_postal)
        

    def continuar(self):
        self.driver.find_element(*self.continue_button).click()

    def obtener_titulo(self):
        return self.driver.find_element(*self.titulo).text