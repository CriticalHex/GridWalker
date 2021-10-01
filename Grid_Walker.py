import random
import pygame
pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("matrix rainbow barf")
clock = pygame.time.Clock()
x = 40
y = 40
# Create a 2 dimensional array. A two dimensional array is simply a list of lists.
grid = []
for i in range(80):
    # Add an empty array that will hold each cell in this row
    grid.append([])
    for j in range(80):
        grid[i].append(0)  # Append a cell
grid[y][x] = 1

GameLoop = True #variable to run game loop

# GAME LOOP-----------------------------------------------------------
while GameLoop:
    
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            GameLoop = False 
    clock.tick(60)
    
    # Draw the grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):  
            if grid[y][x] == 1:
                pygame.draw.rect(screen,(255, 255, 255),[10 * x, 10* y, 10, 10])
                pygame.display.flip()
                pygame.draw.rect(screen,(0, 0, 0),[10 * x, 10* y, 10, 10])
            
           
            grid[y][x] = 0
            rand = random.randint(1,4)
            if rand == 1:
                x += 1
            elif rand == 2:
                x -= 1
            elif rand == 3:
                y += 1
            elif rand == 4:
                y -= 1
            if x >= 80:
                x -= 79
            if x <= 0:
                x += 79
            if y >= 80:
                y -= 79
            if y <= 0:
                y += 79
            grid[y][x] = 1
    
#END GAME LOOP---------------------------------------------------------
pygame.quit()
