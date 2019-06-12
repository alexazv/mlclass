# -*- coding: utf-8 -*-

import random
import requests
import numpy as np


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

        #print("phi: {0}".format(self.phi))
        #print("theta: {0}".format(self.theta))

        url = "http://localhost:8080/antenna/simulate?phi1={0}&theta1={1}&phi2={2}&theta2={3}&phi3={4}&theta3={5}"\
            .format(self.phi[0], self.theta[0], self.phi[1], self.theta[1], self.phi[2], self.theta[2])

        # Enviando requisição e salvando o objeto resposta
        r = requests.get(url=url)
        # Extraindo e imprimindo o texto da resposta
        return float(r.text.split('\n', 1)[0])

    def neighbours(self, step):
        neighbours = []

        for change in [[step, 0, 0], [0, step, 0], [0, 0, step]]:
            neighbours.append(Antenna(randomize=False, phi=np.add(self.phi, change), theta=self.theta))
            neighbours.append(Antenna(randomize=False, phi=np.add(self.phi, np.multiply(change, -1)), theta=self.theta))
            neighbours.append(Antenna(randomize=False, phi=self.phi, theta=np.add(self.theta, change)))
            neighbours.append(Antenna(randomize=False, phi=self.phi, theta=np.add(self.theta, np.multiply(change, -1))))
        return neighbours


model = Antenna(randomize=True)
response = model.function()
print(response)
