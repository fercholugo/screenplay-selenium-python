from screenpy import Actor
from screenpy_selenium import Waits
from screenpy_selenium.actions import Enter, Click, Wait
from screenplay.ui.login_page import LoginPage

class LoginTask:

    """ Realiza el inicio de sesion en OrangeHRM"""

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def perform_as(self, actor: Actor):
        print("Abriendo URL:", LoginPage.URL_ORANGEHRM)
        actor.attempts_to(
            #Ingresa credenciales validas
    Wait.for_the(LoginPage.USERNAME_INPUT).to_be_clickable(),
            Enter.the_text(self.username).into(LoginPage.USERNAME_INPUT),
            Enter.the_text(self.password).into(LoginPage.PASSWORD_INPUT),
            Click.on(LoginPage.LOGIN_BUTTON),

            #espera para visualizar dashboard
            Wait.for_the(LoginPage.DASHBOARD_HEADER).to_be_clickable()
        )

    @staticmethod
    def with_credentials(username: str, password: str):
        """Metodo para llamar a la tarea con credenciales"""
        return LoginTask(username, password)



