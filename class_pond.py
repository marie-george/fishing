from class_fish import Fish


class Pond():

    def __init__(self):
        self.fish_amount = 5
        self.fish_list = []

    def create_shoal(self):
        for f in range(self.fish_amount):
            fish = Fish()
            self.fish_list.append(fish)

