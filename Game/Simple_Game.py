import pygame
import random
import json

score = []
window_size = [250, 300]
window_size = pygame.display.set_mode(window_size)
background = pygame.image.load('background.png').convert()
ally = pygame.image.load('ally.png').convert()
enemy = pygame.image.load('enemy.png').convert()
pygame.init()

def enemy_position_f(p):
    
    if enemy_position_y[p] > 300:
        enemy_position_y[p] = random_()
    enemy_position_y[p] = enemy_position_y[p] + 0.5


def hit(y, v):
    enemy_position_y[y] = random_()
    v = v - 1000
    return enemy_position_y[y], v

def show_(v):
    font = pygame.font.SysFont('Comic Sans MS', 15)
    
    if c == True:
        font = pygame.font.SysFont('Comic Sans MS', 20)
        initial_text = 'Press SPACE to start.'
        start_text = font.render(initial_text, True, (255, 255, 255))
        window_size.blit(start_text, [10, 10])
        font = pygame.font.SysFont('Comic Sans MS', 15)
        with open('score.json', 'r') as f_:
            d = json.load(f_)
        values = list(d.values())
        record = f'The biggest score is: {max(values)}'
        record_text = font.render(record, True, (0, 255, 0))
        window_size.blit(record_text, [40, 100])
        
    else:

        if v >= 0:
            score_text = 'Score: ' + str(score_v)
            image_text = font.render(score_text, True, (0, 255, 0))
            window_size.blit(image_text, [10, 10])

        elif v < 0:
            score_text = 'GAME OVER!'
            image_text = font.render(score_text, True, (255, 0, 0))
            window_size.blit(image_text, [10, 10])

def random_():
    return -1*random.randint(100, 500)
            
life = True
ally_x = 99.5
enemy_position_y = [random_(), random_(), random_()]
score_v = 0
c = True
l = 0

while life:
    pygame.event.get()
    button = pygame.key.get_pressed()
    
    if button[pygame.K_ESCAPE]:
        pygame.quit()
        break
    
    elif button[pygame.K_RIGHT] and ally_x <= 199:
        ally_x = ally_x + 1

    elif button[pygame.K_LEFT] and ally_x >= 0:
        ally_x = ally_x - 1
    window_size.blit(background, [0,0])

    if c == True:
        show_(score_v)
        pygame.display.update()
        start = pygame.key.get_pressed()
        if start[pygame.K_SPACE]:
            c = False
    else:
        score_v = score_v + 1
        score.append(score_v)
        enemy_position_f(0)
        enemy_position_f(1)
        enemy_position_f(2)
        window_size.blit(ally, [ally_x,252])
        window_size.blit(enemy, [0,enemy_position_y[0]])
        window_size.blit(enemy, [100,enemy_position_y[1]])
        window_size.blit(enemy, [200,enemy_position_y[2]])

        if (enemy_position_y[0] >= 204) and (ally_x <= 51):
            enemy_position_y[0] = hit(0, score_v)[0]
            score_v = hit(0, score_v)[1]

        elif (enemy_position_y[1] >= 204) and (ally_x > 51 and ally_x <= 148):
            enemy_position_y[1] = hit(1, score_v)[0]
            score_v = hit(1, score_v)[1]

        elif (enemy_position_y[2] >= 204) and (ally_x > 148):
            enemy_position_y[2] = hit(2, score_v)[0]
            score_v = hit(2, score_v)[1]
        show_(score_v)
        pygame.display.update()

        if score_v < 0:
            pygame.time.wait(1000)
            pygame.quit()
            break

max_score = max(score)

with open('score.json', 'r') as f_:
    d = json.load(f_)

rank = [1,2,3,4,5,6,7,8,9,10]

for i in rank:

    if i <= len(list(d.keys())):
        pass

    else:
        user = i
        break

user_score = {user : max_score}
d.update(user_score)

with open('score.json', 'w') as f_:
    json.dump(d, f_)
