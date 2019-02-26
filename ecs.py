import pygame

WIDTH = 800
HEIGHT = 600


# ---------------------------------------------------
# Components
# ---------------------------------------------------

class Component:
    pass

class PositionComponent(Component):
    def __init__(self, x, y, alto, ancho):
        self.x = x
        self.y = y
        self.alto = alto
        self.ancho = ancho

    def __str__(self):
        return "POSITION_COMPONENT"

class ClickableComponent(Component):
    def __init__(self, callback):
        self.callback = callback

    def __str__(self):
        return "CLICKABLE_COMPONENT"

class ColorComponent(Component):
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
    
    def __str__(self):
        return "COLOR_COMPONENT"

# ---------------------------------------------------
# Entities
# ---------------------------------------------------

class Entity:
    def __init__(self):
        self.componentes = {}
        
    def add_component(self, comp):
        self.componentes[str(comp)] = comp

class Rectangulo(Entity):
    pass

# ---------------------------------------------------
# Systems
# ---------------------------------------------------

class System:
    pass

#Singleton
class RenderSystem(System):
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance == None:
            cls.instance = RenderSystem()
        return cls.instance

    def __init__(self):
        ## Lista con los  componentes que el sistema puede trabajar
        self.requires = ["POSITION_COMPONENT", "COLOR_COMPONENT"] 
        self.canvas = pygame.display.set_mode((WIDTH, HEIGHT))

    def render(self, entity):
        match = False
        for c in self.requires:
            if c in entity.componentes:
                match = True
            else:
                match = False
                break
        
        if match == True:
            ## Renderizado
            color = (entity.componentes["COLOR_COMPONENT"].r, entity.componentes["COLOR_COMPONENT"].g, entity.componentes["COLOR_COMPONENT"].b)
            x = entity.componentes["POSITION_COMPONENT"].x
            y = entity.componentes["POSITION_COMPONENT"].y
            alto = entity.componentes["POSITION_COMPONENT"].alto
            ancho = entity.componentes["POSITION_COMPONENT"].ancho
            pygame.draw.rect(self.canvas, color, (x, y, ancho, alto))

    def blit(self):
        pygame.display.flip()
        

class EventsSystem(System):
    pass

# ---------------------------------------------------
# Controllers
# ---------------------------------------------------

class Controller:
    def __init__(self):
        self.entities = []

    def add_entity(self, entity):
        self.entities.append(entity)

    def on_create(self):
        pass

    def handle_events(self):
        pass

    def draw(self):
        pass

class Pantalla1Controller(Controller):
    def on_create(self):
        # Creando mi entity
        rect1 = Rectangulo()
        rect1.add_component(PositionComponent(400, 400, 40, 40))
        rect1.add_component(ColorComponent(255, 0, 0))

        self.add_entity(rect1)

    def handle_events(self):
        pass

    def draw(self):
        for entity in self.entities:
            RenderSystem.get_instance().render(entity)
        
        RenderSystem.get_instance().blit()

def main():
    pygame.init() 

    p1 = Pantalla1Controller()

    p1.on_create()

    while True:
        p1.handle_events()
        #p1.update()
        p1.draw()


if __name__ == "__main__":
    main()