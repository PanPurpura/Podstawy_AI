import pygame as engine
from pygame.locals import *
from VectorUtils import *
from SteeringBehaviours import *

class Agent:

    def __init__(
            self,
            id_,
            position_ = engine.Vector2(100, 100),
            bounding_radius_ = 0,
            scale_ = 1.0,
            tagged_ = False,
            velocity_ = engine.Vector2(0, 0),
            heading_ = engine.Vector2(0, 0),
            side_ = engine.Vector2(0, 0),
            mass_ = 1.0,
            maxSpeed_ = 0.15,
            maxForce_ = 1.0,
            maxTurnRate_ = 0,
            world_ = None,
            steeringBeh_ = SteeringBehaviours(True),
            ):
        self.id = id_
        self.position = position_
        self.bounding_radius_ = bounding_radius_
        self.scale = scale_
        self.tagged = tagged_
        self.velocity = velocity_
        self.heading = heading_
        self.side = side_
        self.mass = mass_
        self.maxSpeed = maxSpeed_
        self.maxForce = maxForce_
        self.maxTurnRate = maxTurnRate_
        self.world = world_
        self.steeringBeh = steeringBeh_

    def update(self, time_elapsed):
        steeringForce = self.steeringBeh.calculate(engine.Vector2(200, 200), self)
        #print(steeringForce)
        acceleration = steeringForce / self.mass
        self.velocity += acceleration * time_elapsed
        self.velocity = VectorUtils.truncate_vec(self, self.velocity)
        self.position += self.velocity * time_elapsed
        #print("Position: " + str(self.position))

        if self.velocity.length_squared() > 0.00000001:
            self.heading = self.velocity.normalize()
            self.side = VectorUtils.perp(self.heading)

    def move(self, position):
        self.position += position

    def draw(self, gameWorld, position, radius):
        RED = (255, 0, 0)
        engine.draw.circle(gameWorld, RED, position, radius)



