import pygame as engine
from pygame.locals import *

class VectorUtils:
   
    @staticmethod
    def truncate_vec(agent, vec):
        if vec.length() > agent.maxSpeed:
            vec.normalize()
            vec.x *= agent.maxSpeed
            vec.y *= agent.maxSpeed

        return vec
    @staticmethod
    def perp(vec):
        return engine.Vector2(-vec.y, vec.x)