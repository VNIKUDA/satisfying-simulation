import pygame
pygame.init()


class Window:
    def __init__(self, size=(640, 480), fps=60):
        self.size = size
        self.FPS = fps

        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()

        self.closed = False

    def run(self):
        while not self.closed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.closed = True

            self.screen.fill((0, 0, 0))

            pygame.display.update()
            self.clock.tick(self.FPS)


if __name__ == "__main__":
    window = Window()
    
    window.run()