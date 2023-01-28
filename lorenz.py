import pygame
import numpy as np

screenx = 1250
screeny = 750

pygame.init()
size = (screenx, screeny)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("lorenz")

# https://en.wikipedia.org/wiki/Lorenz_system 

#X Y AND Z ARE STATE VARIABLES

#CHANGE SIGMA RHO AND BETA VAR FOR DIFFERENT RESULTS!
def l(x, y, z, sigma=10, rho=28, beta=8/3):
    xcor_1 = sigma*(y - x)
    ycor_2 = x*(rho - z) - y
    zcor_3 = x*y - beta*z
    return xcor_1, ycor_2, zcor_3

#state variables TWEAK AROUND FOR DIFFERENT RESULTS!
# dt is a time step for simulation, larger dt less accurate simulation.
dt = 0.01
steps = 10000
xval,yval,zval = [1],[1],[1]

    
for i in range(steps):
    xcor_1,ycor_2,zcor_3 = l(xval[-1], yval[-1], zval[-1])
    xval.append(xval[-1] + xcor_1 * dt)
    yval.append(yval[-1] + ycor_2 * dt)
    zval.append(zval[-1] + zcor_3 * dt)

    screen.fill((255, 255, 255))

    for x,y,z in zip(xval,yval,zval):
        xcord = int(size[0]/2 + x*10)
        ycord = int(size[1]/2 + z*10)
        pygame.draw.circle(screen, (255, 0, 0), (xcord, ycord), 1)

    pygame.display.flip()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           done = True

pygame.quit()
