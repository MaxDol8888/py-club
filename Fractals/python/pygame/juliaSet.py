#!/usr/bin/env python3

## Source: https://stackoverflow.com/questions/21141065/julia-set-fractals

import pygame, sys, math, cmath, random, time
from pygame.locals import *

print("Julia set fractal generator")
#custom = int(input("Do you want a custom set? Yes(1); No(-1): "))
custom = -1
if custom == -1:
    c = complex((random.randint(-999,1000))/1000.0,(random.randint(-999,1000))/1000.0)
else:
    a = float(input("Real?: "))
    b = float(input("Imaginary?: "))
    c = complex(a,b)
lim = 4
limn = -4
mul = 0
iteration_detail = 100

dimension = (512,512)

screen = pygame.display.set_mode(dimension,0,32)

outFile = "../output/juliaSet_fractal.jpg"

print("Writing a {}x{} picture: {}".format(dimension[0], dimension[1], outFile))

pygame.display.set_caption("Julia set fractal generator")
def iterate (px_i,py_i,iters):
    itnum = 1
    z = complex(((px_i-256)/512.0)*4,((py_i-256)/512.0)*4)
    while itnum <= iters:
        if z.real >= lim or z.imag >= lim or z.real <= limn or z.imag <= limn:
                break
        z = z**2 + c
        itnum += 1
    return(z.real, z.imag, itnum)

def pixel_color_set (iterx, itery, iterations):
    pixel_color = (0,0,0)
    if iterx >= lim or itery >= lim or iterx <= limn or itery <= limn:
        RGB =int(math.sqrt(iterations) * int(255.0 / math.sqrt(iteration_detail)))
        # RGB = iterations * int(255.0/ iteration_detail)
        pixel_color = (RGB, RGB, RGB)
    return(pixel_color)

def draw_pixel (px, py, color):
    print(color)
    return(screen.fill(color, ((px, py),(1, 1))))

while True:
    for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == KEYDOWN:
                    if event.key == K_UP:
                            mul = 0.1
                    elif event.key == K_DOWN:
                            mul = -0.1
                    if event.key == K_SPACE:
                            pygame.image.save(screen, outFile)
            if event.type == KEYUP:
                     if event.key == K_UP:
                            mul = 0
                     elif event.key == K_DOWN:
                            mul = 0
            c += mul
    ypxl = 0
    while ypxl < 512:
            xpxl = 0
            while xpxl < 512:
                    ipxl = iterate(xpxl,ypxl,iteration_detail)
                    cpxl = pixel_color_set(ipxl[0], ipxl[1], ipxl[2])
                    draw_pixel(xpxl, ypxl, cpxl)
                    xpxl += 1
            ypxl += 1
    pygame.display.update()
