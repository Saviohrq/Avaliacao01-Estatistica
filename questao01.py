import funcoes as fx

classes = [[300, 400], [400, 500], [500, 600], [600, 700], [700, 800], [800, 900], [900, 1000], [1000, 1100], [1100, 1200]]
num_lotes = [14, 46, 58, 76, 68, 62, 48, 22, 6]

dados = fx.dados(classes, num_lotes)

numClass = dados[0]
fj = dados[1]
somaFreq = dados[2]
xj = dados[3]
freqAcumulada = dados[4]


print(f"\nMédia: {fx.mediaA(classes, fj)}\nModa: {fx.moda(xj, fj)}\nMediana: {fx.mediana(classes, fj, freqAcumulada)}\nDesvio Padrão: {fx.desvioPadrao(classes, fj)}\nQ1: {fx.percentil(classes, fj, 25)}\nD3: {fx.percentil(classes, fj, 30)}\nD7: {fx.percentil(classes, fj, 70)}\nP15: {fx.percentil(classes, fj, 15)}\nP90: {fx.percentil(classes, fj, 90)}\n")

fx.grafico(fx.gerarClasses(classes), fj)
