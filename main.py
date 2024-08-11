import pygame
from objects import Object
pygame.init()


class Window:
    def __init__(self, size = pygame.Vector2(640, 480), fps = 60):
        # Window attrs
        self.size = size
        self.FPS = fps

        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()

        self.closed = False

        # Scene attrs
        self.container = Object()

    
    def run(self):
        while not self.closed:
            # Event handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.closed = True

            # Update screen
            self.update()

            # Update window and tick the clock
            pygame.display.update()
            self.clock.tick(self.FPS)


    def update(self):
        # Background
        self.screen.fill((100, 100, 100))

        # Drawing objects
        self.container.draw(self.screen)


if __name__ == "__main__":
    window = Window()

    window.run()
