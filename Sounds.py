import pygame, os, random

# always import Sounds when working with this (Use Sound.PlaySound.[Sound you want])

class PlaySound:
    # Title Screen Music~
    def TitleScreen(self):
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.load(os.path.join("Audio", "TitleScreen.ogg"))
        pygame.mixer.music.play(-1, 0)

    # Sound of clicking button/mouse
    def MouseClick(self):
        ClickSound = pygame.mixer.Sound(os.path.join("Audio", "Click.ogg"))
        ClickSound.play(0, 0, 0)

    # Actual game bgm
    def GameBGM(self):
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.load(os.path.join("Audio", "Typenbgm.ogg"))
        pygame.mixer.music.play(-1, 0)

    # This is a keyboard sound
    def KeyPress(self):
        RandKey = random.randint(1, 7)
        if RandKey == 1:
            Key1 = pygame.mixer.Sound(os.path.join("Audio", "Key1.ogg"))
            Key1.play(0, 0, 0)
        elif RandKey == 2:
            Key2 = pygame.mixer.Sound(os.path.join("Audio", "Key2.ogg"))
            Key2.play(0, 0, 0)
        elif RandKey == 3:
            Key3 = pygame.mixer.Sound(os.path.join("Audio", "Key3.ogg"))
            Key3.play(0, 0, 0)
        elif RandKey == 4:
            Key4 = pygame.mixer.Sound(os.path.join("Audio", "Key4.ogg"))
            Key4.play(0, 0, 0)
        elif RandKey == 5:
            Key5 = pygame.mixer.Sound(os.path.join("Audio", "Key5.ogg"))
            Key5.play(0, 0, 0)
        elif RandKey == 6:
            Key6 = pygame.mixer.Sound(os.path.join("Audio", "Key6.ogg"))
            Key6.play(0, 0, 0)
        elif RandKey == 7:
            Key7 = pygame.mixer.Sound(os.path.join("Audio", "Key7.ogg"))
            Key7.play(0, 0, 0)

    # This is the sound for a Keyboard Space
    def KeySpace(self):
        Space = pygame.mixer.Sound(os.path.join("Audio", "KeySpace.ogg"))
        Space.play(0, 0, 0)

    # This is a Clock Tick sound
    def ClockTick(self):
        ClockTick = pygame.mixer.Sound(os.path.join("Audio", "Clock_Tick.ogg"))
        ClockTick.play(0, 0, 0)

    # This is a sound for a dice rolling
    def DiceRoll(self):
        RandDice = random.randint(1, 3)
        if RandDice == 1:
            Dice1 = pygame.mixer.Sound(os.path.join("Audio", "Dice_Roll_1.ogg"))
            Dice1.play(0, 0, 0)
        elif RandDice == 2:
            Dice2 = pygame.mixer.Sound(os.path.join("Audio", "Dice_Roll_2.ogg"))
            Dice2.play(0, 0, 0)
        elif RandDice == 3:
            Dice3 = pygame.mixer.Sound(os.path.join("Audio", "Dice_Roll_2.ogg"))
            Dice3.play(0, 0, 0)

    # Should play when you answer a question correct
    def CorrectAns(self):
        Correct = pygame.mixer.Sound(os.path.join("Audio", "Correct_SFX.ogg"))
        Correct.play(0, 0, 0)

    # Should play when you answer a question correct
    def WrongAns(self):
        Wrong = pygame.mixer.Sound(os.path.join("Audio", "Wrong_SFX.ogg"))
        Wrong.play(0, 0)

    # Sound for climbing
    def Climbing(self):
        Climb = pygame.mixer.Sound(os.path.join("Audio", "Climbing.ogg"))
        Climb.play(0, 0, 0)

    # Play this at end screen / placing flag
    def WinMusic(self):
        pygame.mixer.music.load(os.path.join("Audio", "Win_Music.ogg"))
        pygame.mixer.music.play(0, 0)

# Let me know if there is something missing ):
