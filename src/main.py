import pandas as pd

# Lee el archivo Excel
archivo_excel = 'data.xlsx'
df = pd.read_excel(archivo_excel)

# Nombre de la tabla en la base de datos
tableName = 'DDBB_TABLE_NAME'


# Nombre de la columna que contiene los nuevos valores
columnNewValue = 'PRICE_VALUE'
columnFirst = 'NAME_FIRST_COLUMN_CONDITION'
columnSecond = 'NAME_SECOND_COLUMN_CONDITION'


# Inicializa una lista para almacenar las sentencias UPDATE
sentencias_update = []

# Itera a través de las filas del DataFrame
for index, row in df.iterrows():
    columnFirstValue = row[columnFirst]  
    columnSecondValue = row[columnSecond]
    newValue = row[columnNewValue]
    # Formatea el valor como una cadena con dos decimales
    formatted_columnFirstValue = "{:.2f}".format(columnFirstValue)


    # Genera la sentencia UPDATE y agrégala a la lista
    sentencia = f"UPDATE {tableName} SET {columnNewValue} = '{newValue}' WHERE {columnFirst}='{columnFirstValue}' AND {columnSecond}='{columnSecondValue}';"
    sentencias_update.append(sentencia)

# Guarda las sentencias en un archivo de salida
archivo_salida = 'sentencias_update.sql'
with open(archivo_salida, 'w') as file:
    for sentencia in sentencias_update:
        file.write(sentencia + '\n')

print(f"Se han generado {len(sentencias_update)} sentencias UPDATE en '{archivo_salida}'.")
