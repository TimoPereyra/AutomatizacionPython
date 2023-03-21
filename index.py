from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


path = ('../../Downloads/chromedriver_win32/chromedriver.exe')
webSite = ('https://www.grupo-global.com.ar/')
driver = webdriver.Chrome(path)
driver.get(webSite)
# Ir a la sección de contacto
contact_section = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='#contacto']")))

contact_section.click()
# Completar el formulario de contacto con una dirección de correo inválida
name_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name=nombre]")))
name_field.send_keys("Juan Perez")

email_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name=email]")))
email_field.send_keys("correoInvalido")

message_company = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name=empresa]")))
message_company.send_keys("Hola, no tengo empresa")

message_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea[name=mensaje]")))
message_field.send_keys("Hola.")
buttonContact = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name=submit]")))
buttonContact.click()
# Esperamos a que aparezca el mensaje de error
error_div = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name=email]")))
error_message = error_div.text

if error_message == 'Error en el envío del mensaje. Por favor inténtelo de nuevo más tarde.':
    print('La prueba ha pasado')
else:
    print('La prueba ha fallado')
time.sleep(5)

# Cerramos el navegador
driver.quit()