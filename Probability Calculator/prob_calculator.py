import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = [key for key in kwargs.keys() for i in range(kwargs[key])]
        
    def draw(self, num_ball):
        if num_ball > len(self.contents):
            return self.contents

        drawn_list = random.choices((self.contents), k=num_ball)
        for ball in drawn_list:
            try:
                self.contents.remove(ball)
            except ValueError:
                pass
        return drawn_list


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    not_count = 0
    for i in range(num_experiments):
        data = copy.deepcopy(hat)
        drawn_balls = data.draw(num_balls_drawn)
        for ball in expected_balls.keys():
            count = 0

            for x in range(len(drawn_balls)):
                if drawn_balls[x] == ball:
                    count += 1

            if count < expected_balls[ball]:
                not_count += 1

                break
        # count += sum(ball in data.draw(num_balls_drawn) for ball in expected_balls)
    print(count)
    print(not_count)

    probability = not_count/num_experiments
    return 1 - probability
