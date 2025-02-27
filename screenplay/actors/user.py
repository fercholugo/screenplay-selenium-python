from screenplay.abilities.browse_the_web import BrowseTheWeb


class User:
    def __init__(self, name):
        self.name = name
        self.abilities = {}

    def can(self, ability):
        """Asigna una habilidad al actor."""
        self.abilities[type(ability)] = ability

    def using(self, ability_class):
        """Obtiene una habilidad asignada al actor."""
        return self.abilities.get(ability_class, None)

    def quit(self):
        """Cierra el navegador si tiene la habilidad BrowseTheWeb"""
        browse_the_web = self.using(BrowseTheWeb)
        if browse_the_web:
            browse_the_web.quit()

