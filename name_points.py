import pygame
import random
from math import floor
from vectors import Vector
from text_to_points import pts

screenWidth = 1000
screenHeight = 400
win = pygame.display.set_mode((screenWidth, screenHeight))

class Vehicle:
    def __init__(self, x, y, x0, y0) :
        self.pos = Vector(x, y)
        self.vel = Vector(0, 0)
        self.acc = Vector(0, 0)
        self.target = Vector(x0, y0)
        self.r = 4
        # self.color = (255,255,255)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.max_speed = 10
        self.max_force = 1
    
    def update(self) :
        self.pos.add(self.vel)
        self.vel.add(self.acc)
        self.acc.mult(0)

    def behaviors(self) :
        arrive = self.arrive()
        flee = self.flee()

        arrive.mult(1)
        flee.mult(5)

        self.applyForce(arrive)
        self.applyForce(flee)

    def flee(self) :
        mouse = Vector(mouseX, mouseY)

        desired = mouse.subtract(self.pos)
        d = desired.mag

        if d < 50 :
            desired.setMag(self.max_speed)
            desired.mult(-1)

            steer = desired.subtract(self.vel)
            if steer.mag > self.max_force :
                steer.setMag(self.max_force)
            
            self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            return steer
            
            
        else :
            return Vector(0, 0)

    def arrive(self) :
        desired = self.target.subtract(self.pos)

        d = desired.mag
        #speed = self.max_speed
        #if d < 100 :
        speed = self.max_speed * d / 100

        desired.setMag(speed)

        steer = desired.subtract(self.vel)
        if steer.mag > self.max_force :
            steer.setMag(self.max_force)

        return steer

    def applyForce(self, f) :
        self.acc.add(f)

    def show(self) :
        # x = floor(self.target.x)
        # y = floor(self.target.y)
        # pygame.draw.circle(win, (0, 255, 0), (x, y), self.r + 4)

        x = floor(self.pos.x)
        y = floor(self.pos.y)
        pygame.draw.circle(win, self.color, (x, y), self.r)

vehicles = []
for pt in pts :
    x = random.randint(0, screenWidth)
    y = random.randint(0, screenHeight)
    x0 = pt[0]
    y0 = pt[1]
    v = Vehicle(x, y, x0, y0)
    vehicles.append(v)

play = False
run = True
while run : 

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] :
        play = True

    if play :
        mouseX, mouseY = pygame.mouse.get_pos()

        # if pygame.mouse.get_pressed() != (0, 0, 0) :
        #     pygame.time.delay(10)
        #     x = random.randint(0, screenWidth)
        #     y = random.randint(0, screenHeight)
        #     x0 = mouseX
        #     y0 = mouseY
        #     v = Vehicle(x, y, x0, y0)
        #     vehicles.append(v)

        win.fill(0)

        for vehicle in vehicles :
            vehicle.behaviors()
            vehicle.update()
            vehicle.show()

        pygame.display.update()

pygame.quit()