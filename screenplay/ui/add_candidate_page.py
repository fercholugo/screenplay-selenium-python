from screenpy_selenium import Target
from selenium.webdriver.common.by import By


class AddCandidatePage:
    """Localizadores del formulario para crear candidato"""
    FIRSTNAME_INPUT = Target.the("input primer nombre").located_by("input[placeholder='First Name']")
    LASTNAME_INPUT = Target.the("input apellido").located_by("input[placeholder='Last Name']")
    EMAIL_INPUT = Target.the("input email").located_by("body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > form:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)")
    NUM_KEYWORD_INPUT = Target.the("input numero keyword").located_by("input[placeholder='Enter comma seperated words...']")
    SAVE_BUTTON = Target.the("boton guardar candidato").located_by("button[type='submit']")

    #validacion
    SUCCESSFULLY_SAVED_MSJ = Target.the("Mensaje candidato guardado").located((By.XPATH, "//div[contains(text(), 'successfully Saved')]"))
    SEARCH_BUTTON = Target.the("boton buscar").located((By.XPATH, "//button[normalize-space()='Search']"))
    EYE_BUTTON = Target.the("boton ojo").located((By.XPATH, "//div[@class='orangehrm-container']//button[1]"))
