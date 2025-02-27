from asyncio import timeout

from screenpy import Actor
from screenpy_selenium.actions import Click, Enter, Wait
from screenplay.ui.add_candidate_page import AddCandidatePage
from screenplay.ui.recruitment_page import RecruitmentPage
from screenpy_selenium.questions import Element, Text

from selenium.webdriver.support import expected_conditions as EC


class AddCandidateTask:
    """Completa el formulario de agregar candidato y lo guarda"""
    def __init__(self, first_name: str, last_name: str, email: str, num_keyword: str):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.num_keyword = num_keyword

    def perform_as(self, actor: Actor):
        """Ejecuta la accion de hacer click en 'Add', llenar el formulario y guardarlo."""
        actor.attempts_to(
    Wait.for_the(RecruitmentPage.ADD_CANDIDATE_BUTTON).to_be_clickable(),
            Click.on(RecruitmentPage.ADD_CANDIDATE_BUTTON),
            Wait.for_the(AddCandidatePage.FIRSTNAME_INPUT).to_be_clickable(),
            Enter.the_text(self.first_name).into(AddCandidatePage.FIRSTNAME_INPUT),
            Wait.for_the(AddCandidatePage.LASTNAME_INPUT).to_be_clickable(),
            Enter.the_text(self.last_name).into(AddCandidatePage.LASTNAME_INPUT),
            Wait.for_the(AddCandidatePage.EMAIL_INPUT).to_be_clickable(),
            Enter.the_text(self.email).into(AddCandidatePage.EMAIL_INPUT),
            Wait.for_the(AddCandidatePage.NUM_KEYWORD_INPUT).to_be_clickable(),
            Enter.the_text(self.num_keyword).into(AddCandidatePage.NUM_KEYWORD_INPUT),
            Wait.for_the(AddCandidatePage.SAVE_BUTTON).to_be_clickable(),
            Click.on(AddCandidatePage.SAVE_BUTTON),
            #acciones validacion candidato
            Wait.for_the(AddCandidatePage.NUM_KEYWORD_INPUT).to_be_clickable()
        )

        # Obtener el valor del input (incluso si está deshabilitado)
        element = Element(AddCandidatePage.NUM_KEYWORD_INPUT).answered_by(actor)
        keyword_num_candidate = element.get_attribute("value")
        print(f"keyword almacenado en input: {keyword_num_candidate}")
        actor.keyword_num_candidate = keyword_num_candidate


    @staticmethod
    def with_data(first_name: str, last_name: str, email: str, num_keyword: str):
        """Metodo para llamar a la tarea con datos del candidato"""
        return AddCandidateTask(first_name, last_name, email, num_keyword)
