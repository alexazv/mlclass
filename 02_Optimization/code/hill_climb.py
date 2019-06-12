from models import Antenna
from copy import deepcopy
import time
import csv


def hill_climb(antenna0, stride, max_steps, max_unchanged):

    antenna = deepcopy(antenna0)
    old_function = antenna.function()

    results = [(antenna.phi, antenna.theta, old_function)]

    unchanged = 0

    for step in range(max_steps):
        print(max_steps)
        neighbours = antenna.neighbours(stride)

        print("Step {0} of {1}: {2}".format(step, max_steps, old_function))

        for neighbour in neighbours:
            function = neighbour.function()
            if function > old_function:
                antenna = neighbour
                old_function = function
                unchanged = 0
        results.append((antenna.phi, antenna.theta, old_function))
        unchanged += 1
        if unchanged >= max_unchanged:
            break

    with open("hill_climb_{0}.csv".format(time.time()), mode='w') as csv_file:
        fieldnames = ['phi1', 'phi2', 'phi3', 'theta1', 'theta2', 'theta3', 'result']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        print('Writing file:')
        for result in results:
            writer.writerow({'phi1': result[0][0], 'phi2': result[0][1], 'phi3': result[0][2],
                             'theta1': result[1][0], 'theta2': result[1][1], 'theta3': result[1][2],
                             'result': result[2]})


hill_climb(Antenna(randomize=True), stride=2, max_steps=200, max_unchanged=10)
