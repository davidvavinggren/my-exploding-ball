import pygame
import sys
import numpy as np

pygame.init()
WIDTH, HEIGHT = 800, 600
PPM = 50  # pixels/m
g = 9.82  # gravity constant in m/s^2
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()  # keep track of time & cap FPS


class Ball:
    def __init__(self, x_m, y_m, radius_px, color):
        self.p = np.array([x_m, y_m], dtype=float)  # position vector (x, y) (m)
        self.v = np.zeros(2, dtype=float)  # velocity vector (vx, vy) (m/s)
        self.a = np.array([0, -g], dtype=float)  # acceleration vector (ax, ay) (m/s^2)
        self.radius = radius_px
        self.color = color

    def update(self, dt):
        # v = v + dv/dt * dt = v + a * dt
        self.v += self.a * dt

        # p = p + dv/dt * dt = p + v * dt
        self.p += self.v * dt
        print(self.p)

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self._world_to_screen(), self.radius)
        pygame.draw.circle(
            surface, (0, 0, 0), self._world_to_screen(), self.radius, 2
        )  # black outline with width 2

    def _world_to_screen(self):
        # y is up in real world but not in pygame; flip and shift
        x, y = self.p
        sx = WIDTH / 2 + x * PPM  # shift right from centre
        sy = HEIGHT / 2 - y * PPM  # flip & shift down from centre
        return int(sx), int(sy)


ball = Ball(x_m=0, y_m=0, radius_px=20, color=(255, 0, 0))  # red ball


# ----------------------------- main loop ----------------------------
running = True
dt = 0.0
while running:
    # ---- 1. process events ----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # window close button
            running = False
        elif (
            event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
        ):  # escape key
            running = False

    # ---- 2. update physics ----
    ball.update(dt)
    dt = clock.get_time() / 1000.0  # seconds since last frame
    print(dt)

    # ---- 3. render ----
    screen.fill((255, 255, 255))  # clear to white
    ball.draw(screen)  # draw the red ball
    pygame.display.flip()  # swap buffers

    # ---- 4. timing ----
    fps = clock.tick(60)  # cap to 60 FPS
    pygame.display.set_caption(f"my exploding ball; FPS = {clock.get_fps():.1f}")
# --------------------------------------------------------------------

pygame.quit()
sys.exit()
