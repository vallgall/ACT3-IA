import pandas as pd
import numpy as np

# --------------- Configuración Inicial ---------------

# Definir parámetros
fecha_inicio = '2024-04-01'
numero_dias = 30  # Número de días para generar datos
fechas = pd.date_range(start=fecha_inicio, periods=numero_dias, freq='D')

horas = [
    '06:00', '07:00', '08:00', '09:00', '10:00',
    '11:00', '12:00', '13:00', '14:00', '15:00',
    '16:00', '17:00', '18:00', '19:00', '20:00'
]

dias_map = {
    'Monday': 'Lunes',
    'Tuesday': 'Martes',
    'Wednesday': 'Miercoles',
    'Thursday': 'Jueves',
    'Friday': 'Viernes',
    'Saturday': 'Sabado',
    'Sunday': 'Domingo'
}

estaciones = ['Estacion A', 'Estacion B', 'Estacion C', 'Estacion D', 'Estacion E']

# Definir las probabilidades corregidas para 'lluvia'
# Opciones únicas para evitar repeticiones innecesarias
opciones_lluvia = [0, 5, 10, 15, 20]
prob_lluvia = [0.7, 0.1, 0.05, 0.025, 0.015]

# Verificar que las probabilidades sumen 1
suma_prob_lluvia = sum(prob_lluvia)
if not np.isclose(suma_prob_lluvia, 1.0):
    # Normalizar las probabilidades si no suman exactamente 1
    prob_lluvia = [p / suma_prob_lluvia for p in prob_lluvia]
    print("Probabilidades normalizadas para 'lluvia':", prob_lluvia)
else:
    print("Probabilidades para 'lluvia' suman 1.0.")

# Definir probabilidades para 'evento_especial'
prob_evento_especial = [0.85, 0.15]  # [No, Sí]

# --------------- Generación de Datos ---------------

# Lista para almacenar los registros
data = []

# Establecer semilla para reproducibilidad
np.random.seed(42)

for fecha in fechas:
    dia_semana_ingles = fecha.strftime('%A')  # Día de la semana en inglés
    dia_semana_espanol = dias_map[dia_semana_ingles]
    
    for estacion in estaciones:
        for hora in horas:
            # Determinar si es hora pico o valle
            horas_pico = ['06:00', '07:00', '08:00', '09:00', '17:00', '18:00', '19:00']
            if hora in horas_pico:
                numero_pasajeros = np.random.randint(150, 400)  # Horas pico
            else:
                numero_pasajeros = np.random.randint(50, 200)   # Horas valle
            
            # Generar temperatura entre 10 y 35 grados Celsius
            temperatura = np.random.randint(10, 35)
            
            # Generar cantidad de lluvia según las probabilidades definidas
            lluvia = np.random.choice(opciones_lluvia, p=prob_lluvia)
            
            # Determinar si hay evento especial
            evento_especial = np.random.choice([0, 1], p=prob_evento_especial)
            
            # Agregar el registro a la lista de datos
            data.append([
                fecha.strftime('%Y-%m-%d'),
                hora,
                dia_semana_espanol,
                estacion,
                numero_pasajeros,
                temperatura,
                lluvia,
                evento_especial
            ])

# --------------- Creación del DataFrame ---------------

# Crear el DataFrame con las columnas especificadas
df = pd.DataFrame(data, columns=[
    'fecha',
    'hora',
    'dia_semana',
    'estacion',
    'numero_pasajeros',
    'temperatura',
    'lluvia',
    'evento_especial'
])

# --------------- Exportación a CSV ---------------

# Guardar el DataFrame en un archivo CSV
nombre_archivo = 'transporte_masivo_ampliado.csv'
df.to_csv(nombre_archivo, index=False)

print(f"Dataset '{nombre_archivo}' generado exitosamente.")
