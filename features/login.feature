Feature: Inicio de sesion en OrangeHRM

  Scenario: Usuario inicia sesion exitosamente
    Given el usuario abre la pagina de inicio de OrangeHRM
    When ingresa el usuario "Admin" y la contraseña "admin123"
    And presiona el boton de login
    Then deberia ver el dashboard del sistema
