
Feature: Funcion crear candidato en el modulo de reclutamiento en OrangeHRM

  Background:
    Given el usuario ha iniciado sesion en OrangeHRM con las credenciales usuario "Admin" y la contraseña "admin123"

  Scenario: Crear un nuevo candidato en el modulo Recruitment
    Given el usuario navega al modulo "Recruitment"
    When el usuario ingresa a la funcion Add y crea un nuevo candidato:
      | Nombre | Apellido | Correo | Identificacion |
      | Fernando| Lugo | fernandolugo@test.com | 12345678 |
    Then el candidato con la Identificacion "12345678" se crea y lista exitosamente