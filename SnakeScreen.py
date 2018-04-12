from UI.Base.ScreenBase import *
from Snake.Snake import *
from Snake.Enums import *

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
        
    def Show(self):   
        screen = self.display
        field = PlayField()
        group = Snake()
        group.ConstructSnake()
        feed = Food()
        block = feed.GetNewBlock()
        groupFood = pygame.sprite.Group()
        groupFood.add(block)

        print(block.rect.center)

        UPDATE = pygame.USEREVENT + 1
        pygame.time.set_timer(UPDATE,100)
        textsurface = Font.MonoSpace(15).render(str(self.highscore),False,Color.Black)


        while not self.decision:
            self.CheckEvents()
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_UP and not group.Direction is DirectionEnum.Down:
                        group.Direction = DirectionEnum.Up
                    if event.key == pygame.K_DOWN and not group.Direction is DirectionEnum.Up:
                        group.Direction = DirectionEnum.Down
                    if event.key == pygame.K_LEFT and not group.Direction is DirectionEnum.Forward:
                        group.Direction = DirectionEnum.Backward
                    if event.key == pygame.K_RIGHT and not group.Direction is DirectionEnum.Backward:
                        group.Direction = DirectionEnum.Forward
                if event.type==UPDATE:
                    game_over = not(pygame.sprite.collide_rect(field,group.sprites()[0]))
                    if game_over:
                        self.decision = True
                        self.Quit(False)
                    else:
                        screen.fill(Color.White)
                        screen.blit(textsurface,(620,20))
                        group.Move()
                        group.draw(screen)
                        groupFood.draw(screen)

                        if pygame.sprite.collide_rect(group.sprites()[0],groupFood.sprites()[0]):
                            group.EatFood(groupFood.sprites()[0])
                            block = feed.GetNewBlock()
                            groupFood.empty()
                            groupFood.add(block)
                            self.highscore+=1
                            textsurface = Font.MonoSpace(15).render(str(self.highscore),False,Color.Black)