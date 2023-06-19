from tkinter import font
import pygame
import settings

pygame.init()


scoreValue = 0

textfont = pygame.font.SysFont('arial', 16)
text = textfont.render("SCORE: " + str(scoreValue), True, (255, 255, 0))
textRect = text.get_rect()
textRect.topleft = (8, 5)
