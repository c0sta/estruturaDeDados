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
  while lista:
    menor = min(lista)
    vet.append(menor)
    lista.remove(menor)
  return vet

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
    if len(v) <= 1:
        return v
    else:
        m = len(v) // 2
        e = mergesort(v[:m])
        d = mergesort(v[m:])
        return merge(e, d)

#Algoritmo quicksort
def quick(lista):
   if len(lista) <= 1:
       return lista

   inicio = lista[0]
   iguais  = [x for x in lista if x == inicio]
   menores = [x for x in lista if x <  inicio]
   maiores = [x for x in lista if x >  inicio]
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

print("---------------------------------------------------------------------------------------")
print("                                         Tempo                                         ")
print("---------------------------------------------------------------------------------------")
print("   "
      "          |         Mergesort   Quicksort   Selection   Native         |            ")

size = 2000
i = 0
for i in range(11):
    lista = geraLista(size)
    cronometraSeleção(lista)
    cronometraMerge(lista)
    cronometraQuick(lista)
    cronometraNative(lista)
        
    i =(tempoMerge+tempoQuick+tempoSeleção)
    if(size < 10000):
        print("   %.0f" % size, "     |","         %.2f" % tempoMerge,"        %.2f" % tempoQuick,"        %.2f" % tempoSeleção,"     %.3f"%tempoNative,"        |")
    else:
        print("   %.0f" % size, "    |", "         %.2f" % tempoMerge, "        %.2f" % tempoQuick, "        %.2f" % tempoSeleção,"     %.3f"%tempoNative,"        |" )
    size += 2000
    
