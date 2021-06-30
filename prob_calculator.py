import copy
import random

random.seed(95)


class Hat:

    def __init__(self, **balls):
        self.contents = []
        for key, value in balls.items():
            for x in range(value):
                self.contents.append(key)

    def draw(self, num):
        if num > len(self.contents):
            return self.contents
        else:
            balls_drawn = []
            for x in range(num):
                index = random.randrange(len(self.contents))
                balls_drawn.append(self.contents[index])
                self.contents.pop(index)
            return balls_drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_balls_list = []
    for key, value in expected_balls.items():
        for x in range(value):
            expected_balls_list.append(key)

    num_matches = 0
    for x in range(num_experiments):
        contents_copy = copy.copy(hat.contents)
        balls_drawn = copy.copy(hat.draw(num_balls_drawn))
        count = 0
        for ball in expected_balls_list:
            if ball in balls_drawn:
                balls_drawn.remove(ball)
                count += 1
        if count == len(expected_balls_list):
            num_matches += 1
        hat.contents = contents_copy

    probability = num_matches / num_experiments
    return probability
