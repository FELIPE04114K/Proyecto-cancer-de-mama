import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer

#Lectura
ruta = "https://docs.google.com/spreadsheets/d/1mYcXGzyLTId_Mwv-NWLg3xj2CxCUT3Jt/export?format=csv"
data= pd.read_csv(ruta)

try:
    data = pd.read_csv(ruta)
    print("Dimensiones del dataset:", data.shape)
    print(data.head())
except Exception as e:
    print("Error al cargar los datos:", e)

# Información general
print("\nInformación del dataset:")
data.info()

# Mostrar nombres de las columnas
print("\nNombres de las columnas:", data.columns)

# Comprobación de valores nulos
print("\nValores nulos por columna:")
print(data.isnull().sum())

# Limpieza de datos: eliminar filas con valores nulos
data_clean = data.dropna()

# Verificación del nombre de la columna "glucosa"
columna_glucosa = "glucosa"  # Cambia si el nombre real es diferente
if columna_glucosa in data_clean.columns:
    # **1. Histograma de Glucosa**
    plt.figure(figsize=(10, 6))
    sns.histplot(data_clean[columna_glucosa], kde=True, bins=30, color="blue")
    plt.title("Distribución de la Glucosa en Pacientes con Cáncer de Mama")
    plt.xlabel("Nivel de Glucosa")
    plt.ylabel("Frecuencia")
    plt.show()

    # **2. Boxplot de Glucosa (para ver valores atípicos)**
    plt.figure(figsize=(8, 4))
    sns.boxplot(x=data_clean[columna_glucosa], color="red")
    plt.title("Boxplot de Niveles de Glucosa")
    plt.xlabel("Nivel de Glucosa")
    plt.show()

else:
    print(f"La columna '{columna_glucosa}' no se encuentra en el dataset.")

# **3. Matriz de correlación (para variables numéricas)**
plt.figure(figsize=(10, 6))
sns.heatmap(data_clean.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Matriz de Correlación entre Variables")
plt.show()

