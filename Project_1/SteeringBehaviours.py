import pygame as engine
from pygame.locals import *

class SteeringBehaviours:

    def __init__(self, seek_ = False):
        self.seekOn = seek_


    def seek(self, targetPos, agent):
        desiredVelocity = (targetPos - agent.position).normalize() * agent.maxSpeed
        return desiredVelocity - agent.velocity

    def accumulateForce(self, runningTot, forceToAdd, agent):
        magnitudeSoFar = runningTot.length()
        magnitudeRemaining = agent.maxForce - magnitudeSoFar

        if magnitudeRemaining <= 0.0:
            return False
        
        magnitudeToAdd = forceToAdd.length()

        if magnitudeToAdd < magnitudeRemaining:
            runningTot += forceToAdd
        else:
            runningTot += (forceToAdd.normalize() * magnitudeRemaining)

        return True
    
    def calculate(self, targetPos, agent):
        steeringForce = engine.Vector2(0, 0)

        force = None

        if (self.seekOn == True):
            force = self.seek(targetPos, agent) * 1.5

            if self.accumulateForce(steeringForce, force, agent) == False:
                return steeringForce
            
        return steeringForce