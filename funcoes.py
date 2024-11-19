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
    

def media(x):
    return round(sum(x) / len(x), 2)

def mediaPond(pontoMedio, frequencia):
    ptMedioXfrequencia = []

    for i in range(len(pontoMedio)):
        ptMedioXfrequencia.append(pontoMedio[i] * frequencia[i])
    
    return sum(ptMedioXfrequencia) / sum(frequencia)

def moda(pontoMedio, frequencia):
    return pontoMedio[frequencia.index(max(frequencia))]

def mediana(intervalos, frequencia, frequenciaAcumulada):
    freqMediana = max(frequencia)
    indexMediana = frequencia.index(freqMediana)
    a, b = intervalos[indexMediana]
    limiteInferior = a
    amplitudeClasse = b - a
    elementoMediano = sum(frequencia) / 2
    freqAnterior = frequenciaAcumulada[(frequencia.index(freqMediana)) - 1]

    return limiteInferior + amplitudeClasse * ((elementoMediano - freqAnterior) / freqMediana)