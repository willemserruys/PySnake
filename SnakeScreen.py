from UI.Base.ScreenBase import *
from Snake.Snake import *
from Snake.Enums import *
from DataAccess.Controller import *

class PlayField:
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([640,480])
        self.rect = self.image.get_rect()
        
class SnakeScreen(ScreenBase):
    def __init__(self,display):
        super().__init__(display)
        self.display = display
        self.display.fill(Color.White)
        self.decision = False
        self.highscore = 0
        self.key = pygame.K_RIGHT
        
    def Show(self):   
        screen = self.display
        field = PlayField()
        group = Snake()
        group.ConstructSnake()
        feed = Food()
        block = feed.GetNewBlock(group.sprites())
        groupFood = pygame.sprite.Group()
        groupFood.add(block)

        print(block.rect.center)

        UPDATE = pygame.USEREVENT + 1
        pygame.time.set_timer(UPDATE,70)
        textsurface = Font.MonoSpace(15).render(str(self.highscore),False,Color.Black)

        ps4 = PS4Controller()
        ps4.init()
        print(ps4.joystick_present)
        if ps4.joystick_present:
            if not ps4.hat_data:
                ps4.hat_data = {}
                for i in range(ps4.controller.get_numhats()):
                    ps4.hat_data[i] = (0, 0)

        while not self.decision:
            self.CheckEvents()
            
            for event in pygame.event.get():
                if ps4.joystick_present:
                    if event.type == pygame.JOYHATMOTION:
                        ps4.hat_data[event.hat] = event.value
                        hatValues = ps4.hat_data[0]
                        if hatValues[0] == -1:
                            self.key = pygame.K_LEFT
                        elif hatValues[0] == 1:
                            self.key = pygame.K_RIGHT
                        elif hatValues[1] == -1:
                            self.key = pygame.K_DOWN
                        elif hatValues[1] == 1:
                            self.key = pygame.K_UP                       
                    
                if event.type==pygame.KEYDOWN:
                    self.key = event.key


                if event.type==UPDATE:
                    group.UpdateDirection(self.key)
                    game_over = not(pygame.sprite.collide_rect(field,group.sprites()[0])) or group.DetectCollisionWithItself()
                    if game_over:
                        self.decision = True
                        self.Quit(False)
                    else:
                        screen.fill(Color.White)
                        screen.blit(textsurface,(620,20))
                        group.Move()
                        group.draw(screen)
                        pygame.display.update()
                        groupFood.draw(screen)

                        if pygame.sprite.collide_rect(group.sprites()[0],groupFood.sprites()[0]):
                            group.EatFood(groupFood.sprites()[0])
                            block = feed.GetNewBlock(group.sprites())
                            groupFood.empty()
                            groupFood.add(block)
                            self.highscore+=1
                            textsurface = Font.MonoSpace(15).render(str(self.highscore),False,Color.Black)

