from pytest_bdd import given, when, then, parsers
from screenpy import Actor, SeeAllOf, ReadsExactly
from screenpy_selenium import IsVisible
from screenplay.tasks.login_task import LoginTask
from screenplay.tasks.navigate_url_task import NavigateUrlTask
from screenpy_selenium.questions import Element, Text
from screenplay.ui.login_page import LoginPage
from screenpy.pacing import beat


@given("el usuario abre la pagina de inicio de OrangeHRM")
def open_page(actor: Actor):
    actor.attempts_to(
        NavigateUrlTask.open_url()
    )

@when(parsers.parse('ingresa el usuario "{user}" y la contraseña "{password}"'))
def perform_login(actor: Actor, user: str, password: str):
    actor.attempts_to(
        LoginTask.with_credentials(user, password)
    )

@when("presiona el boton de login")
def press_login(actor: Actor):
    print("se presiono el boton de login")
    #paso incluido en loginTask
    pass

@then("deberia ver el dashboard del sistema")
def verify_dashboard(actor: Actor):
    actor.should(
        SeeAllOf(
            (Element(LoginPage.DASHBOARD_HEADER), IsVisible()),
            (Text.of_the(LoginPage.DASHBOARD_HEADER), ReadsExactly("Dashboard"))
        )
    )









