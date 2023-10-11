import pytest
from selenium import webdriver

@pytest.fixture
def browser(selenium):
    # Esto inicia el navegador especificado en pytest.ini
    return selenium

def test_aplicacion_web(browser):
    # Abre la URL de la aplicación web
    browser.get("http://localhost:8080")

    # Realiza las acciones del usuario
    # Por ejemplo, puedes encontrar elementos por su etiqueta, clase, ID, etc., y realizar acciones sobre ellos
    welcome_message = browser.find_element_by_tag_name("h1")
    assert welcome_message.text == "Bienvenido a mi aplicación web"

    # Asegúrate de que la fecha y hora se muestren
    datetime = browser.find_element_by_class_name("datetime")
    assert len(datetime.text) > 0
