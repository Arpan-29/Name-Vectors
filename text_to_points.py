import pygame
import random

string = 'ARPAN'

pygame.init()
screenWidth =  1000
screenHeight = 400
win = pygame.display.set_mode((screenWidth, screenHeight))

font = pygame.font.SysFont('comicsansms', int(200 * 5 / len(string)))
text = font.render(string, True, (255, 255, 255))
win.fill(0)
win.blit(text, (100, 50))

px = pygame.PixelArray(win)

pts = []
for x in range(screenWidth - 1) :
    for y in range(screenHeight - 1) :
        color = px[x, y]
        if color > 0 :
            if px[x + 1, y] == 0 :
                pts.append((x, y))
            elif px[x, y + 1] == 0 :
                pts.append((x, y))
            elif px[x - 1, y] == 0 :
                pts.append((x, y))
            elif px[x, y - 1] == 0 :
                pts.append((x, y))

# l = len(pts)
# l2 = l
# prob = 0.6
# for i in range(int(prob * l)) :
#     r = random.randint(0, l2 - 1)
#     pts.pop(r)
#     l2 -= 1

l = len(pts)
i = 0
while i < l :
    x = pts[i][0]
    y = pts[i][1]

    neighbors = []
    for j in range(1, 5) :
        neighbors.append((x + j, y))
        neighbors.append((x - j, y))
        neighbors.append((x, y + j))
        neighbors.append((x, y - j))
    for n in neighbors :
        if n in pts :
            pts.remove(n)
            l -= 1
    i += 1

# pygame.display.update()
# pygame.time.delay(2000)