# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 13:25:38 2020

@author: emreo
"""
import pygame
import time
pygame.init()

class GameCore():
    def __init__(self):
        self.windows_width = 1280
        self.windows_height = 720
        self.window = pygame.display.set_mode((self.windows_width,self.windows_height))
        pygame.display.set_caption("Meeting Animals")
        
        self.background = pygame.image.load("oyun.png")
        self.Animals = Animals()
        
        self.clock = pygame.time.Clock()
        
    def draw(self):
        self.window.blit(self.background,(0,0))
        self.Animals.animal_draw(self.window)
        pygame.display.update()
        

    def gameLoop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            
        
        self.draw()
        
        
class KordinatAnimals():
    
    def __init__(self,x1,x2,y1,y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2


ari = KordinatAnimals(810,930,165,242)  
aslan = KordinatAnimals(390, 555, 520, 680)
esek = KordinatAnimals(985, 1125, 300, 500)
inek = KordinatAnimals(160, 335, 350, 500)
kartal = KordinatAnimals(525, 635, 70, 235)
keci = KordinatAnimals(460, 600, 335, 470)
kedi = KordinatAnimals(170, 265, 505, 675)
kelebek = KordinatAnimals(1135, 1248, 230, 315)
kopek = KordinatAnimals(720, 840, 550, 670)
koyun = KordinatAnimals(720, 852, 340, 465)
tavuk = KordinatAnimals(1040, 1140, 550, 680)

    
class Animals():
    
  
    def __init__(self):
        self.ari = pygame.image.load("ari.png")
        self.aslan = pygame.image.load("aslan.png")
        self.esek = pygame.image.load("esek.png")
        self.inek = pygame.image.load("inek.png")
        self.kartal = pygame.image.load("kartal.png")
        self.keci = pygame.image.load("keci.png")
        self.kedi = pygame.image.load("kedi.png")
        self.kelebek = pygame.image.load("kelebek.png")
        self.kopek = pygame.image.load("kopek.png")
        self.koyun = pygame.image.load("koyun.png")
        self.tavuk = pygame.image.load("tavuk.png")  
        
        
        self.ari = pygame.transform.scale(self.ari,(250,350))
        self.aslan = pygame.transform.scale(self.aslan,(250,350))
        self.esek = pygame.transform.scale(self.esek,(250,350))
        self.inek = pygame.transform.scale(self.inek,(250,350))
        self.kartal = pygame.transform.scale(self.kartal,(250,350))
        self.keci = pygame.transform.scale(self.keci,(250,350))
        self.kedi = pygame.transform.scale(self.kedi,(250,350))
        self.kelebek = pygame.transform.scale(self.kelebek,(250,350))
        self.kopek = pygame.transform.scale(self.kopek,(250,350))
        self.koyun = pygame.transform.scale(self.koyun,(250,350))
        self.tavuk = pygame.transform.scale(self.tavuk,(250,350))
        
        self.resimboyutuX, self.resimboyutuY  = 250, 350
       
        self.animalslist = [self.ari,
                            self.aslan,
                            self.esek,
                            self.inek,
                            self.kartal,
                            self.keci,
                            self.kedi,
                            self.kelebek,
                            self.kopek,
                            self.koyun,
                            self.tavuk
                            ]
        
    def animal_draw(self,window):
        
        pygame.mixer.music.set_volume(0.2)
        
        sol,orta,sag = pygame.mouse.get_pressed()
        
        pos = pygame.mouse.get_pos()
        x = pos[0]
        y = pos[1]
        
        if ari.x1 < x < ari.x2 and ari.y1 < y < ari.y2:
            if x + self.resimboyutuX > 1280 and y + self.resimboyutuY > 720:
                    window.blit(self.ari,(x-self.resimboyutuX,y-self.resimboyutuY))
            elif x + self.resimboyutuX > 1280:
                window.blit(self.ari,(x-self.resimboyutuX,y))
            elif y + self.resimboyutuY > 720:
                window.blit(self.ari,(x,y-self.resimboyutuY))
            else:
                window.blit(self.ari,(x,y))
        
            if sol == 1:
                pygame.mixer.music.load("ari.mp3") 
                pygame.mixer.music.play()
                time.sleep(0.5)
                
        elif aslan.x1 < x < aslan.x2 and aslan.y1 < y < aslan.y2:
            if x + self.resimboyutuX > 1280 and y + self.resimboyutuY > 720:
                    window.blit(self.aslan,(x-self.resimboyutuX,y-self.resimboyutuY))
            elif x + self.resimboyutuX > 1280:
                window.blit(self.aslan,(x-self.resimboyutuX,y))
            elif y + self.resimboyutuY > 720:
                window.blit(self.aslan,(x,y-self.resimboyutuY))
            else:
                window.blit(self.aslan,(x,y))
            if sol == 1:
                pygame.mixer.music.load("aslan.mp3") 
                pygame.mixer.music.play()
                time.sleep(0.5)
                
        elif esek.x1 < x < esek.x2 and esek.y1 < y < esek.y2:
            if x + self.resimboyutuX > 1280 and y + self.resimboyutuY > 720:
                    window.blit(self.esek,(x-self.resimboyutuX,y-self.resimboyutuY))
            elif x + self.resimboyutuX > 1280:
                window.blit(self.esek,(x-self.resimboyutuX,y))
            elif y + self.resimboyutuY > 720:
                window.blit(self.esek,(x,y-self.resimboyutuY))
            else:
                window.blit(self.esek,(x,y))
            if sol == 1:
                pygame.mixer.music.load("esek.mp3") 
                pygame.mixer.music.play()
                time.sleep(0.5)
                
        elif inek.x1 < x < inek.x2 and inek.y1 < y < inek.y2:
            if x + self.resimboyutuX > 1280 and y + self.resimboyutuY > 720:
                    window.blit(self.inek,(x-self.resimboyutuX,y-self.resimboyutuY))
            elif x + self.resimboyutuX > 1280:
                window.blit(self.inek,(x-self.resimboyutuX,y))
            elif y + self.resimboyutuY > 720:
                window.blit(self.inek,(x,y-self.resimboyutuY))
            else:
                window.blit(self.inek,(x,y))
            if sol == 1:
                pygame.mixer.music.load("inek.mp3") 
                pygame.mixer.music.play()
                time.sleep(0.5)
                
        elif kartal.x1 < x < kartal.x2 and kartal.y1 < y < kartal.y2:
            if x + self.resimboyutuX > 1280 and y + self.resimboyutuY > 720:
                    window.blit(self.kartal,(x-self.resimboyutuX,y-self.resimboyutuY))
            elif x + self.resimboyutuX > 1280:
                window.blit(self.kartal,(x-self.resimboyutuX,y))
            elif y + self.resimboyutuY > 720:
                window.blit(self.kartal,(x,y-self.resimboyutuY))
            else:
                window.blit(self.kartal,(x,y))
            if sol == 1:
                pygame.mixer.music.load("kartal.mp3") 
                pygame.mixer.music.play()
                time.sleep(0.5)
                
        elif keci.x1 < x < keci.x2 and keci.y1 < y < keci.y2:
            if x + self.resimboyutuX > 1280 and y + self.resimboyutuY > 720:
                    window.blit(self.keci,(x-self.resimboyutuX,y-self.resimboyutuY))
            elif x + self.resimboyutuX > 1280:
                window.blit(self.keci,(x-self.resimboyutuX,y))
            elif y + self.resimboyutuY > 720:
                window.blit(self.keci,(x,y-self.resimboyutuY))
            else:
                window.blit(self.keci,(x,y))
            if sol == 1:
                pygame.mixer.music.load("keci.mp3") 
                pygame.mixer.music.play()
                time.sleep(0.5)
                
        elif kedi.x1 < x < kedi.x2 and kedi.y1 < y < kedi.y2:
            if x + self.resimboyutuX > 1280 and y + self.resimboyutuY > 720:
                    window.blit(self.kedi,(x-self.resimboyutuX,y-self.resimboyutuY))
            elif x + self.resimboyutuX > 1280:
                window.blit(self.kedi,(x-self.resimboyutuX,y))
            elif y + self.resimboyutuY > 720:
                window.blit(self.kedi,(x,y-self.resimboyutuY))
            else:
                window.blit(self.kedi,(x,y))
            if sol == 1:
                pygame.mixer.music.load("kedi.mp3") 
                pygame.mixer.music.play()
                time.sleep(0.5)
                
        elif kelebek.x1 < x < kelebek.x2 and kelebek.y1 < y < kelebek.y2:
            if x + (self.resimboyutuX) > 1280 and y + (self.resimboyutuY) > 720:              
                window.blit(self.kelebek,(x-self.resimboyutuX,y-self.resimboyutuY))
            elif x + self.resimboyutuX > 1280:
                window.blit(self.kelebek,(x-self.resimboyutuX,y))
            elif y + self.resimboyutuY > 720:
                window.blit(self.kelebek,(x,y-self.resimboyutuY))
            else:
                window.blit(self.kelebek,(x,y))
                
            
        elif kopek.x1 < x < kopek.x2 and kopek.y1 < y < kopek.y2:
            if x + self.resimboyutuX > 1280 and y + self.resimboyutuY > 720:
                    window.blit(self.kopek,(x-self.resimboyutuX,y-self.resimboyutuY))
            elif x + self.resimboyutuX > 1280:
                window.blit(self.kopek,(x-self.resimboyutuX,y))
            elif y + self.resimboyutuY > 720:
                window.blit(self.kopek,(x,y-self.resimboyutuY))
            else:
                window.blit(self.kopek,(x,y))
            if sol == 1:
                pygame.mixer.music.load("kopek.mp3") 
                pygame.mixer.music.play()
                time.sleep(0.5)
                
        elif koyun.x1 < x < koyun.x2 and koyun.y1 < y < koyun.y2:
            if x + self.resimboyutuX > 1280 and y + self.resimboyutuY > 720:
                    window.blit(self.koyun,(x-self.resimboyutuX,y-self.resimboyutuY))
            elif x + self.resimboyutuX > 1280:
                window.blit(self.koyun,(x-self.resimboyutuX,y))
            elif y + self.resimboyutuY > 720:
                window.blit(self.koyun,(x,y-self.resimboyutuY))
            else:
                window.blit(self.koyun,(x,y))
            if sol == 1:
                pygame.mixer.music.load("koyun.mp3") 
                pygame.mixer.music.play()
                time.sleep(0.5)
                
        elif tavuk.x1 < x < tavuk.x2 and tavuk.y1 < y < tavuk.y2:
            if x + self.resimboyutuX > 1280 and y + self.resimboyutuY > 720:
                    window.blit(self.tavuk,(x-self.resimboyutuX,y-self.resimboyutuY))
            elif x + self.resimboyutuX > 1280:
                window.blit(self.tavuk,(x-self.resimboyutuX,y))
            elif y + self.resimboyutuY > 720:
                window.blit(self.tavuk,(x,y-self.resimboyutuY))
            else:
                window.blit(self.tavuk,(x,y))
            if sol == 1:
                pygame.mixer.music.load("tavuk.mp3") 
                pygame.mixer.music.play()
                time.sleep(0.5)
                
        pygame.display.update() 
            
Game = GameCore()

while True:
    Status = Game.gameLoop()
    if Status == "QUIT":
        break
    
pygame.quit()