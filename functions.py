from random import choice

class Game:
    def __init__(self):
        self.clicks = 0
        self.click_speed = 1
        self.level = 1
        self.level_cost = 2

    def add_click(self):
        self.clicks += self.click_speed

    def level_up(self):
        if self.clicks >= self.level_cost:
            self.clicks -= self.level_cost
            self.level += 1
            self.click_speed *= 2
            self.level_cost = self.level_cost ** 2

    def save(self):
        f = open('data/save.txt', 'w')
        f.write(str(self.clicks)+'\n')
        f.write(str(self.click_speed)+'\n')
        f.write(str(self.level)+'\n')
        f.write(str(self.level_cost))
        f.close()

    def load(self):
        f = open('data/save.txt')
        i = 0
        for line in f:
            line = line.strip()
            i += 1
            if i == 1:
                self.clicks = int(line)
            elif i == 2:
                self.click_speed = int(line)
            elif i == 3:
                self.level = int(line)
            elif i == 4:
                self.level_cost = int(line)
        f.close()


class SplashManager:
    def __init__(self):
        self.catalog = []

    def load_splashes(self):
        f = open('data/splashes.txt')
        for line in f:
            line = line.strip()
            self.catalog.append(line)
        f.close()

    def get(self):
        return choice(self.catalog)

class DataManager:
    def __init__(self):
        self.author = 'AUTHORNAME'
        self.gamename = 'GAMENAME'
        self.version = 'VERSION'

    def load_data(self):
        f = open('data/game.txt')
        for line in f:
            line = line.strip()
            data = line.split(':')
            if data[0] == 'gamename':
                self.gamename = data[1]
            if data[0] == 'author':
                self.author = data[1]
            if data[0] == 'version':
                self.version = data[1]
        f.close()