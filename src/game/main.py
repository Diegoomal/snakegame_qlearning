import numpy as np

from configs import Configs
from device import Device
from food import Food
from snake import Snake
from square import Square


class Game:

    def __init__(self):

        self.vel = [[20, 0], [0, 0], [0, 0], [0, 0]]

        self.device = Device()
        # ações teclado
        self.device.set_vel(self.vel)

        self.food = Food(x=20, y=20, color='gold').create()

        self.snake = Snake(
            x=Configs.START_POSITION_X,
            y=Configs.START_POSITION_Y,
            color='white'
            ).create()

    def draw(self):

        self.device.canvas.delete('all')

        for s in self.snake:
            s.update()
            self.device.canvas.create_polygon(s.pos(), fill=s.color)

        for f in self.food:
            f.update()
            self.device.canvas.create_polygon(f.pos(), fill=f.color)

    def update(self):

        # snake position update

        for i in range(len(self.vel)-1, 0, -1):
            self.vel[i] = self.vel[i-1]

        for i in range(len(self.vel)):
            self.snake[i].velx = self.vel[i][0]
            self.snake[i].vely = self.vel[i][1]

        # snake and food colision

        if (self.snake[0].pos() == self.food[0].pos()):

            # self.food[0].x = Square.get_random_position_x()
            # self.food[0].y = Square.get_random_position_y()
            self.food[0].update_position()

            self.vel.append([0, 0])
            self.snake.append(
                Square(
                    self.snake[-1].x,
                    self.snake[-1].y,
                    self.snake[0].color
                )
            )

        self.device.canvas.after(Configs.UPDATE_TIME)
        self.device.window.update_idletasks()
        self.device.window.update()

    def run(self, random_play=False):
        while True:
            if random_play:
                self.random_snake_moviment()
            self.update()
            self.draw()

    def random_snake_moviment(self):

        n_action = np.random.randint(0, 4)

        if n_action.__eq__(0):
            if (self.vel[0] != [0, 20]):
                self.vel[0] = [0, -20]
        elif n_action.__eq__(1):
            if (self.vel[0] != [0, -20]):
                self.vel[0] = [0, 20]
        elif n_action.__eq__(2):
            if (self.vel[0] != [20, 0]):
                self.vel[0] = [-20, 0]
        elif n_action.__eq__(3):
            if (self.vel[0] != [-20, 0]):
                self.vel[0] = [20, 0]


if __name__ == "__main__":

    np.random.seed(42)

    Game().run(random_play=False)
