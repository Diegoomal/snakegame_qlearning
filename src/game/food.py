from square import Square


class Food(Square):

    def __init__(self, x=20, y=20, color='purple'):
        super().__init__(x, y, color)
        self.update_position()
        self.color = color
        self.body = self.create()

    def create(self):
        return [Square(self.x, self.y, self.color)]
