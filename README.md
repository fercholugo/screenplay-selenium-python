## **Proyecto de Automatización de Pruebas con Python, Screenplay, Selenium **

Este proyecto consiste en la automatización de pruebas funcionales sobre el proceso de inicio de sesión y la funcionalidad de crear un candidato en el módulo Recruitment de la plataforma OrangeHRM. Se implementa utilizando el patrón de diseño Screenplay, lo que permite estructurar las pruebas de manera modular y mantenible.

## **Tecnologías y Herramientas**

- Lenguaje: Python 3.x
- Framework de Automatización: ScreenPy y ScreenPy‑Selenium (implementación del patrón Screenplay)
- Pruebas BDD: pytest‑bdd (para escribir escenarios en Gherkin y ejecutarlos de forma automatizada)
- Driver Web: Selenium WebDriver (con WebDriver Manager para la gestión automática del driver)
- Gestión de Dependencias: pip (mediante un archivo requirements.txt)
- IDE: PyCharm
- Control de Versiones: Git y GitHub

## **Flujos Automatizados**

Función de Inicio de Sesión:
  - Validación del ingreso exitoso al sistema utilizando credenciales válidas.
  - Verificación de mensajes de error para credenciales incorrectas.
    
Función Agregar Candidato:

  - Diligenciamiento del formulario para crear un nuevo candidato en el módulo Recruitment.
  - Verificación de la creación del candidato mediante la validación del keyword (por ejemplo, número de identificación) en el listado o en el input, y/o mediante la aparición de un mensaje de guardado.
   
## **Estructura del Proyecto**

El proyecto sigue la estructura típica del patrón Screenplay adaptada a Python:

FEATURES:
Los archivos .feature (escritos en lenguaje Gherkin) definen los escenarios y pasos de cada flujo.

RUNNER:
Archivos de test (por ejemplo, test_login.py y test_modrecruitment_function_add_candidate.py) que sirven para ejecutar los escenarios definidos en los features mediante pytest‑bdd.

UI:
Módulos donde se mapean los elementos web (Targets) de la aplicación, como login_page.py, add_candidate_page.py y recruitment_page.py.

TASK:
Clases que definen las acciones que un actor puede realizar en la aplicación (por ejemplo, LoginTask, AddCandidateTask, NavigateUrlTask y RecruitmentTask).

STEPDEFINITION:
Implementaciones de los pasos definidos en los archivos .feature, que conectan directamente con las TASKS.

QUESTION:
Clases o funciones que encapsulan las validaciones y consultas sobre el estado de la UI (por ejemplo, para verificar que el dashboard se muestre o que el candidato se haya creado correctamente).
