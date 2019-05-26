"""
@author: Alexandre Azevedo <alexandre.a512@gmail.com>
26/05/19
"""

import pandas as pd
import numpy as np

print('\n - Lendo o arquivo com o dataset sobre diabetes')
data = pd.read_csv('diabetes_dataset.csv')

print(' - Criando X e y para o algoritmo de aprendizagem a partir do arquivo diabetes_dataset')
# Caso queira modificar as colunas consideradas basta algera o array a seguir.
feature_cols = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
                'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']
X = data[feature_cols]
print(np.isnan(X))
clean = X.dropna(axis='rows')

clean.to_csv('out.csv', encoding='utf-8', index=False)

