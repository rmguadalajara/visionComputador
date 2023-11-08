import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
import datetime
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import make_column_transformer, make_column_selector
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GroupShuffleSplit
from tensorflow.keras import callbacks
from tensorflow.keras.callbacks import EarlyStopping
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Carga de datos
logging.info('Loading data...')
visits = pd.read_csv('/content/drive/MyDrive/deep_learning/data/visits/entrenamiento1.csv')
visits_features = visits.copy()

# Conversión de fechas a formato numérico
logging.info('Converting dates to numerical format...')
visits_features['FECHA_ENTRADA_REV'] = pd.to_datetime(visits_features['FECHA_ENTRADA_REV']).astype(int) / 10**9
visits_features['FECHA_SALIDA_REV'] = pd.to_datetime(visits_features['FECHA_SALIDA_REV']).astype(int) / 10**9

# Separación de características y objetivo
logging.info('Separating features and target...')
visits_objective = visits_features.pop('FECHA_SALIDA_REV')

# Codificación de características categóricas
logging.info('Encoding categorical features...')
visits_features_transf = pd.get_dummies(visits_features, columns=['ID_ACCION'])

# Normalización de características numéricas
logging.info('Normalizing numerical features...')
scaler = StandardScaler()
visits_features_transf_fit = scaler.fit_transform(visits_features_transf)

# Definición del modelo
logging.info('Defining model...')
input_shape = [170]
model = tf.keras.Sequential([
    layers.Dense(512, input_shape = input_shape),
    layers.Dense(512, activation='relu'),
    layers.Dense(512, activation='relu'),
    layers.Dense(512, activation='relu'),
    layers.Dense(1)
])

# Compilación del modelo
logging.info('Compiling model...')
model.compile(optimizer='adam', loss='mae')

# Entrenamiento del modelo
logging.info('Training model...')
out = model.fit(visits_features_transf_fit, visits_objective, batch_size=256, epochs=100)

# Análisis del SGD: Gráfica de pérdidas
logging.info('Plotting loss graph...')
history_df = pd.DataFrame(out.history)
history_df.loc[5:, ['loss']].plot();

# Predicciones
logging.info('Making predictions...')
predictions = model.predict(visits_features_transf)
for i in range(len(predictions)):
        a = predictions[i][0]
        b = visits_features_transf.iloc[i]

        difference = a - b
        difference_in_minutes = difference.total_seconds() / 60
        logging.info(f"Prediction: {a}, Actual: {b}, Difference: {difference_in_minutes} minutos")
