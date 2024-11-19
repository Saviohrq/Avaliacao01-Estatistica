import funcoes as fx

classes = [[300, 400], [400, 500], [500, 600], [600, 700], [700, 800], [800, 900], [900, 1000], [1000, 1100], [1100, 1200]]
num_lotes = [14, 46, 58, 76, 68, 62, 48, 22, 6]

dados = fx.dados(classes, num_lotes)

numClass = dados[0]
fj = dados[1]
somaFreq = dados[2]
xj = dados[3]
freqAcumulada = dados[4]

print(fx.mediaPond(xj, fj))
print(fx.moda(xj, fj))
print(fx.mediana(classes, fj, fj))
