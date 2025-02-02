from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y,SHOT_RADIUS)
        self.velocity = 0
    def draw(self, screen):
        pygame.draw.circle(screen,"red",self.position,self.radius,2)
    
    def move(self,dt):
        self.position += self.velocity * dt
    
    def update(self, dt):
        self.move(dt)