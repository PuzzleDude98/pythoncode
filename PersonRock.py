"""
NOTE: this uses pygame. Most editors do not.
If you want to run this, make sure you have pygame
"""

"""
PersonRock

Description: An animation
"""

import pygame
pygame.init()

window = pygame.display.set_mode([400, 400])
window.fill((200, 200, 255))

bg_color = (120, 80, 40)
rock_color = (70, 60, 50)
ground_color = (60, 50, 40)
person_color = (150, 140, 80)

rock_y = -200
person_x = 70

ground_rect = pygame.Rect(0, 340, 400, 60)
rock_rect = pygame.Rect(20, rock_y, 150, 340)
person_rect = pygame.Rect(person_x, 300, 30, 40)

# Declare an offsets for the rock and person
ro=0
po=0
po2=0

a=int(input("Blood and gore mode on(1) or off(2)? "))
if a==1:
    a=(204,0,0)
else:
    a=(0,0,234)

frames = 0
while frames < 120:

    # Increase the rock offset
    if frames<100:
        ro+=2
    else:
        person_color=a
    # If the rock offset is higher than 160,
    # increase the person offsets
    if ro>160:
        po+=2
        po2+=1
        person_rect = pygame.Rect(person_x-po2, 300+po, 30+po, 40-po)

    # Use the offsets to set the rock rect's y
    # and person rect's x
    rock_rect.y=rock_y+ro

    window.fill(bg_color)
    pygame.draw.rect(window, ground_color, ground_rect)

    # Draw the rock rectangle and person ellipse
    pygame.draw.ellipse(window,person_color,person_rect)
    pygame.draw.rect(window,rock_color,rock_rect)

    # Flip and wait every frame
    pygame.display.flip()
    pygame.time.wait(40)

    frames += 1
