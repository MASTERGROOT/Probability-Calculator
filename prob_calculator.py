import copy
import random

class Hat:
    def __init__(self, **color):
        self.color = color
        self.contents = [key for key, value in self.color.items() for num in range(value)]

    
    def draw(self, num_balls):
        if num_balls > len(self.contents):
            return self.contents
        draw_balls = []
        for num in range(num_balls):
            rand_idx = random.randrange(len(self.contents))
            draw_balls.append(self.contents.pop(rand_idx))
        return draw_balls
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_succes = 0
    for num in range(num_experiments):
        copy_contents = copy.copy(hat.contents)
        draw_balls = hat.draw(num_balls_drawn)
        succes = True
        for ball in expected_balls:
            if draw_balls.count(ball) < expected_balls[ball]:
                succes = False
        if succes:
            num_succes += 1
        hat.contents = copy_contents
    return num_succes/num_experiments

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,expected_balls={"red":2,"green":1},num_balls_drawn=5,num_experiments=2000)

print(probability)