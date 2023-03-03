import pygame
from pygame.locals import *
import random

size = width, height = (1200, 800)
road_w = int(width / 1.6)
roadmark_w = int(width / 80)
right_lane = width / 2 + road_w / 4
left_lane = width / 2 - road_w / 4
speed = 1

pygame.init()
running = True
# set window size

screen = pygame.display.set_mode(size)
# set title

pygame.display.set_caption("Svet car game")
# set background color

screen.fill((60, 220, 0))

# apply changes
pygame.display.update()

# load player vehicle
car = pygame.image.load("car1.PNG")
car_location = car.get_rect()
car_location.center = right_lane, height * .8

# load enemy vehicle
car2 = pygame.image.load("other_car.PNG")
car2_location = car.get_rect()
car2_location.center = left_lane, height * .2

counter = 0
# game loop
while running:
    counter += 1
    if counter == 5000:
        speed += 0.15
        counter = 0
        print("Level up", speed)
    # animate enemy vehicle
    car2_location[1] += speed
    if car2_location[1] > height:
        if random.randint(0, 1) == 0:
            car2_location.center = right_lane, -200
        else:
            car2_location.center = left_lane, -200
    #end game
    if car_location[0] == car2_location[0] and car2_location[1] > car_location[1] - 250:
        print("GAME OVER! YOU LOST!")
        break


    # event listeners
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                car_location = car_location.move([-int(road_w / 2), 0])
            if event.key in [K_d, K_RIGHT]:
                car_location = car_location.move([int(road_w / 2), 0])
    # draw graphics
    pygame.draw.rect(
        screen,
        (50, 50, 50),
        (width / 2 - road_w / 2, 0, road_w, height))
    # center line
    pygame.draw.rect(
        screen,
        (255, 240, 60),
        (width / 2 - roadmark_w / 2, 0, roadmark_w, height))
    # left line
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width / 2 - road_w / 2 + roadmark_w * 2, 0, roadmark_w, height))
    # right line
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width / 2 + road_w / 2 - roadmark_w * 3, 0, roadmark_w, height))
    screen.blit(car, car_location)
    screen.blit(car2, car2_location)
    pygame.display.update()

pygame.quit()