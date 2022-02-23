# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 00:36:06 2020

@author: emreo
"""
import pygame
pygame.init()


class Baslangic():

    def __init__(self):
        self.windows_width = 1280
        self.windows_height = 720
        self.window = pygame.display.set_mode((self.windows_width,self.windows_height))
        pygame.display.set_caption("Meeting Animals")
        
        self.background = pygame.image.load("giris.png")
        
        self.clock = pygame.time.Clock()
        
        self.playX1 = 465
        self.playX2 = 810
        self.playY1 = 580
        self.playY2 = 660
        
        
    def draw(self):
        self.window.blit(self.background,(0,0))
        pygame.display.update()
        

    def baslangicLoop(self):
        
        pos = pygame.mouse.get_pos()
        x = pos[0]
        y = pos[1]
        
        sol,orta,sag = pygame.mouse.get_pressed()
        

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
        
        if self.playX1 < x < self.playX2 and self.playY1 < y < self.playY2:
            if sol == 1:
                import meetinganimals
                meetinganimals()     
        self.draw()
        
Baslangic = Baslangic()
pygame.mixer.music.load("girisekrani.mp3")
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play()
while True:

    Status = Baslangic.baslangicLoop()
    if Status == "QUIT":
        break
    
pygame.quit()