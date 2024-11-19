import funcoes as fx

rol = [61,65,43,53,55,51,58,55,59,56,52,53,62,49,68,51,50,67,62,64,53,56,48,50,61,44,64,53,54,55,48,54,57,41,54,71,57,53,46,48,55,46,57,54,48,63,49,55,52,51]

rol.sort()

valorMin = min(rol)
valorMax = max(rol)
numClasses = 6
amplitude = 5
classes = []
frequencias = [0, 0, 0, 0, 0, 0]

for i in range(numClasses):
    inf = valorMin + i * amplitude
    sup = valorMin + amplitude
    classes.append((inf, sup))

for valor in rol:
    for i, classe in enumerate(classes):
        if classe[0] <= classe[1]:
            frequencias[i] += 1
            break

dados = fx.dados(classes, frequencias)

numClass = dados[0]
fj = dados[1]
somaFreq = dados[2]
xj = dados[3]
freqAcumulada = dados[4]

print(f"\nMédia: {fx.mediaA(classes, fj)}\nModa: {fx.moda(xj, fj)}\nMediana: {fx.mediana(classes, fj, freqAcumulada)}\nDesvio Padrão: {fx.desvioPadrao(classes, fj)}\nQ1: {fx.percentil(classes, fj, 25)}\nD3: {fx.percentil(classes, fj, 30)}\nD7: {fx.percentil(classes, fj, 70)}\nP15: {fx.percentil(classes, fj, 15)}\nP90: {fx.percentil(classes, fj, 90)}\n")

fx.grafico(fx.gerarClasses(classes), fj)