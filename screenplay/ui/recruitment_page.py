from screenpy_selenium import Target


class RecruitmentPage:

    """Localizadores para el modulo Recruitment"""
    RECRUITMENT_MENU = Target.the("menu recruitment").located_by("body > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > aside:nth-child(1) > nav:nth-child(1) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(5) > a:nth-child(1)")
    ADD_CANDIDATE_BUTTON = Target.the("boton para agregar candidato").located_by("button[class='oxd-button oxd-button--medium oxd-button--secondary']")
