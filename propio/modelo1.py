# Paso 1: Importar las librerías necesarias
import tensorflow as tf
from tensorflow import keras
import cx_Oracle
import numpy as np
import logging

# Configura el nivel de log a INFO
logging.basicConfig(level=logging.INFO)

# Registra un mensaje de log
logging.info("Definiendo el modelo de red neuronal...")
# Paso 2: Definir el modelo de red neuronal
model = keras.Sequential([
    keras.layers.Dense(512, activation='relu', input_shape=(4,)),
    keras.layers.Dense(512, activation='relu'),
    keras.layers.Dense(512, activation='relu'),
    keras.layers.Dense(512, activation='relu'),
    keras.layers.Dense(1)
])
logging.info("Compilando el modelo...")
# Paso 3: Compilar el modelo
model.compile(loss='mse', optimizer='adam', metrics=['mae', 'mse'])

# Paso 4: Cargar los datos desde la base de datos Oracle
# Aquí se debe reemplazar los valores de conexión a la base de datos y la query para cargar los datos
logging.info("Accediendo a la base de datos...")
dsn_tns = cx_Oracle.makedsn('cancosi.sir.renfe.es', '1541', service_name='opercosi')
conn = cx_Oracle.connect(user='APLPOSIO_MATTALLER', password='mD1PLUNk', dsn=dsn_tns)
cursor = conn.cursor()
cursor.execute("SELECT ri.cod_matricula, cod_serie, id_accion, fecha_entrada_rev FROM r_intervencion ri  WHERE ri.fecha_entrada_rev > TO_DATE('01-01-' || TO_CHAR(SYSDATE, 'YYYY'), 'DD-MM-YYYY")
data = cursor.fetchall()
cursor.close()
conn.close()

logging.info("Preparando los datos para el entrenamiento...")
# Preparar los datos para el entrenamiento del modelo
data = np.array(data)
x_train = data[:, 1:]
y_train = data[:, 0]

# Paso 5: Entrenar el modelo
logging.info("Entrenando el modelo...")
model.fit(x_train, y_train, epochs=100)
logging.info("Fin del entrenamiento.")
# Paso 6: Validar el modelo y sus predicciones contra los datos del dataset
# Aquí se debe reemplazar los valores de conexión a la base de datos y la query para cargar los datos de validación
""" cursor = conn.cursor()
cursor.execute('SELECT ri.cod_matricula, ri.cod_serie, ri.id_accion, ri.fecha_entrada_rev, ri.fecha_salida_rev FROM r_intervencion ri  WHERE ri.fecha_entrada_rev > TO_DATE('01-01-' || TO_CHAR(SYSDATE, 'YYYY'), 'DD-MM-YYYY')
data = cursor.fetchall()
cursor.close()
conn.close() """

# Preparar los datos de validación
""" data = np.array(data)
x_test = data[:, 1:]
y_test = data[:, 0] """

# Evaluar el modelo
""" loss, mae, mse = model.evaluate(x_test, y_test, verbose=2)
print("Mean Absolute Error:", mae)
print("Mean Squared Error:", mse) """

""" 
def predict(data):
    # Asegúrate de que los datos estén en el formato correcto para tu modelo
    # ...
    return model.predict(data) """