import playsound
from random import choice

class Music():
    def __init__(self):
        self.__variants = "ABG"
        self.__sequence = choice(self.__variants)
    def play(self):
        for bukva in self.__sequence:
            playsound.playsound(f"Sounds/{bukva}.mp3")
    def next(self):
        self.__sequence += choice(self.__variants)
    def check(self, guess):
        if guess == self.__sequence:
            playsound.playsound("Sounds/correct.wav")
        else:
            playsound.playsound("Sounds/incorrect.wav")

player = Music()
answer = input("Чё услышал: ").lower()
player.check(answer)
player.play()
player.next()
player.play()