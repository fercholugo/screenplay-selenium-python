import pytest
from screenpy import Actor
from screenpy_selenium.abilities import BrowseTheWeb
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service  # <-- Nuevo import

@pytest.fixture
def actor():
    # Configurar opciones de Chrome
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    # Inicializar el driver con Service
    service = Service(executable_path=ChromeDriverManager().install())  # <-- Usar Service
    driver = Chrome(service=service, options=chrome_options)            # <-- Nueva sintaxis

    actor = Actor.named("Tester").who_can(BrowseTheWeb.using(driver))
    yield actor

