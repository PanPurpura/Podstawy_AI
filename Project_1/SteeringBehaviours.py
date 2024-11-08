import pygame as engine
from pygame.locals import *
import random
from VectorUtils import *

class SteeringBehaviours:

    WANDER_RADIUS = 1.0
    WANDER_DISTANCE = 1.0
    WANDER_JITTER = 1.0

    def __init__(self, seek_ = False, wander_ = False):
        self.seekOn = seek_
        self.wanderOn = wander_


    def seek(self, targetPos, agent):
        desiredVelocity = (targetPos - agent.position).normalize() * agent.maxSpeed
        return desiredVelocity - agent.velocity
    
    def wander(self, agent):
        wanderTarget = engine.Vector2(0, 0)

        wanderTarget += engine.Vector2(random.uniform(-1, 1) * self.WANDER_JITTER,
                                       random.uniform(-1, 1) * self.WANDER_JITTER)

        wanderTarget.normalize()
        wanderTarget *= self.WANDER_RADIUS

        targetLocal = wanderTarget + engine.Vector2(self.WANDER_DISTANCE, 0)
        targetWorld = VectorUtils.pointToWorldSpace(VectorUtils(),
                                                    targetLocal,
                                                    agent.heading,
                                                    agent.side,
                                                    agent.position)
        
        return targetWorld - agent.position



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

        if self.seekOn == True:
            force = self.seek(targetPos, agent) * 0.8

            if self.accumulateForce(steeringForce, force, agent) == False:
                return steeringForce
            
        if self.wanderOn == True:
            force = self.wander(agent) * 0.9

            if self.accumulateForce(steeringForce, force, agent):
                return steeringForce
            
        return steeringForce