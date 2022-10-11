import pygame, sys
from math import *

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WIDTH = 600
HEIGHT = 600

clock = pygame.time.Clock()
window = pygame.display.set_mode((WIDTH, HEIGHT))
running = True

cube_points = [[-1, -1, 1],
               [1, -1, 1],
               [1, 1, 1],
               [-1, 1, 1],
               [-1, -1, -1],
               [1, 1, -1],
               [-1, 1, -1],
               [1, -1, -1]]

rotation_matrix = [[1,0,0], 
                   [0,1,0],
                   [0,0,0]]

def matrix_multiplication(a, b):
    points_2d = [0 for _ in range(3)]

    a_cols = len(a[0])
    a_rows = len(a)
    b_rows = len(b)

    if(a_cols == b_rows):
        for r in range(a_rows):
            for i in range(b_rows):
                points_2d[r] += a[r][i] * b[i]
    else:
        print("Incompatible matrix size")
                
    return points_2d

def draw_lines(i, j, points):
    pygame.draw.line(window, WHITE, (points[i][0], points[i][1]) , (points[j][0], points[j][1]))
    

angle_x = angle_y = angle_z = 0

pygame.init()

while running:

    clock.tick(5)
    window.fill(BLACK)

    rotation_x = [[1, 0, 0],
                  [0, cos(angle_x), -sin(angle_x)],
                  [0, sin(angle_x), cos(angle_x)]]

    rotation_y = [[cos(angle_y), 0, sin(angle_y)],
                  [0, 1, 0],
                  [-sin(angle_y), 0, cos(angle_y)]]

    rotation_z = [[cos(angle_z), -sin(angle_z), 0],
                  [sin(angle_z), cos(angle_z), 0],
                  [0, 0, 1]]

    
    points_to_draw= [0 for _ in range(len(cube_points))]
    i = 0

    for p in cube_points:
        rotate_x = matrix_multiplication(rotation_x, p)
        rotate_y = matrix_multiplication(rotation_y, rotate_x)
        rotate_z = matrix_multiplication(rotation_z, rotate_y)
        point_2d = matrix_multiplication(rotation_matrix, rotate_z)
        x = point_2d[0] * 100 + WIDTH/2
        y = point_2d[1] * 100 + HEIGHT/2
        points_to_draw[i] = [x, y]
        i += 1
        pygame.draw.circle(window, WHITE, (x,y), 5 )

    
    draw_lines(0, 1, points_to_draw)
    draw_lines(0, 3, points_to_draw)
    draw_lines(0, 4, points_to_draw)
    draw_lines(2, 1, points_to_draw)
    draw_lines(2, 3, points_to_draw)
    draw_lines(2, 5, points_to_draw)
    draw_lines(6, 4, points_to_draw)
    draw_lines(6, 3, points_to_draw)
    draw_lines(6, 5, points_to_draw)
    draw_lines(7, 1, points_to_draw)
    draw_lines(7, 4, points_to_draw)
    draw_lines(7, 5, points_to_draw)

    angle_x += 0.1
    angle_y += 0.1
    angle_z += 0.1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()