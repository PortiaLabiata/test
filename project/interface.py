import pygame
from pygame.draw import *
import pygame.font

class Text(pygame.sprite.Sprite):
    # @anchor uses rect position
    def __init__(self, text, font, color, position, anchor="topleft"):
        pygame.sprite.Sprite.__init__(self)
        self._text = text
        self._font = font
        self._color = color
        self._position = position
        self._anchor = anchor
        self.render()

    def render(self):
        self.image = self._font.render(self._text, 1, self._color)
        self.rect = self.image.get_rect(**{self._anchor: self._position})

class MultiText(pygame.sprite.Sprite):
    # @anchor uses rect position
    def __init__(self, texts, font, color, position, anchor="topleft"):
        pygame.sprite.Sprite.__init__(self)
        self._texts = texts
        self._font = font
        self._color = color
        self._position = position
        self._anchor = anchor
        self.render()

    def render(self):
        width, height = 0, 0
        for text in self._texts:
            height += self._font.get_linesize()
            w, _ = self._font.size(text)
            if w > width:
                width = w

        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))
        self.rect = self.image.get_rect(**{self._anchor: self._position})
        line = iter_count(0, self._font.get_linesize())
        for text in self._texts:
            image = self._font.render(text, 1, self._color)
            self.image.blit(image, (0, next(line)))

def generate_control_panel(alm):
    font = pygame.font.SysFont(None, 23)
    panel_string = "V vert.: "+str(round(alm.v[1], 2))+"\nV hor.:"+str(round(alm.v[1], 2))
    #surface = font.render(panel_string, False, (255, 255, 255))
    #rect = surface.get_rect()
    #rect.center = (50, 20)
    surface = MultiText(panel_string, font, (255, 255, 255), (50, 20))
    surface.render()
    return surface, rect


