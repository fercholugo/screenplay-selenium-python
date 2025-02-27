from screenpy import Actor
from screenpy_selenium import Wait
from screenpy_selenium.questions import Element
from screenpy_selenium.resolutions import IsVisible
from screenplay.ui.login_page import LoginPage



class IsDashboardVisible:
    """Pregunta para verificar si el dashboard es visible."""

    @staticmethod
    def is_visible():
        return IsDashboardVisible()

    def answered_by(self, actor):
        return Element(LoginPage.DASHBOARD_HEADER).answered_by(actor)
