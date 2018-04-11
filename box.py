class Box:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.w = random.randint(10, 100)
        self.h = random.randint(10, 50)
        self.x2 = self.x + self.w
        self.y2 = self.y + self.h
        self.speed = speed

    def draw(self):
        pygame.draw.rect(screen, BLACK, [self.x, self.y, self.w, self.h], 0)

    def move(self):
        self.x -= self.speed
        self.x2 = self.x + self.w
        self.y2 = self.y + self.h

def calc_score(score):
    return 'Score:' + str(score)

def check(player, box):
    top_left = player.x <= box.x <= player.x2 and player.y <= box.y <= player.y2
    bottom_right = player.x <= box.x2 <= player.x2 and player.y <= box.y2 <= player.y2
    if top_left or bottom_right:
        return True
    return False
