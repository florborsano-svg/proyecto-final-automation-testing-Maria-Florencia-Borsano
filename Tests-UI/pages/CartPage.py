from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Defino 1 clase para cada pagina de la web a testear

class CartPage:
    
    def __init__(self,driver): #para crear la clase
        self.driver = driver # el constructor

        self.checkout_button = (By.ID,'checkout')

        self.producto = (
            By.CLASS_NAME,
            "inventory_item_name"
        )

        self.titulo = (
            By.CLASS_NAME,
            "title"
        )

        self.boton_continuar_compra = (By.ID,'continue-shopping')
        
    def obtener_nombre_producto(self):
        """
        Devuelve el nombre del producto
        que aparece en el carrito.
        """

        return self.driver.find_element(
            *self.producto
        ).text
    

    def ir_a_checkout(self):
        #self.driver.find_element(*self.checkout_button).click()
        elemento = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located(self.checkout_button)
                )
        elemento.click()

    def obtener_titulo(self):
        return self.driver.find_element(
            *self.titulo
        ).text

    def boton_continuar_compra_visible(self):
        return self.driver.find_element(
                *self.boton_continuar_compra
        ).is_displayed()