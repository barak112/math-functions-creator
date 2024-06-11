import pygame
import random

pygame.init()

image = pygame.image.load("function creator/functions.png")
rnd = random.randrange
color = (255, 0, 0)
black = (0, 0, 0)

minusb = 1
y = 0
count = 0
linecount = 0
firsttime = True
font = pygame.font.Font('freesansbold.ttf', 25)

startx = 380
starty = count + 300

endx = 420
endy = 300 - count

num = 0

wn_width = 800
wn_hight = 600

wn = pygame.display.set_mode((wn_width, wn_hight))

base_font = pygame.font.Font(None, 32)
user_text = 0

input_rect = pygame.Rect(200, 550, 140, 32)

color_active = (170, 170, 170)

color_passive = (100, 100, 100)
backgroundcolor = color_passive

active = False

class line(object):
    def __init__(self, start, end, blue, width):
        object.__init__(self)
        self.start = start
        self.end = end
        self.blue = blue
        self.width = width

b = 0
lines = []
wn.blit(image, (0, -30))
state = True
while state:
    mouse = pygame.mouse.get_pos()

    def create_line(count, color):
        global start, end, num
        start = (startx - 20000), (starty + 1 + y * 20000 + int(num) * -20 * minusb)
        end = (endx + 20000), (endy + 1 + count / 20 * -20000 + int(num) * -20 * minusb)
        color = color
        width = 3
        return line(start, end, color, width)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        if 200 <= mouse[0] <= 200 + 80 and 550 <= mouse[1] <= 550 + 32:
            active = True
        else:
            active = False

        if event.type == pygame.KEYDOWN:
            if 200 <= mouse[0] <= 200 + 80 and 550 <= mouse[1] <= 550 + 32:
                if event.unicode.isnumeric():
                    if len(str(user_text)) == 1:
                        user_text = user_text * 10 + int(event.unicode)
                    else:
                        user_text = int(event.unicode)
            else:
                if event.unicode.isnumeric():
                    b = int(event.unicode)
                    num = int(event.unicode)

            del lines[linecount]
            color = (255, 0, 0)
            lines.append(create_line(count, color))
            drawlines(wn, lines)

            if pygame.key.get_pressed()[pygame.K_DOWN]:
                count -= 20
                y -= 1
                del lines[linecount]
                color = (255, 0, 0)
                lines.append(create_line(count, color))
                drawlines(wn, lines)
                pygame.display.update()

            if pygame.key.get_pressed()[pygame.K_UP]:
                count += 20
                y += 1
                del lines[linecount]
                color = (255, 0, 0)
                lines.append(create_line(count, (255, 0, 0)))
                drawlines(wn, lines)
                pygame.display.update()

            if pygame.key.get_pressed()[pygame.K_n]:
                color = (rnd(255), rnd(255), rnd(255))
                lines.append(create_line(count, color))
                del lines[linecount]
                y += 1
                linecount += 1
                count += 20
                lines.append(create_line(count, (255, 0, 0)))
                drawlines(wn, lines)
                pygame.display.update()

            if pygame.key.get_pressed()[pygame.K_MINUS]:
                minusb = -1
                lines.append(create_line(count, (255, 0, 0)))
                del lines[linecount]
                drawlines(wn, lines)
                pygame.display.update()

            if pygame.key.get_pressed()[pygame.K_PLUS]  or pygame.key.get_pressed()[pygame.K_EQUALS]:
                minusb = 1
                lines.append(create_line(count, (255, 0, 0)))
                del lines[linecount]
                drawlines(wn, lines)
                pygame.display.update()

            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                quit()

        if active:
            backgroundcolor = color_active
        else:
            backgroundcolor = color_passive

        pygame.draw.rect(wn, backgroundcolor, input_rect)

        text_surface = base_font.render(str(user_text), True, (255, 255, 255))
        if minusb == -1:
            fistext = font.render(str(f"f({user_text})={user_text * y - b}"), True, black)
        else:
            fistext = font.render(str(f"f({user_text})={user_text*y+b}"), True, black)
        wn.blit(fistext, (input_rect.x + 5, input_rect.y + 5))

        input_rect.w = max(10, text_surface.get_width() + 70)

    def drawlines(wn, lines):
        wn.blit(image, (0, -30))
        text = font.render(str(f"m:{y}"), True, black)
        textRect = text.get_rect()
        textRect.center = (50 // 2, 40 // 2)

        text2 = font.render(str(f"lines:{len(lines)}"), True, black)
        textRect2 = text.get_rect()
        textRect2.center = (1450 // 2, 40 // 2)

        wn.blit(text, textRect)
        wn.blit(text2, textRect2)

        for line in lines:
            pygame.draw.line(wn, line.blue, line.start, line.end, line.width)
            pygame.display.update()

    if firsttime:
        lines.append(create_line(count, color))
        drawlines(wn, lines)
        firsttime = False

    pygame.display.update()