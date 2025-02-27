from screenpy import Actor
from screenpy_selenium.actions import Click

from screenplay.ui.recruitment_page import RecruitmentPage


class RecruitmentTask:

    """Navega al modulo recruitment"""
    def perform_as(self, actor: Actor):
        actor.attempts_to(
            Click.on(RecruitmentPage.RECRUITMENT_MENU)
        )

    @staticmethod
    def navigate():
        """Metodo para llamar la tarea"""
        return RecruitmentTask()





