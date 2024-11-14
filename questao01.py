areas = ["300 |- 400", "400 |- 500", "500 |- 600", "600 |- 700", "800 |- 900", "900 |- 1000", "1000 |- 1100", "1100 |- 1200"]
pontoMedio = [350, 450, 550, 650, 750, 850, 950, 1050, 1150]
num_lotes = [14, 46, 58, 76, 68, 62, 48, 22, 6]
numClass = len(areas)
classOrdenada = sorted(num_lotes)

def media():
    soma = 0

    for i in range(numClass):
        soma += (pontoMedio[i] * num_lotes[i])

    media = soma / sum(num_lotes)

    return media

def moda():
    ordenada = sorted(num_lotes)
    count = 0

    for i in range(numClass):
        if num_lotes[i] == ordenada[numClass]:
            return pontoMedio[i]

def rol():
    j = 0
    rol = []
    for i in range(numClass):
        while j < num_lotes[i]:
            rol.append(pontoMedio[i])
            j += 1
    return rol

def mediana():
    soma_fi = sum(num_lotes)
    rol = []
    

    if soma_fi % 2 == 0:
        mediana = [rol[soma_fi//2], rol[(soma_fi//2) + 1]]
        return mediana
    else:
        mediana = rol[(soma_fi//2) + 1]
        return mediana
        

