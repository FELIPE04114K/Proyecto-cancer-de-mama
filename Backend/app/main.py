import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from dotenv import load_dotenv
import os

load_dotenv()
#Lectura
ruta = os.getenv("DB_URL")
data= pd.read_csv(ruta)


# Normalizamos los nombres de las columnas
data.columns = [col.strip().lower() for col in data.columns]

# Mostrar al usuario qué variables hay
print("Columnas disponibles en los datos:")
print(data.columns)
print("\nEjemplo de los datos cargados:")
print(data.head())

# Función para mostrar gráfica circular de clasificación
def mostrar_conteo():
    conteo = data['clasificación'].value_counts()
    etiquetas = ['Con cáncer' if val == 1 else 'Sin cáncer' for val in conteo.index]
    colores = ['#ff9999', '#99ff99']

    plt.figure(figsize=(6,6))
    plt.pie(conteo, labels=etiquetas, autopct='%1.1f%%', colors=colores, startangle=140)
    plt.title('Distribución general de los diagnósticos')
    plt.show()

# Gráfica de barras comparando el promedio de una variable según el diagnóstico
def graficar_variable(variable):
    plt.figure(figsize=(8,5))
    data.groupby('clasificación')[variable].mean().plot(kind='bar', color=['#99ff99', '#ff9999'])

    plt.xticks([0,1], ['Sin cáncer', 'Con cáncer'], rotation=0)
    plt.title(f'Promedio de {variable.capitalize()} según diagnóstico')
    plt.ylabel(f'Nivel de {variable}')
    plt.xlabel("Diagnóstico")
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

# Diagnóstico personalizado mejorado
def diagnostico_individual(variable):
    while True:
        entrada = input(f"\nIngresa tu valor de {variable.capitalize()} (o escribe 'volver' para regresar al menú): ").strip().lower()

        if entrada == 'volver':
            break

        try:
            valor = float(entrada)
        except ValueError:
            print("⚠️ Por favor, ingresa un número válido.")
            continue

        media = data[variable].mean()
        std = data[variable].std()

        if valor < media - std:
            estado = 'BAJO'
            descripcion = f"Tu nivel de {variable} es más bajo de lo habitual comparado con el promedio general."
        elif valor > media + std:
            estado = 'ALTO'
            descripcion = f"Tu nivel de {variable} es más alto de lo habitual comparado con el promedio general."
        else:
            estado = 'NORMAL'
            descripcion = f"Tu nivel de {variable} está dentro del rango promedio esperado."

        # Comparación con grupo (con/sin cáncer)
        promedio_con = data[data['clasificación'] == 1][variable].mean()
        promedio_sin = data[data['clasificación'] == 0][variable].mean()
        grupo_asociado = "personas CON cáncer de mama" if abs(valor - promedio_con) < abs(valor - promedio_sin) else "personas SIN cáncer de mama"

        # Mostrar resultado
        print(f"\n👉 Tu nivel de {variable.capitalize()} es {estado}.")
        print(f"   (Tu valor: {valor} | Promedio general: {media:.2f})")
        print(f"📌 {descripcion}")
        print(f"📊 Según los datos, tu valor se parece más al grupo de {grupo_asociado}.")

        # Mostrar histograma con valor del usuario
        plt.figure(figsize=(8,5))
        sns.histplot(data[variable], kde=True, bins=25, color='skyblue')
        plt.axvline(valor, color='red', linestyle='--', linewidth=2, label='Tu valor')
        plt.title(f'Distribución de {variable.capitalize()} en la población del estudio')
        plt.xlabel(variable.capitalize())
        plt.ylabel('Número de personas')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

        print("📈 La gráfica muestra cómo se distribuye esta variable entre todas las personas del estudio.")
        print("🔴 La línea roja indica tu valor y permite ver si estás dentro o fuera del rango común.\n")

# Mostrar estadísticas generales por grupo
def mostrar_estadisticas():
    print("\nEstadísticas generales (promedios por grupo):")
    resumen = data.groupby('clasificación').mean(numeric_only=True)
    resumen.index = ['Sin cáncer', 'Con cáncer']
    print(resumen.round(2))

# Menú principal interactivo
def menu():
    while True:
        print("\n=========== MENÚ DE EVALUACIÓN MÉDICA ===========")
        print("1. Ver distribución general de diagnósticos")
        print("2. Comparar variable entre personas con/sin cáncer")
        print("3. Ingresar mi valor personal y comparar con la población")
        print("4. Ver resumen general (estadísticas)")
        print("5. Salir del sistema")
        print("==================================================")

        opcion = input("Escribe el número de la opción que deseas realizar: ").strip()

        if opcion == "1":
            mostrar_conteo()

        elif opcion == "2":
            print("\nVariables disponibles para comparar:")
            for col in data.columns:
                if col != 'clasificación':
                    print(f"🔹 {col}")
            var = input("Escribe el nombre exacto de la variable: ").strip().lower()
            if var in data.columns and var != 'clasificación':
                graficar_variable(var)
            else:
                print("⚠️ Variable no válida. Intenta de nuevo.")

        elif opcion == "3":
            print("\nVariables disponibles para evaluación personal:")
            for col in data.columns:
                if col != 'clasificación':
                    print(f"🔹 {col}")
            var = input("Escribe la variable a evaluar: ").strip().lower()
            if var in data.columns and var != 'clasificación':
                diagnostico_individual(var)
            else:
                print("⚠️ Variable no válida. Intenta de nuevo.")

        elif opcion == "4":
            mostrar_estadisticas()

        elif opcion == "5":
            print("\nGracias por usar este sistema de evaluación médica sencilla. ¡Cuídate mucho!")
            break

        else:
            print("⚠️ Opción no reconocida. Por favor elige una opción válida del menú.")

# Ejecutar menú
menu()

