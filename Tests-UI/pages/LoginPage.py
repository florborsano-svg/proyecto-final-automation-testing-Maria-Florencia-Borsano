from selenium.webdriver.common.by import By

# Defino 1 clase para cada pagina de la web a testear

class LoginPage:
    
    def __init__(self,driver): #para crear la clase
        self.driver = driver # el constructor


# defino 3 locators: que estaban utilizados y buscados en "def test_01_login(driver):""
        self.username = (By.ID, "user-name") # self significa esta clase
        self.password = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def ingresar_Usuario(self,usuario):
        #self.driver.find_element(*self.username).send_keys(usuario) #el * desempaqueta, extrae de la estructura los valores de los elementos en este caso seria "user-name"
        elemento_usuario = self.driver.find_element(*self.username)
        elemento_usuario.clear()
        elemento_usuario.send_keys(usuario)
    #numeros = [10,20,30,40]
    #print(*numeros) # solo imprime los valores


    def ingresar_password(self,password):
        #self.driver.find_element(*self.password).send_keys(password)
        elemento_usuario = self.driver.find_element(*self.password)
        elemento_usuario.clear()
        elemento_usuario.send_keys(password)
        


    def hacer_login(self,usuario,password):
        self.ingresar_Usuario(usuario) # para invocar este metodo y todos NO se necesita pasar el argumento "self"
        self.ingresar_password(password)
        self.driver.find_element(*self.login_button).click() # es pasarle esto: self.login_button = (By.ID, "login-button")


   