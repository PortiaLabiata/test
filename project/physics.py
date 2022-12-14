import numpy as np
import pygame
from math import sin, cos, sqrt, radians, degrees

def rotate_vector(v, alpha):
    rot = np.array([[cos(alpha), -sin(alpha)], [sin(alpha), cos(alpha)]])
    return np.transpose(np.dot(np.linalg.inv(rot), np.transpose(v)))

def rotate_image(img, rect, alpha):
    rot_img = pygame.transform.rotate(img, degrees(alpha))
    rot_rect = rot_img.get_rect(center = rect.center)
    return rot_img, rot_rect

class MaterialPoint:
    r0 = np.array([0, 0])
    r = r0
    a = np.array([0, 0])
    v0 = np.array([0, 0])
    v = v0
    m = 0
    dt = 1
    forces = []

    def __init__(self, r0, v0, m, dt):
        self.r0 = r0
        self.r = self.r0
        self.v0 = v0
        self.v = v0
        self.m = m
        self.dt = dt

    def update_coordinates(self):
        self.a = sum(self.forces) / self.m
        self.v = self.v + self.a * self.dt
        self.r = self.r + self.v * self.dt

    def apply_force(self, f):
        self.forces.append(f)

class ALM(MaterialPoint, pygame.sprite.Sprite):
    angle = radians(0)
    main_thrust = np.array([0, -1.5])
    rcs_left_thrust = np.array([-1, 0])
    rcs_right_thrust = np.array([1, 0])
    angular_velocity = radians(0.1)
    current_ang_vel = 0

    main_fuel = 5000
    rcs_fuel = 1000


    def __init__(self, r0, v0, m, dt):
        pygame.sprite.Sprite.__init__(self)
        self.r0 = r0
        self.image = pygame.Surface((45, 45))
        self.image = pygame.image.load("./ALM_anims/ALM0.bmp").convert_alpha()

        """
        self.im0 = pygame.image.load("./ALM_anims/ALM0.bmp").convert_alpha()
        self.im1 = pygame.image.load("./ALM_anims/ALM1.bmp").convert_alpha()
        self.im2 = pygame.image.load("./ALM_anims/ALM2.bmp").convert_alpha()
        self.im3 = pygame.image.load("./ALM_anims/ALM3.bmp").convert_alpha()
        self.im4 = pygame.image.load("./ALM_anims/ALM4.bmp").convert_alpha()
        self.im_1 = pygame.image.load("./ALM_anims/ALM-1.bmp").convert_alpha()
        self.im_2 = pygame.image.load("./ALM_anims/ALM-2.bmp").convert_alpha()
        self.im_3 = pygame.image.load("./ALM_anims/ALM-3.bmp").convert_alpha()
        """

        self.rect = self.image.get_rect(center=(self.r0[0], self.r0[1]))
        self.r = self.r0
        self.v0 = v0
        self.v = v0
        self.m = m
        self.dt = dt

    def update_coordinates(self):
        MaterialPoint.update_coordinates(self)
        self.rect.center = (self.r[0], self.r[1])
        self.angle += self.current_ang_vel
        degangle = degrees(self.angle)
        if degangle >= 360 or degangle <= -360:
            self.angle = 0
        """
        if degangle >= 0 and degangle < 90:
            self.image = self.im0
        elif degangle >= 90 and degangle < 180
        """


    def main_stage_thrust(self, perc):
        self.apply_force(rotate_vector(self.main_thrust*perc/100, self.angle))
        #self.main_fuel -= 0.01

    def rotate_clockwise(self):
        self.current_ang_vel += self.angular_velocity*1/30
        self.angle += self.current_ang_vel
        self.rcs_fuel -= 0.001


    def rotate_counterclockwise(self):
        self.current_ang_vel -= self.angular_velocity*1/30
        self.angle += self.current_ang_vel
        self.rcs_fuel -= 0.001

    def hover_left(self):
        self.apply_force(rotate_vector(self.rcs_left_thrust, self.angle))
        self.rcs_fuel -= 0.001

    def hover_right(self):
        self.apply_force(rotate_vector(self.rcs_right_thrust, self.angle))
        self.rcs_fuel -= 0.001
