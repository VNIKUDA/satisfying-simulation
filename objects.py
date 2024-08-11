import pygame


class Object:
    def __init__(self, center = pygame.Vector2(320, 240), radius = 150):
        self.center = center
        self.radius = radius

        self.image = pygame.Surface((radius*2, radius*2), flags=pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 255, 255), (radius, radius), radius, width=3)

        self.collider = pygame.mask.from_surface(self.image)

    def draw(self, surface):
        position = self.center.x - self.radius, self.center.y - self.radius
        surface.blit(self.image, position)
        