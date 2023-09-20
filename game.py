import pygame
from player import Player
from sharks import Sharks
from plants import Plant
import random
import os

class Game:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.win = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Evita los Obstáculos")
        self.font = pygame.font.Font(None, 36)
        self.score = 0
        self.max_score = 0
        self.instructions = [
            "¡Recolecta algas mientras evades a los tiburones y obten el mayor puntaje!",
            "Presiona 'W' para moverte hacia ARRIBA",
            "Presiona 'D' para moverte hacia la DERECHA",
            "Presiona 'S' para moverte hacia ABAJO",
            "Presiona 'A' para moverte hacia la IZQUIERDA",
            "Presiona 'X' para volver al menu principal"
        ]
        self.player = Player(50, 150)
        self.player_velocity = 4
        self.sharksList = []
        self.plantsList = []
        self.running = True
        self.clock = pygame.time.Clock()

    def show_instructions(self):
        instructions_given = True

        while instructions_given:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.win.fill((255, 255, 255))

            y_pos = 100
            for instruction in self.instructions:
                instructions_txt = self.font.render(instruction, True, (0, 0, 0))
                self.win.blit(instructions_txt, ((width - instructions_txt.get_width()) / 2, y_pos))
                y_pos += 50

            pygame.display.update()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_x]:
                self.show_menu()
                instructions_given = False

    def show_menu(self):
        menu = True
        while menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.win.fill((135, 206, 234))

            # Dibuja el texto del menú
            menu_txt = self.font.render("Presiona ESPACIO para comenzar", True, (0, 0, 0))
            self.win.blit(menu_txt, ((width - menu_txt.get_width()) / 2, (height - menu_txt.get_height()) / 2))

            instructions_text = self.font.render("Presiona 'I' para ver las instrucciones", True, (0, 0, 0))
            self.win.blit(instructions_text, ((width - instructions_text.get_width()) / 2, 250))

            self.best_score_text = self.font.render("Mejor puntaje: " + str(self.max_score), True, (0, 0, 0))
            self.win.blit(self.best_score_text, ((width - self.best_score_text.get_width()) / 2, 300))

            pygame.display.update()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                menu = False
            elif keys[pygame.K_i]:
                self.show_instructions()

    def restarting(self):
        self.sharksList = []
        self.plantsList = []
        player = Player(50, 150)

        if self.score > self.max_score:
            self.max_score = self.score

        self.score = 0
        self.win.fill((255, 255, 255))
        
        self.show_menu()
        self.running = True

    def generate_objects(self):
        if pygame.time.get_ticks() % 50 == 0:
            plant = Plant(self.width, random.randint(0, self.height - 20), 90, 90)
            obstacle = Sharks(self.width, random.randint(0, self.height - 20), 100, 80)
            self.plantsList.append(plant)
            self.sharksList.append(obstacle)
        for plant in self.plantsList:
            plant.move()
        for obstacle in self.sharksList:
            obstacle.move()

    def event_management(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def movement_management(self, keys):
        if keys[pygame.K_a]:
            self.player.move(-self.player_velocity, 0)
        if keys[pygame.K_d]:
            self.player.move(self.player_velocity, 0)
        if keys[pygame.K_w]:
            self.player.move(0, -self.player_velocity)
        if keys[pygame.K_s]:
            self.player.move(0, self.player_velocity)

    def verify_collision(self):
        for obstacle in self.sharksList:
            if self.player.check_collision(obstacle):
                self.restarting()
                break
        
        for plant in self.plantsList:
            if self.player.check_collision(plant):
                self.score += 1
                self.plantsList.remove(plant)

    def draw_elements(self):
        self.win.fill((135, 206, 234))

        puntuacion = self.font.render("Puntuación: " + str(self.score), True, (0, 0, 0))
        #puntaje_maximo = self.font.render("Puntaje máximo: " + str(self.max_score), True, (0, 0, 0))
        self.win.blit(puntuacion, (10, 10))
        self.win.blit(self.best_score_text, (10, 40))

        for plant in self.plantsList:
            plant.draw(self.win)
        for obstacle in self.sharksList:
            obstacle.draw(self.win)

        self.player.draw(self.win)

        pygame.display.update()

    def start_game(self):
        self.show_menu()

        while self.running:
            self.clock.tick(30)

            self.generate_objects()            

            keys = pygame.key.get_pressed()
            self.event_management()
            if keys[pygame.K_x]:
                self.restarting()
            elif keys[pygame.K_ESCAPE]:
                break
            else:
                self.movement_management(keys)
                self.verify_collision()
                self.draw_elements()

if __name__ == "__main__":
    pygame.init()
    width, height = 1000, 400
    juego = Game(width, height)
    juego.start_game()
    pygame.quit()
