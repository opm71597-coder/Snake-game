import pygame
import random

pygame.init()

#screen
h=600
w=400
screen=pygame.display.set_mode((h,w))
pygame.display.set_caption("snake game")
random_h=random.randint(20,400)
random_w=random.randint(20,400)
font=pygame.font.SysFont(None,55)
#color
black=(0,0,0)
red=(255,0,0)
white=(255,255,255)
blue=(0,0,255)

def text_display(text,color,x,y):
  st= font.render(text,True,color)
  screen.blit(st,[x,y])

def plot_snake(color,snk_list,siz):
  for x,y in snk_list:
   pygame.draw.rect(screen,color,[x,y,siz,siz])


def gameloop():
  lose=False
  exit=False
  snake_x=45
  snake_y=55
  size=10
  velocity_x=0
  velocity_y=0
  velocity=10
  food_x=random_w
  food_y=random_h
  snk_list=[]
  snk_l=1
  clock=pygame.time.Clock()
  fps=30
  point=0

  while not exit:

   if lose:
    screen.fill(white)
    text_display("your lose enter for restart",red,100,100)
    for event in pygame.event.get():
     if event.type == pygame.QUIT:
      exit=True
     if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RETURN:
       gameloop()

   else:
    for event in pygame.event.get():
     if event.type == pygame.QUIT:
      exit=True

     if event.type == pygame.KEYDOWN:

      if event.key == pygame.K_RIGHT:
       velocity_x=velocity
       velocity_y=0

      if event.key == pygame.K_LEFT:
       velocity_x=-velocity
       velocity_y=0

      if event.key == pygame.K_UP:
       velocity_x=0
       velocity_y=-velocity

      if event.key == pygame.K_DOWN:
       velocity_x=0
       velocity_y=velocity

    snake_x= snake_x + velocity_x
    snake_y= snake_y + velocity_y
    screen.fill(black)
    pygame.draw.rect(screen,red,[food_x,food_y,size,size])
    if abs(snake_x - food_x)<9 and abs(snake_y - food_y)<9:
     point+=10
     food_x=random.randint(20,400)
     food_y=random.randint(20,400)
     snk_l+=1

    head=[]
    head.append(snake_x)
    head.append(snake_y)
    snk_list.append(head)

    if len(snk_list)> snk_l:
     del snk_list[0]

    if snake_x<0 or snake_x>w or snake_y<0 or snake_y>h:
     lose=True

    if head in snk_list[:-1]:
     lose=True

    text_display("score:" + str(point),red,5,5)
    plot_snake(blue,snk_list,size)
   pygame.display.update()
   clock.tick(fps)

gameloop()
pygame.quit()
