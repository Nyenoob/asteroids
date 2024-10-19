from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        self.velocity = 0
    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)
    
    def move(self,dt):
        self.position += self.velocity * dt
    
    def update(self, dt):
        self.move(dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        #here we spawn!!!
        speed_up=1.2
        random_angle=random.uniform(20, 50) #should generate an angle between 20 and 50
        new_vel1 = self.velocity.rotate(random_angle) 
        new_vel2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = new_vel1*speed_up
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = new_vel2*speed_up
        