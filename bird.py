class Bird:
    def __init__(self):
        self.direction = 1
        self.position = 0

    def turn(self):
        self.direction = self.direction * (-1)
        return self.direction

    def hop(self):
        self.position = self.direction + self.position
        return self.position

    def location(self):
        print("The Bird is at location:", self.position)



