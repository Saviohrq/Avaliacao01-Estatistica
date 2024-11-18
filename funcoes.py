def media(x):
    return round(sum(x) / len(x), 2)

def mediaPond(pontoMedio, frequencia):
    ptMedioXfrequencia = []

    for i in range(len(pontoMedio)):
        ptMedioXfrequencia.append(pontoMedio[i] * frequencia[i])
    
    return sum(ptMedioXfrequencia) / sum(frequencia)

def moda(pontoMedio, frequencia):
    return pontoMedio[frequencia.index(max(frequencia))]

def mediana(media, moda):
    return (2 * media + moda) / 3 # --> mediana obtida por meio da sua relação empírica