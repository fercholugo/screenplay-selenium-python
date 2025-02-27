from pytest_bdd import scenarios, given, when, then, parsers
from screenpy import SeeAllOf, ReadsExactly, See
from screenpy_selenium import IsVisible

from screenplay.tasks.add_candidate_task import AddCandidateTask
from screenplay.tasks.login_task import LoginTask
from screenplay.tasks.navigate_url_task import NavigateUrlTask
from screenplay.tasks.recruitment_task import RecruitmentTask
from screenpy_selenium.questions import Element, Text

from screenplay.ui.add_candidate_page import AddCandidatePage
from screenplay.ui.recruitment_page import RecruitmentPage


@given(parsers.parse('el usuario ha iniciado sesion en OrangeHRM con las credenciales usuario "{user}" y la contraseña "{password}"'))
def usuario_inicia_sesion(actor, user: str, password: str):
    print("Paso para iniciar sesion en la aplicacion.")
    actor.attempts_to(
        NavigateUrlTask.open_url(),
        LoginTask.with_credentials(user, password)
    )

@given('el usuario navega al modulo "Recruitment"')
def navegar_a_reclutamiento(actor):
    print("el usuario navega al modulo Recruitment")
    actor.attempts_to(RecruitmentTask.navigate())

@when("el usuario ingresa a la funcion Add y crea un nuevo candidato:")
def agregar_candidato(actor, datatable):
    print("el usuario ingresa a la funcion Add y crea un nuevo candidato")
    #Procesa la tabla de datos
    candidate = {}
    headers = datatable[0]
    values = datatable[1]
    for header, value in zip(headers, values):
        candidate[header] = value
    #llena el formulario
    actor.attempts_to(
        AddCandidateTask.with_data(
            candidate["Nombre"],
            candidate["Apellido"],
            candidate["Correo"],
            candidate["Identificacion"]
        )
    )
    #print("Este es el contenido de candidate: " , candidate)

@then(parsers.parse('el candidato con la Identificacion "{number_candidate_expected}" se crea y lista exitosamente'))
def validar_candidato_guardado(actor, number_candidate_expected: str):
    #Numero de candidato ingresado
    candidate_number = getattr(actor, "keyword_num_candidate", None)
    #print(f"valor recuperado keyword en step: {candidate_number}")

    #validacion
    assert candidate_number == number_candidate_expected, (
        f"Se esperaba {number_candidate_expected} pero se obtuvo {candidate_number}"
    )
    print(f'el candidato con la Identificacion "{number_candidate_expected}" se crea y lista exitosamente')






