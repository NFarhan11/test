import pygame, sys

pygame.init()

class Object(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()

objs = Object()
print(objs)