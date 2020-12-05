# https://www.reddit.com/r/adventofcode/comments/3w6h3m/day_10_solutions/

from itertools import groupby

def look_and_say(input_string, num_iterations):
    for i in range(num_iterations):
        input_string = ''.join([str(len(list(g))) + str(k) for k, g in groupby(input_string)])
    return input_string

print(len(look_and_say('1113222113', 50)))