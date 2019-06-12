# -*- coding: utf-8 -*-

import random
import requests
import numpy as np
import os

results = {}


def save_obj():
    print("saving results")
    np.savez_compressed('results.npz', results)


def load_obj():
    if os.path.isfile('./file.txt'):
        np.load('results.npz', results)
    print("Found {0} results".format(len(results)))

class Antenna:

    phi = []
    theta = []

    lower = 0
    higher = 360

    def __init__(self, randomize, phi=None, theta=None):

        if randomize:
            self.phi = [random.randint(self.lower, self.higher), random.randint(self.lower, self.higher), random.randint(self.lower, self.higher)]
            self.theta = [random.randint(self.lower, self.higher), random.randint(self.lower, self.higher), random.randint(self.lower, self.higher)]
        else:
            self.phi = np.clip(phi, a_min=self.lower, a_max=self.higher)
            self.theta = np.clip(theta, a_min=self.lower, a_max=self.higher)

    def function(self):

        if (self.phi[0], self.phi[1], self.phi[2], self.theta[0], self.theta[1], self.theta[2]) in results:
            print('found saved results')
            return results[(self.phi[0], self.phi[1], self.phi[2], self.theta[0], self.theta[1], self.theta[2])]

        url = "https://aydanomachado.com/mlclass/02_Optimization.php" \
              "?dev_key=Alexandre%20Azevedo&phi1={0}& phi2={1}&phi3={2}&theta1={3}&theta2={4}&theta3={5}"\
            .format(self.phi[0], self.phi[1], self.phi[2], self.theta[0], self.theta[1], self.theta[2])

        # Enviando requisição e salvando o objeto resposta
        r = requests.get(url=url)
        # Extraindo e imprimindo o texto da resposta
        data = float(r.json()['gain'])
        results[(self.phi[0], self.phi[1], self.phi[2], self.theta[0], self.theta[1], self.theta[2])] = data
        return data

    def neighbours(self, step):
        neighbours = []

        for change in [[step, 0, 0], [0, step, 0], [0, 0, step],
                       [step, step, 0], [step, 0, step], [0, step, step], [step, step, step]]:
            neighbours.append(Antenna(randomize=False, phi=np.add(self.phi, change), theta=self.theta))
            neighbours.append(Antenna(randomize=False, phi=np.add(self.phi, np.multiply(change, -1)), theta=self.theta))
            neighbours.append(Antenna(randomize=False, phi=self.phi, theta=np.add(self.theta, change)))
            neighbours.append(Antenna(randomize=False, phi=self.phi, theta=np.add(self.theta, np.multiply(change, -1))))
        return neighbours
