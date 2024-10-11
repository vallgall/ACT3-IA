import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Cargar el dataset
df = pd.read_csv('transporte_masivo_ampliado.csv')

# Convertir variables categóricas a variables dummy
df = pd.get_dummies(df, columns=['dia_semana', 'estacion'], drop_first=True)

# Definir variables independientes y dependiente
X = df.drop(['fecha', 'hora', 'numero_pasajeros'], axis=1)
y = df['numero_pasajeros']

# Dividir el dataset en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo de árbol de decisión
modelo = DecisionTreeRegressor(max_depth=5, random_state=42)
modelo.fit(X_train, y_train)

# Realizar predicciones
y_pred = modelo.predict(X_test)

# Evaluación del modelo
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Error Cuadrático Medio (MSE): {mse}")
print(f"Coeficiente de Determinación (R²): {r2}")

import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

# Visualización del árbol de decisión
plt.figure(figsize=(20,10))
plot_tree(modelo, feature_names=X.columns, filled=True, rounded=True)
plt.title("Árbol de Decisión para Predicción de Pasajeros")
plt.show()

# Importancia de las características
importancia = pd.Series(modelo.feature_importances_, index=X.columns).sort_values(ascending=True)

plt.figure(figsize=(10,8))
importancia.plot(kind='barh')
plt.title('Importancia de las Características')
plt.xlabel('Importancia')
plt.ylabel('Características')
plt.show()
