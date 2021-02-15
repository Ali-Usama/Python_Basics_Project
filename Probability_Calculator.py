import random, copy


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
    # expected_balls_list = [balls for balls in expected_balls.keys() for i in range(expected_balls[balls])]
    print(expected_balls)

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










hat = Hat(black=6, red=4, green=3)
#print(hat.draw(5))
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print(probability)
'''
#for key in dict_1.keys():
 #   for i in range(dict_1[key]):
  #      contents.append(key)

dict_1 = {"red": 2, "blue": 1}
contents = [key for key in dict_1.keys() for i in range(dict_1[key])]
print(contents)


# drawn_list = [item for item in random.sample((contents), 2)]
drawn_list = random.choices((contents), k=2)
print(drawn_list)
'''