from screenpy import Actor
from screenpy_selenium.actions import Enter, Click, Open
from screenplay.ui.login_page import LoginPage

class NavigateUrlTask:

    """Navegar a la url de sistema ORANGEHRM"""
    def perform_as(self, actor: Actor):
        actor.attempts_to(
            # Abre la url del sistema
            Open.their_browser_on(LoginPage.URL_ORANGEHRM)
        )

    @staticmethod
    def open_url():
        """Metodo para navegar a la url del sistema"""
        return NavigateUrlTask()

