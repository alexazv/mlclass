"""
@author: Alexandre Azevedo <alexandre.a512@gmail.com>
26/05/19
"""

import pandas as pd
import numpy as np
from array import array

def average(value, row, reference):
    #print(reference)
    #print(row)

    age_gap = 5
    dpf_gap = 0.1
    preg_min = 0
    preg_max = 0

    if row["Pregnancies"] >= 1:
        preg_min = 0
        preg_max = 1
    elif (row["Pregnancies"] > 1) & (row["Pregnancies"] <= 3):
        preg_min = 1
        preg_max = 1
    elif row["Pregnancies"] > 3:
        preg_min = 3
        preg_max = 3


    filtered_reference = reference[(reference["Age"] <= (row["Age"] + age_gap)) & (reference["Age"] >= (row["Age"] - age_gap)) &
                                   (reference["Pregnancies"] <= (row["Pregnancies"] + preg_max)) & (reference["Pregnancies"] >= (row["Pregnancies"] - preg_min)) &
                                   (reference["DiabetesPedigreeFunction"] <= (row["DiabetesPedigreeFunction"] + dpf_gap)) &
                                   (reference["DiabetesPedigreeFunction"] >= (row["DiabetesPedigreeFunction"] - dpf_gap))]
    return filtered_reference[value].mean()

print('\n - Lendo o arquivo com o dataset sobre diabetes')
data = pd.read_csv('diabetes_dataset.csv')

print(' - Criando X e y para o algoritmo de aprendizagem a partir do arquivo diabetes_dataset')
# Caso queira modificar as colunas consideradas basta algera o array a seguir.
feature_cols = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
                'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']
X = data[feature_cols]

print("calculating:")

for column in X.columns:
    clean = X.dropna(subset=[column])
    null_items = X[X[column].isnull()].index.tolist()

    for index, item in enumerate(null_items):
        print("in column " + column + ", calculating item " + str(index) + " of " + str(len(null_items)))
        row = X.iloc[item, :]
        X[column][item] = average(column, row, clean)

clean = X.dropna(axis='rows')
clean.to_csv('out3.csv', encoding='utf-8', index=False)

