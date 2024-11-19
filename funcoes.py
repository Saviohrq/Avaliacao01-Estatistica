import math
import matplotlib.pyplot as plt

def dados(classes, frequencia):
    numClass = len(classes)
    fj = frequencia
    somaFreq = sum(frequencia)
    xj = []
    freqAcumulada = []
    freqAcumulada.append(fj[0])

    for i in range(numClass):
        a, b = classes[i]
        xj.append((a + b) / 2)

    for i in range(1, numClass):
        freqAcumulada.append(fj[i] + fj[i-1])

    return [numClass, fj, somaFreq, xj, freqAcumulada]
    

def mediaA(classes, frequencia):
    soma = 0

    for i in range(len(frequencia)):
        a, b = classes[i]
        pontoMedio = (a + b) / 2
        soma += pontoMedio * frequencia[i]

    return soma / sum(frequencia)
    

def mediaPond(pontoMedio, frequencia):
    ptMedioXfrequencia = []

    for i in range(len(pontoMedio)):
        ptMedioXfrequencia.append(pontoMedio[i] * frequencia[i])
    
    media = sum(ptMedioXfrequencia) / sum(frequencia)
    return media

def moda(pontoMedio, frequencia):
    return pontoMedio[frequencia.index(max(frequencia))]

def mediana(classes, frequencia, frequenciaAcumulada):
    freqMediana = max(frequencia)
    indexMediana = frequencia.index(freqMediana)
    a, b = classes[indexMediana]
    limiteInferior = a
    amplitudeClasse = b - a
    elementoMediano = sum(frequencia) / 2
    freqAnterior = frequenciaAcumulada[(frequencia.index(freqMediana)) - 1]

    return round(limiteInferior + amplitudeClasse * ((elementoMediano - freqAnterior) / freqMediana), 2)

def desvioPadrao(classes, frequencia):
    media = mediaA(classes, frequencia)
    somatorio = 0
    n = len(classes)

    for i in range(n):
        a, b = classes[i]
        xj = (a + b) / 2
        somatorio += (xj - media) ** 2

    if(n != 1):
        var = somatorio / (n - 1)
    else:
        var = 0

    return round(math.sqrt(var), 2)

def percentil(classes, frequencias, percentil):
    n = sum(frequencias)
    posicao = percentil * n / 100

    freqSoma = 0
    for i in range(len(classes)):
        freqSoma += frequencias[i]
        if freqSoma >= posicao:
            a, b = classes[i]
            limiteInferior = a
            amplitudeClasse = b - a
            freqSomaAnterior = freqSoma - frequencias[i]
            
            return round(limiteInferior + ((posicao - freqSomaAnterior) / frequencias[i]) * amplitudeClasse, 2)
        
def gerarClasses(classes):
    intervaloClass = []
    for i in classes:
        intervaloClass.append(str(i[0]) + " |- " + str(i[1]))
    return intervaloClass

def grafico(classes, frequencias):
    plt.bar(classes, frequencias)
    plt.xlabel("xj")
    plt.ylabel("fj")
    plt.title("Gráfico de frequências")
    plt.show()