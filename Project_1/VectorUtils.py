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
    
    @staticmethod
    def pointToWorldSpace(self, point, agent_heading, agent_side, agent_position):
        point_copy = engine.Vector2(point.x, point.y)

        mat_transform = [[1, 0, 0],
                         [0, 1, 0],
                         [0, 0, 1]]
        
        mat_transform = self.rotate_mat(mat_transform, agent_heading, agent_side)
        mat_transform = self.translate_mat(mat_transform, agent_position.x, agent_position.y)
        point_copy = self.transformVector(mat_transform, point_copy)

        return point_copy

        
    def rotate_mat(self, matrix, heading, side):

        copy_mat = matrix

        copy_mat[0][0] = heading.x
        copy_mat[0][1] = heading.y
        copy_mat[1][0] = side.x
        copy_mat[1][1] = side.y

        return copy_mat
    
    def translate_mat(self, matrix, x, y):

        copy_mat = matrix

        copy_mat[0][2] = x
        copy_mat[1][2] = y

        return copy_mat
    
    def transformVector(self, matrix, point):

        copy_point = point

        x = (matrix[0][0] * copy_point.x) + (matrix[0][1] * copy_point.y) + matrix[0][2]
        y = (matrix[1][0] * copy_point.x) + (matrix[1][1] * copy_point.y) + matrix[1][2]

        copy_point.x = x
        copy_point.y = y

        return copy_point