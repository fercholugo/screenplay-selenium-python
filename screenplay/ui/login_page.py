from screenpy_selenium import Target
from selenium.webdriver.common.by import By


class LoginPage:
    """Localizadores para la pagina de inicio de sesion"""
    URL_ORANGEHRM = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    USERNAME_INPUT = Target.the("input de usuario").located_by("input[placeholder='Username']")
    PASSWORD_INPUT = Target.the("input de contraseña").located_by("input[placeholder='Password']")
    LOGIN_BUTTON = Target.the("input de usuario").located_by("button[type='submit']")

    #validacion
    DASHBOARD_HEADER = Target.the("Dashboard header").located((By.XPATH, "//h6[normalize-space()='Dashboard']"))




