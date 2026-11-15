import pygame
import random
import math

PLATFORM_COLOR = (100, 80, 50)
PLATFORM_COLOR_CRUMBLING = (150, 100, 100)
PLATFORM_COLOR_SPRING = (255, 200, 50)
LAVA_COLOR = (220, 60, 20)

PLATFORM_NORMAL = 0
PLATFORM_CRUMBLING = 1
PLATFORM_SPRING = 2

CRUMBLE_TIME = 90
SPRING_BOOST = -22

class Platform(pygame.Rect):
    def __init__(self, x, y, w, h, ptype=PLATFORM_NORMAL):
        super().__init__(x, y, w, h)
        self.type = ptype
        self.crumble_timer = 0
        self.active = True

def generate_platforms(width, base_y, count=30):
    plats = [Platform(0, base_y, width, 20, PLATFORM_NORMAL)]
    y = base_y - 110
    for i in range(count):
        w = random.randint(80, 200)
        x = random.randint(0, width - w)
        r = random.random()
        if r < 0.25:
            ptype = PLATFORM_CRUMBLING
        elif r < 0.40:
            ptype = PLATFORM_SPRING
        else:
            ptype = PLATFORM_NORMAL
        plats.append(Platform(x, y, w, 16, ptype))
        y -= random.randint(80, 130)
    return plats

def draw_lava(screen, lava_y, cam_y, width, height, frame):
    ly = int(lava_y - cam_y)
    if ly < height:
        pts = [(0, ly)]
        for x in range(0, width + 20, 20):
            pts.append((x, ly + int(math.sin(x * 0.08 + frame * 0.1) * 8)))
        pts.append((width, height)); pts.append((0, height))
        pygame.draw.polygon(screen, LAVA_COLOR, pts)
        s = pygame.Surface((width, 30), pygame.SRCALPHA)
        for i in range(15):
            pygame.draw.line(s, (255, 100, 0, max(0, 60 - i * 4)), (0, i), (width, i), 1)
        screen.blit(s, (0, ly - 15))