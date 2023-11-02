from threading import Thread
from time import sleep


class Bucket():

    def __init__(self):
        self.fish_list = []
        self.fish_amount = 0

    def catch_fish(self, list):
        while len(list) > 0:
            caught_fish = list.pop()
            self.fish_list.append(caught_fish)
            print('Рыбка попалась на крючок')
            sleep(5)
        return list

    def make_thread(self, list):
        new_thread = Thread(target=self.catch_fish(list))
        new_thread.start()
        return list

    def get_fish_amount(self):
        for f in self.fish_list:
            self.fish_amount += 1


