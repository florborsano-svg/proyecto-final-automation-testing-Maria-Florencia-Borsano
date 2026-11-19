from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Defino 1 clase para cada pagina de la web a testear

class CheckoutOverview:
    
    def __init__(self,driver): #para crear la clase
        self.driver = driver # el constructor

    # locators:

        self.finish_button = (By.ID,'finish')
        self.confirmacion = (By.CLASS_NAME, 'complete-header')
        self.titulo = (By.CLASS_NAME,'title')
        self.boton_cancel = (By.ID,'cancel')

    #metodos:

    def finalizar_compra(self):
        self.driver.find_element(*self.finish_button).click()

    def obtener_confirmacion(self):
        elemento = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(self.confirmacion)
    )
        return elemento.text

    def obtener_titulo(self):
        elemento = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(self.titulo)
        )
        return elemento.text

    def boton_cancel_visible(self):
        return self.driver.find_element(
         *self.boton_cancel
        ).is_displayed()