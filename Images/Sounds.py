import pygame, os, random

# always import Sounds when working with this (Use Sound.PlaySound.[Sound you want])

class PlaySound:
    # Title Screen Music~
    def TitleScreen(self):
        pygame.mixer.music.load(os.path.join("Audio", "TitleScreen.ogg"))
        pygame.mixer.music.play(0, 0)

    # Sound of clicking button/mouse
    def MouseClick(self):
        pygame.mixer.music.load(os.path.join("Audio", "Click.ogg"))
        pygame.mixer.music.play(0, 0)

    # Actual game bgm
    def GameBGM(self):
        pygame.mixer.music.load(os.path.join("Audio", "Typenbgm.ogg"))
        pygame.mixer.music.play(0, 0)

    # This is a keyboard sound
    def KeyPress(self):
        RandKey = random.randint(1, 7)
        if RandKey == 1:
            pygame.mixer.music.load(os.path.join("Audio", "Key1.ogg"))
            pygame.mixer.music.play(0, 0)
        elif RandKey == 2:
            pygame.mixer.music.load(os.path.join("Audio", "Key2.ogg"))
            pygame.mixer.music.play(0, 0)
        elif RandKey == 3:
            pygame.mixer.music.load(os.path.join("Audio", "Key3.ogg"))
            pygame.mixer.music.play(0, 0)
        elif RandKey == 4:
            pygame.mixer.music.load(os.path.join("Audio", "Key4.ogg"))
            pygame.mixer.music.play(0, 0)
        elif RandKey == 5:
            pygame.mixer.music.load(os.path.join("Audio", "Key5.ogg"))
            pygame.mixer.music.play(0, 0)
        elif RandKey == 6:
            pygame.mixer.music.load(os.path.join("Audio", "Key6.ogg"))
            pygame.mixer.music.play(0, 0)
        elif RandKey == 7:
            pygame.mixer.music.load(os.path.join("Audio", "Key7.ogg"))
            pygame.mixer.music.play(0, 0)

    # This is the sound for a Keyboard Space
    def KeySpace(self):
        pygame.mixer.music.load(os.path.join("Audio", "KeySpace.ogg"))
        pygame.mixer.music.play(0, 0)

    # This is a Clock Tick sound

    # This is a sound for a dice rolling
    def DiceRoll(self):
        RandDice = random.randint(1, 3)
        if RandDice == 1:
            pygame.mixer.music.load(os.path.join("Audio", "Dice_Roll_1"))
            pygame.mixer.music.play(0, 0)
        elif RandDice == 2:
            pygame.mixer.music.load(os.path.join("Audio", "Dice_Roll_2"))
            pygame.mixer.music.play(0, 0)
        elif RandDice == 3:
            pygame.mixer.music.load(os.path.join("Audio", "Dice_Roll_2"))
            pygame.mixer.music.play(0, 0)

    # Should play when you answer a question correct
    def CorrectAns(self):
        pygame.mixer.music.load(os.path.join("Audio", "Correct_SFX.ogg"))
        pygame.mixer.music.play(0, 0)

    # Should play when you answer a question correct
    def WrongAns(self):
        pygame.mixer.music.load(os.path.join("Audio", "Wrong_SFX.ogg"))
        pygame.mixer.music.play(0, 0)

    # Sound for climbing
    def Climbing(self):
        pygame.mixer.music.load(os.path.join("Audio", "Climbing.ogg"))
        pygame.mixer.music.play(0, 0)

    # Play this at end screen / placing flag
    def WinMusic(self):
        pygame.mixer.music.load(os.path.join("Audio", "Win_Music.ogg"))
        pygame.mixer.music.play(0, 0)

# Let me know if there is something missing ):
