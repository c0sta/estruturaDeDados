from random import shuffle
import random
import time

# Gera lista de acordo com o tamanho passado


def geraLista(n):
    lista = list(range(n))
    random.shuffle(lista)
    return lista

# Algoritmo de Seleção


def seleção(lista):
    vet = []
    global contSelec
    contSelec = 0
    while lista:
        menor = min(lista)
        vet.append(menor)
        lista.remove(menor)
        contSelec += 1
    return vet


# Algoritmo de Inserção
def inserção(v):
    global contInsert
    contInsert = 0
    # print(len(v))
    for j in range(1, len(v)):
        x = v[j]
        i = j - 1
        while i >= 0 and v[i] > x:
            v[i + 1] = v[i]
            i = i - 1
        v[i + 1] = x
        contInsert += 1
    return v


# Algoritmo MergeSort


def merge(esquerda, direita):
    vet = []
    i, j = 0, 0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            vet.append(esquerda[i])
            i += 1
        else:
            vet.append(direita[j])
            j += 1
    vet += esquerda[i:]
    vet += direita[j:]
    return vet


def mergesort(v):
    global contMerge
    contMerge = 0
    if len(v) <= 1:
        return v
    else:
        m = len(v) // 2
        e = mergesort(v[:m])
        d = mergesort(v[m:])
        contMerge += 1
        return merge(e, d)

# Algoritmo quicksort


def quick(lista):
    global contQuick
    contQuick = 0
    if len(lista) <= 1:
        return lista
    inicio = lista[0]
    while(contQuick < len(lista)):
        # iguais = [x for x in lista if x == inicio]
        contQuick += 1
        iguais = []
        for x in lista:
            if x == inicio:
                iguais.append(x)
            return x
        # menores = [x for x in lista if x < inicio]
        menores = []
        for x in lista:
            if x < inicio:
                menores.append(x)
            return x
        # maiores = [x for x in lista if x > inicio]
        maiores = []
        for x in lista:
            if x > inicio:
                maiores.append(x)
            return x
    return quick(menores) + iguais + quick(maiores)

# Cronometra tempo de execução da função nativa .sort()


def cronometraNative(lista):
    inicio = time.time()
    lista.sort()
    fim = time.time()
    global tempoNative
    tempoNative = fim - inicio

# Cronometra o tempo de execução da função de seleção


def cronometraSeleção(lista):
    lista = lista.copy()
    inicio = time.time()
    seleção(lista)
    fim = time.time()
    global tempoSeleção
    tempoSeleção = fim-inicio


def cronometraInserção(lista):
    inicio = time.time()
    inserção(lista)
    fim = time.time()
    global tempoInserção
    tempoInserção = fim - inicio

# Cronometra o tempos de execução da função Merge


def cronometraMerge(lista):
    lista = lista.copy()
    inicio = time.time()
    mergesort(lista)
    fim = time.time()
    global tempoMerge
    tempoMerge = fim-inicio

# Cronometra o tempo de execução da função Quick


def cronometraQuick(list):
    lista = list.copy()
    inicio = time.time()
    quick(lista)
    fim = time.time()
    global tempoQuick
    tempoQuick = fim-inicio


size = 5000
i = 0
cronometro = 0
print("----------------------------------------------------------------------------------------------------------------------|")
print(
    "|                                            [EP1] - Vale a pena ordenar?                                               |")
print('| Algoritmo escolhido: Todos                                             Duração dos testes 30.00                     |')
print('| Alunos: Gabriel Costa, Raphael  Ribeira De Paula e William Barreto                                                   |')
print("|---------------------------------------------------------------------------------------------------------------------|")

print("|---------------------------Tempo de Ordenação----------------------|--------------Numero de Buscas-------------------|")
print('|-------------------------------------------------------------------|-------------------------------------------------|')
print("|   n     |  Inserção   Mergesort   Quicksort   Selection   Native  |   Inserção   Mergesort   Quicksort   Selection |")
inicio = time.time()
while cronometro < 30:
    lista = geraLista(size)
    cronometraSeleção(lista)
    cronometraMerge(lista)
    cronometraQuick(lista)
    cronometraNative(lista)
    cronometraInserção(lista)

    i = (tempoMerge+tempoQuick+tempoSeleção+tempoInserção)
    print("|   %.0f" % size, " |", "   %.2f" % tempoInserção, "       %.2f" % tempoMerge,
          "        %.2f" % tempoQuick, "       %.2f" % tempoSeleção, "   %.3f" % tempoNative, " |      %d" % contInsert,  "       %d" % contMerge,  "          %d" % contQuick,  "        %d       |" % contSelec)

    size += 5000
    cronometro = time.time() - inicio
