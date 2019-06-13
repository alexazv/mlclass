from models import Antenna, load_obj, save_obj, results, max_val_key
from copy import deepcopy
import time
import csv
import numpy as np
import random


def sim_ann(antenna0, stride, max_steps, max_unchanged):

    antenna = deepcopy(antenna0)
    old_function = antenna.function()

    unchanged = 0
    chance = 0.9

    # saved_results = [(antenna.phi, antenna.theta, old_function, chance)]

    for step in range(max_steps):

        print("Step {0} of {1}: {2}, chance: {3}".format(step, max_steps, old_function, chance))
        neighbours = antenna.neighbours(stride)
        for neighbour in neighbours:
            function = neighbour.function()
            if (function > old_function) | (random.random() < chance):
                antenna = neighbour
                if old_function != function:
                    old_function = function
                    unchanged = 0

        if step%5 == 0:
            save_obj()

        # results.append((antenna.phi, antenna.theta, old_function, chance))
        chance = chance * (0.95 ** ((step/2)+1))
        unchanged += 1
        if unchanged >= max_unchanged:
            save_obj()
            break
    """
    with open("simm_ann_{0}.csv".format(time.time()), mode='w') as csv_file:
        fieldnames = ['phi1', 'phi2', 'phi3', 'theta1', 'theta2', 'theta3', 'result', 'temperature']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        print('Writing file:')
        for result in results:
            writer.writerow({'phi1': result[0][0], 'phi2': result[0][1], 'phi3': result[0][2],
                             'theta1': result[1][0], 'theta2': result[1][1], 'theta3': result[1][2],
                             'result': result[2], 'temperature': results[3]})
    """

    save_obj()


load_obj()
"""
key = max_val_key()
print(key)
sim_ann(Antenna(randomize=False, phi=[key[0], key[1], key[2]], theta=[key[3], key[4], key[5]]), stride=5, max_steps=200, max_unchanged=5)
"""
sim_ann(Antenna(randomize=True), stride=5, max_steps=1000, max_unchanged=5)
