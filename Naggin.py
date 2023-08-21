import pygame as py
import time 
import random

speed_of_snake = 15

WIDTH = 700
HEIGHT = 460

midnight_blue = py.Color(25,25,112)
mint_cream = py.Color(245,255,250)
crimson_red = py.Color(220,20,60)
lawn_green = py.Color(124,252,0)
orange_red= py.Color(255,69,0)

py.init()

#display
screen = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("naggin")

game_clock = py.time.Clock()

pos_of_snake = [100,50]

body_of_snake = [
    [100,50],
    [90,50],
    [80,50],
    [70,50]
]

pos_of_fruit = [
    random.randrange(1,(WIDTH/10))*10,
    random.randrange(1,(HEIGHT/10))*10
]

spawn_of_fruit = True

intial_direction = "RIGHT"
snake_direction = intial_direction

score = 0

