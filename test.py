import pygame 
  
pygame.init() 
  
surface = pygame.display.set_mode((400,300)) 
  
color = (255,0,0) 
while True:
	pygame.draw.rect(surface, color, pygame.Rect(0, 600, 600, 20)) 
	pygame.display.flip()
