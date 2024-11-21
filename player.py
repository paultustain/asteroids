import pygame
from circleshape import CircleShape
from constants import (
    PLAYER_RADIUS, 
    PLAYER_TURN_SPEED, 
    PLAYER_SPEED, 
    SHOT_RADIUS, 
    PLAYER_SHOOT_SPEED, 
    PLAYER_SHOOT_COOLDOWN
)

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, 5) 
    
    def draw(self, screen):
        pygame.draw.circle(
            screen, 
            'white', 
            self.position, 
            self.radius
        )

    def update(self, dt):
        self.position += self.velocity * dt


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0 
        self.cooldown = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(
            screen, 
            'white', 
            self.triangle(), 
            2
        )

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.cooldown = max(0, self.cooldown - dt)
        
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.cooldown == 0:
                self.shoot(dt)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, dt):
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.cooldown += PLAYER_SHOOT_COOLDOWN
