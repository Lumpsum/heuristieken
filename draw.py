import pygame
import sys
import random

def draw_solution(grids):
    pygame.init()
    
    grid_width, grid_height = len(grids[0]), len(grids[0])
    margin = 5
    screen_width, screen_heigth = 600, 600
    block_size = (screen_width / (grid_width)) - margin
    textfont = pygame.font.SysFont("monospace", 40)
    
    window = pygame.display.set_mode((screen_width + 100, screen_heigth + margin))
    i = 0
    delay = int(0.5 * 1000)

    grids = grids[::-1]
    
    # Set colors for each car in grid.
    cars = {}
    cars[0], cars[1] = (255, 255, 255), (255, 0, 0)
    for x in grids[0]:
        for y in x:
            if y not in cars and y != 0 and y != 1:
                cars[y] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    # Draw grid function.
    def draw_grid(grid):
        for y in range(grid_height):
            for x in range(grid_width):
                rect = pygame.Rect(margin + x*(block_size + margin), margin + y*(block_size + margin), block_size, block_size)
                pygame.draw.rect(window, cars[grid[y][x]], rect)
        return True
        
    draw_grid(grids[i])
    pygame.display.update()
    
    # Set exit options.
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if i < len(grids) - 1:
            i = i + 1
            window.fill(pygame.Color("black"))
            window.blit(textfont.render("Move:", 1, (255,255,255)), (screen_width + margin, margin))
            window.blit(textfont.render(str(i) + " / " + str(len(grids)-1), 1, (255,255,255)), (screen_width + margin, margin+30))
        draw_grid(grids[i])

        pygame.time.delay(delay)
        pygame.display.update()