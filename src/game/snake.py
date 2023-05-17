from square import Square


class Snake(Square):

    def __init__(self, x=20, y=20, color='white'):
        super().__init__(x, y, color)
        self.body = self.create()

    def create(self):
        return [
            Square(self.x, self.y, self.color),
            Square(self.x, self.y, self.color),
            Square(self.x, self.y, self.color),
            Square(self.x, self.y, self.color)
        ]

    def append_last_postion(self):
        self.body.append(
                Square(
                    self.body[-1].x,
                    self.body[-1].y,
                    self.body[0].color
                )
            )
