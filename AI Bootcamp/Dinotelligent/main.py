import pygame
import os
import random
import sys
import neat

pygame.init()

# Konstanter

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

RUNNING = [pygame.image.load("path"), pygame.image.load("path")]

JUMPING = pygame.image.load("path")

BG = pygame.image.load("path")

FONT = pygame.font.Font("AI Bootcamp\Dinotelligent\Assets\PressStart2P-Regular.ttf",20)


class Dinosaur:
    X_POS = 80
    Y_POS = 310
    JUMP_VEL = 8.5


    def __init__(self, img=RUNNING[0]):
        self.image = img
        self.dino_run = True
        self.dino_jump = False
        self.jump_vel = self.JUMP_VEL
        self.rect = pygame.Rect(self.X_POS, self.Y_POS, img.get_width(), img.get_height())
        self.step_index = 0

    def update(self):
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()
        if self.step_index >= 10:
            self.step_index = 0
    
    def run(self):
        self.image = RUNNING[self.step_index // 5]
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = JUMPING
        if self.dino_jump:
            self.rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
            if self.jump_vel <= -self.JUMP_VEL:
                self.dino_jump = False 
                self.dino_run = True
                self.jump_vel = self.JUMP_VEL

    def draw(self):
        SCREEN.blit(self.image, (self.rect.x, self.rect.y))


def main():
    clock = pygame.time.Clock()

    dinosaurs = [Dinosaur()]

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        SCREEN.fill((255,255,255))

        for dinosaur in dinosaurs:
            dinosaur.update()
            dinosaur.draw(SCREEN)

        clock.tick(30)
        pygame.display.update()

main()