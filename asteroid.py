from circleshape import *
from constants import *

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