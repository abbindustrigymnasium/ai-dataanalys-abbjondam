import pygame
import os
import random
import sys
import math
import numpy as np
import neat

pygame.init()


""" Pygame constants """

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
RUNNING = [pygame.image.load("Dinotelligent\Assets\Dino\DinoRun1.png"), pygame.image.load("Dinotelligent\Assets\Dino\DinoRun2.png")]

JUMPING = pygame.image.load("Dinotelligent\Assets\Dino\DinoJump.png")

DUCKING = [pygame.image.load("Dinotelligent\Assets\Dino\DinoDuck1.png"), pygame.image.load("Dinotelligent\Assets\Dino\DinoDuck2.png")]


SMALL_CACTUS = [pygame.image.load("Dinotelligent\Assets\Cactus\SmallCactus1.png"),
                pygame.image.load("Dinotelligent\Assets\Cactus\SmallCactus2.png"),
                pygame.image.load("Dinotelligent\Assets\Cactus\SmallCactus3.png")]

LARGE_CACTUS = [pygame.image.load("Dinotelligent\Assets\Cactus\LargeCactus1.png"),
                pygame.image.load("Dinotelligent\Assets\Cactus\LargeCactus2.png"),
                pygame.image.load("Dinotelligent\Assets\Cactus\LargeCactus3.png")]

PTERODACTYL = [pygame.image.load("Dinotelligent/Assets/Flying/fly1.png"), pygame.image.load("Dinotelligent/Assets/Flying/fly2.png")]

BG = pygame.image.load("Dinotelligent\Assets\Other\Track.png")

FONT = pygame.font.Font("Dinotelligent\Assets\PressStart2P-Regular.ttf",20)


""" Dinosaur class from which every dinosaur is created from"""

class Dinosaur:

    #Constants for the class

    X_POS = 80
    Y_POS = 310
    JUMP_VEL = 9.2

    #Init function

    def __init__(self, img=RUNNING[0]):
        self.image = img
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.jump_vel = self.JUMP_VEL
        self.rect = pygame.Rect(self.X_POS, self.Y_POS, img.get_width(), img.get_height())
        self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        self.step_index = 0
        self.x_offset = 54
        self.y_offset = 12

    #Update function (call the functions run, jump and duck)

    def update(self):
        self.rect = pygame.Rect(self.X_POS, self.rect.y, self.image.get_width(), self.image.get_height())
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()
        if self.dino_duck:
            self.duck()
        if self.step_index >= 20:
            self.step_index = 0

    #Run function makes the dinosaur run     
    
    def run(self):
        self.image = RUNNING[self.step_index // 10]
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.step_index += 1

    #Jump function makes the dinosaur jump    

    def jump(self):
        self.image = JUMPING
        if self.dino_jump:
            self.rect.y = round(self.rect.y - self.jump_vel * 3)
            self.jump_vel -= 0.6
        if self.jump_vel <= -self.JUMP_VEL:
            self.dino_jump = False 
            self.dino_run = True
            self.jump_vel = self.JUMP_VEL

    #Duck function makes the dinosaur duck    

    def duck(self):
        self.image = DUCKING[self.step_index // 10]
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS +37 
        self.x_offset = 85
        self.step_index += 1
    
    #Draws the dinosaur

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.rect.x, self.rect.y))
        pygame.draw.rect(SCREEN, self.color, (self.rect.x, self.rect.y, self.rect.width, self.rect.height), 2)
        if len(obstacles) > 0:
            pygame.draw.line(SCREEN, self.color, (self.rect.x + self.x_offset, self.rect.y + self.y_offset), obstacles[obstacleId].rect.bottomleft, 2)


"""Classes for obstacle update fucntion updates position and draw draws the obstacle """            

#Class for ground obstacles 

class Obstacle:
    def __init__(self, image, number_of_cacti):
        self.image = image
        self.type = number_of_cacti
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop(0)
            obstacles[0].rect.x -= game_speed
            return True

    def draw(self,SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)

#Class for flying obstacles 

