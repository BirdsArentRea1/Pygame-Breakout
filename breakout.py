import random
import pygame
pygame.init()

screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Pong")

hit = pygame.mixer.Sound('pluck.mp3')

doExit = False

clock = pygame.time.Clock()

p1x = 400
p1y = 400


bx = 300
by = 200

bVx = 5
bVy = 5

p1Score = 0
p2Score = 0

class brick:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.color = (random.randrange(100, 250),random.randrange(100, 250),random.randrange(100, 250))
        self.isDead = False
    def draw(self):
        if not self.isDead:
            pygame.draw.rect(screen, self.color, (self.xpos, self.ypos, 100, 50))
        
#bounding box collision
    def collide(self, bx, by):
        if not self.isDead:
            if (bx + 20 > self.xpos and
                bx < self.xpos + 100 and
                by + 20 > self.ypos and
                by < self.ypos + 50):
                self.isDead = True
                print("HIT")
                pygame.mixer.Sound.play(hit) 
                
                return True
        return False
    
        
b1 = brick(50, 50)
b2 = brick(200, 50)
b3 = brick(350, 50)
b4 = brick(500, 50)
b5 = brick(650, 50)
b6 = brick(50, 130)
b7 = brick(200, 130)
b8 = brick(350, 130)
b9 = brick(500, 130)
b10 = brick(650, 130)
  
#level1 = pygame.mixer.music.load('Breakout_phase_1.mp3')
#pygame.mixer.music.play(-1)

while not  doExit: #game loop
    
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True
            
#game logic will go here---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   #paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        p1x-=8
    if keys[pygame.K_d]:
        p1x+=8
        
        
        #ball
    bx += bVx
    by += bVy
        
    #ball hits left or right wall
    if bx + 20 > 700:
            bVx *= -1
            
    if by + 20 < 0:
            bVy *= -1
            #increase p1 score here
            
    #ball hits right paddle
    if bx < p1x + 100 and by + 20 > p1y and by < p1y + 20:
                bVx *= -1
                bVy *= -1  
    
    #print(p1x, p1y, p2x, p2y)
        
    #increase score when you hit the left wall
  
     #ball collision with brick
    if b1.collide(bx, by):
        bVy *= -1
    elif b2.collide(bx, by):
        bVy *= -1
    elif b3.collide(bx, by):
        bVy *= -1
    elif b4.collide(bx, by):
        bVy *= -1
    elif b5.collide(bx, by):
        bVy *= -1
    elif b6.collide(bx, by):
        bVy *= -1
    elif b7.collide(bx, by):
        bVy *= -1
    elif b8.collide(bx, by):
        bVy *= -1
    elif b9.collide(bx, by):
        bVy *= -1
    elif b10.collide(bx, by):
        bVy *= -1
    
#render section will go here----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    screen.fill((0,0,0,))
    
    #brick
    b1.draw()
    b2.draw()
    b3.draw()
    b4.draw()
    b5.draw()
    b6.draw()
    b7.draw()
    b8.draw()
    b9.draw()
    b10.draw()
        
        

    #paddle
    pygame.draw.rect(screen, (255, 255, 255), (p1x, p1y, 100, 20), 1)
    
    
    pygame.draw.circle(screen, (255, 255, 255),  (bx, by), 10)
    
    pygame.display.flip()
        
    font = pygame.font.Font(None, 74)
    text = font.render(str(p1Score), 1, (255, 255, 255))
    screen.blit(text, (250,10))
    text = font.render(str(p2Score), 1, (255, 255, 255))
    screen.blit(text, (420,10))
            
#end of game loop      
pygame.quit()

