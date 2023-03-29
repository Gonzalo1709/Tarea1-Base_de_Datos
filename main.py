import pandas as pd

# Fue necesario agregar el argumento "sep" 
# ya que el documento usaba ";" como separador
filename = 'Porticos.csv'
df = pd.read_csv(filename, sep=';')

# Pregunta 1:
print("Pregunta 1: ", end="")
print(df['CATEGORIA'].value_counts().idxmax())

# Pregunta 2:
print("Pregunta 2: ")

fechas = df['FECHA'].tolist()
categoria = df['CATEGORIA'].tolist()
fechas_formateadas = []

for fecha_a_formatear in fechas:
    fecha = fecha_a_formatear.split("/")[1]
    fechas_formateadas.append(fecha)


contador = {}

for indice, categoria_a_checkear in enumerate(categoria):
    if categoria_a_checkear == "N1":
        if fechas_formateadas[indice] in contador:
            contador[fechas_formateadas[indice]] += 1
        else:
            contador[fechas_formateadas[indice]] = 1


print("La cantidad de autos con categoría N1 en los meses es: ", end="") 
print(contador)

respuesta = max(contador, key=contador.get)
print("El mes con más autos con categoría N1 es: ", end="")
print(respuesta)

# Pregunta 3:
print("Pregunta 3: ")
print("La placa con más autos es: ", end="")
# No sé por qué la placa salía como un float, por ello el int().
print(int(df['PLACA'].value_counts().idxmax()))
print("La cantidad de veces que se repite es: ", end="")
print(df['PLACA'].value_counts().max())
print("La placa con la segunda mayor cantidad de autos es: ", end="")
print(int(df['PLACA'].value_counts().index[1]))
print("La cantidad de veces que se repite es: ", end="")
print(df['PLACA'].value_counts()[int(df['PLACA'].value_counts().index[1])])

# Pregunta 4:
print("Pregunta 4: ")
contador = {}
for indice, alerta in enumerate(df['ALERTA']):
    if alerta == 2111:
        if df["CATEGORIA"][indice] == "N3":
            if fechas_formateadas[indice] in contador:
                contador[fechas_formateadas[indice]] += 1
            else:
                contador[fechas_formateadas[indice]] = 1

print("La cantidad de autos con categoría N3 cuya alerta es 2111 en los meses es: ", end="")
print(contador)

print("El mes con más autos con categoría N3 cuya alerta es 2111 es: ", end="")
print(max(contador, key=contador.get))

# Pregunta 5:
print("Pregunta 5: ")
contador = {}
contador2 = {}
for indice, alerta in enumerate(df['ALERTA']):
    if alerta != 0:
        if alerta in contador2:
            contador2[alerta] += 1
        else:
            contador2[alerta] = 1

        if fechas_formateadas[indice] in contador:
            contador[fechas_formateadas[indice]] += 1
        else:
            contador[fechas_formateadas[indice]] = 1
        
print("La cantidad de alertas en los meses es: ", end="")
print(contador)

print("El mes con más alertas es: ", end="")
print(max(contador, key=contador.get))

print("La cantidad de alertas por tipo es: ", end="")
print(contador2)

print("La alerta con más ocurrencias es: ", end="")
print(max(contador2, key=contador2.get))