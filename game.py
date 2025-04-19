import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()  # keep track of time & cap FPS

# ----------------------------- main loop ----------------------------
running = True
while running:
    # ---- 1. process events ----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # clicked the window’s ❌
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    # ---- 2. update physics ----
    dt = clock.get_time() / 1000.0  # seconds since last frame
    # (nothing to update yet)

    # ---- 3. render ----
    screen.fill((255, 255, 255))  # clear to white
    # (nothing to draw yet)
    pygame.display.flip()  # swap buffers

    # ---- 4. timing ----
    fps = clock.tick(60)  # cap to 60 FPS
    pygame.display.set_caption(f"Physics Sandbox — {clock.get_fps():.1f} FPS")
# --------------------------------------------------------------------

pygame.quit()
sys.exit()