class flyingObstacle:
    def __init__(self, image):
        self.image = image
        self.rect = self.image[0].get_rect()
        self.rect.x = SCREEN_WIDTH
        self.step_index = 1

    def update(self):
        self.rect.x -= game_speed
        if self.step_index >= 29:
            self.step_index = 0
        if self.rect.x < -self.rect.width:
            obstacles.pop(0)
            obstacles[0].rect.x -= game_speed
            return True
        
    def draw(self,SCREEN):
        if self.image == PTERODACTYL:
            self.step_index += 1
            self.type = self.step_index
        

        SCREEN.blit(self.image[self.step_index // 15], self.rect)

class SmallCactus(Obstacle):
    def __init__(self, image, number_of_cacti):
        super().__init__(image, number_of_cacti)
        self.rect.y = 325

class LargeCactus(Obstacle):
    def __init__(self, image, number_of_cacti):
        super().__init__(image, number_of_cacti)
        self.rect.y = 300

class Pterodactyl(flyingObstacle):
    def __init__(self, image):
        super().__init__(image)
        random_height = random.choice([245,275,325])
        self.rect.y = random_height


#Remove dinasaur genome and net

def remove(index):
    dinosaurs.pop(index)
    ge.pop(index)
    nets.pop(index)

""" Eval function (the game) """

def eval_genomes(genomes, config):
    global game_speed, x_pos_bg, y_pos_bg, obstacles, dinosaurs, ge, nets, points, obstacleId

    #Variables

    clock = pygame.time.Clock()
    points = 0

    obstacles = []
    dinosaurs = []
    ge = []
    nets = []

    x_pos_bg = 0
    y_pos_bg = 380
    game_speed = 10
    ObstacleId = 0

    #Create net, genome and dinosaur
    
    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        dinosaurs.append(Dinosaur())
        g.fitness = 0
        ge.append(g)


    #Score function

    def score():
        global points, game_speed
        points += 0.2
        if round(points) % 100 == 0 and round(points) != 0:
            game_speed += 0.2
        if game_speed % 1 > 0.9:
            game_speed = round(game_speed)
        text = FONT.render(f'Points: {str(round(points))}', True, (0, 0, 0))
        SCREEN.blit(text, (800, 50))

    #Print out statistics on screen

    def statistics():
        text_1 = FONT.render(f'Dinosaurs Alive:  {str(len(dinosaurs))}', True, (0, 0, 0))
        text_2 = FONT.render(f'Generation:  {pop.generation+1}', True, (0, 0, 0))
        text_3 = FONT.render(f'Game Speed:  {str(round(game_speed))}', True, (0, 0, 0))

        SCREEN.blit(text_1, (50, 450))
        SCREEN.blit(text_2, (50, 480))
        SCREEN.blit(text_3, (50, 510))

    # Function for moving background

    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            x_pos_bg = 0
        x_pos_bg -= game_speed

    # Function for spawning obstacles randomly (spawning flying after score is greater than 100)
    
    def spawnObstacle():
        rand_int = random.randint(0, 3)
        nextPos = random.randint(0,700)
        if rand_int == 0 or rand_int == 3 and points < 100:
            obstacles.append(SmallCactus(SMALL_CACTUS, random.randint(0,2)))
        elif rand_int == 1:
            obstacles.append(LargeCactus(LARGE_CACTUS, random.randint(0,2)))
        elif rand_int == 3:
            obstacles.append(Pterodactyl(PTERODACTYL))
        return nextPos

    #Game loop

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        SCREEN.fill((255,255,255))

        #Update and draw each dinosaur

        for dinosaur in dinosaurs:
            dinosaur.update()
            dinosaur.draw(SCREEN)

        #Spawn new obstacles    

        if len(obstacles) == 0:
            nextSpawn = spawnObstacle()
        if len(obstacles) > 0:
            if obstacles[-1].rect.x < nextSpawn:
                nextSpawn = spawnObstacle()

        #Check collision (remove if collision) and add fitness if dinosaur has passed obstacle       
            
        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            passedObstacle = obstacle.update()
            if passedObstacle:
                for g in ge:
                    g.fitness += 5

            for i, dinosaur in enumerate(dinosaurs):
                if dinosaur.rect.colliderect(obstacle.rect):
                    ge[i].fitness -= 1
                    remove(i)
                   

        #Get closest obstacle infront of dinosaur

        obstacleId = 0
        if len(dinosaurs) == 0:
            break
        else:
            if len(obstacles) > 1 and dinosaurs[0].rect.x > obstacles[0].rect.right:
                obstacleId = 1

        # Control for dinosaurs (get output from the net and jump/duck/run based on the outputs)

        if len(obstacles) > 0:
            for i, dinosaur in enumerate(dinosaurs):
                ge[i].fitness += 0.01
                output = nets[i].activate((abs(dinosaur.rect.right - obstacles[obstacleId].rect.x), obstacles[obstacleId].rect.bottom))  #distance((dinosaur.rect.x, dinosaur.rect.y), obstacle.rect.midtop) 
                
                if dinosaur.dino_duck != True:
                    if output[0] > 0.5 and dinosaur.rect.y == dinosaur.Y_POS and output[0] > output[1]:
                        dinosaur.dino_jump = True
                        dinosaur.dino_run = False
                if dinosaur.dino_jump != True:
                    if output[1] > 0.5 and output[1] > output[0]:
                        dinosaur.dino_duck = True
                        dinosaur.dino_run = False
                    elif dinosaur.dino_duck == True:
                        dinosaur.dino_run = True
                        dinosaur.dino_duck = False

        #Call functions
                        
        score()
        statistics()
        background()
        clock.tick(60)
        pygame.display.update()


#Set up neat, start a population, print statistics and run the population

def run(config_path):
    global pop
    config = neat.config.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path
    )

    pop = neat.Population(config)

    pop.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    pop.add_reporter(stats)

    winner = pop.run(eval_genomes, 50)

#Run the run function

if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')
    run(config_path)


