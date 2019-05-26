def main():
    #Algoritmo Cavaleiros
    cavaleiros_arquivo = open('cavaleiros.txt', 'r')
    cavaleiros = separaNomes(cavaleiros_arquivo)
    nome_dos_cavaleiros = []
    
    for key in cavaleiros:
        nome_dos_cavaleiros.append(key)

    encontrou = False
    print("---"*20)
    print("TÁVOLA REDONDA")
    print("---"*20)
    for arranjo in permutações(nome_dos_cavaleiros):
        if organizaMesa(arranjo, cavaleiros) == True:
            print("Rei Arthur, trago boas notícias! Encontrei a seguinte organização dos cavaleiros em torno da Távola!")
            print(arranjo)
            encontrou = True
            break
    if not encontrou:
        print("Trago más noticias Rei Arthur! Não consegui organizar os cavaleiros em torno da távola redonda")


    print("---"*20)
    print("CASANDO AS DAMAS")
    print("---"*20)
    #Algoritmo para casar as damas
    casamento_arquivo = open('casamento.txt','r')
    damas = separaNomes(casamento_arquivo)

    nome_das_damas = []
    for key in damas:
        nome_das_damas.append(key)

    casou = True
    for arranjo in enumerações(nome_das_damas):
        lista = []
        for dama in arranjo:
            lista.extend([i for i in damas[dama]])
        if( len(set(lista)) >= len(arranjo) ):
            continue

        else:
            print("Rei Arthur infelizmente não foi possível casar todas as damas!")
            casou = False
            break
    if casou:
        print("Rei Arthur! Trago boas notícias, foi possível casar todas as damas de acordo com suas preferências")
       

        
#Transforma cada linha em uma lista com os nomes separados invidualmente 
def separaNomes(arquivo):
    linhas = []
    nomes = []
    #separa as linhas em listas
    for line in arquivo:
        linha = line.split('\n')
        #Estou pegando a linha[0] pois sem especificar a primeira posição retorna com uma posição a mais e vazia
        linhas.append(linha[0])
    #separa os nomes presentes em cada linha
    for names in linhas:
        nome = names.split()
        nomes.append(nome)
    #Passa a lista com as listas de nomes para a função que irá organizar as preferencias
    return organizaPreferencias(nomes)

#Organiza as preferencias de cada um. De forma onde a chave é a pessoa e a lista as preferencias 
def organizaPreferencias(listas):
    preferencias = {}
    #para cada lista irá criar um chave com a primeira posição(nome) e add uma lista com os nomes restantes(preferencias)
    #Adicionando um False para representar que a pessoa ainda encontra-se sem um par
    for l in listas:
        preferencias.update({l[0]: l[1:]})
    return preferencias

#Verifica os cavaleiros que estão dentro da lista de preferencias dos outros cavaleiros de forma que apenas esses sentem perto
def organizaMesa(arranjo, dicionario):   
    for i in range(len(arranjo)):
        if arranjo[i-1] not in dicionario[arranjo[i]]:
            return False
    return True

     
#algoritmos do mago merlin
        
def enumerações(items):
    n = len(items)
    s = [0]*(n+1)
    k = 0
    while True:
        if s[k] < n:
            s[k+1] = s[k] + 1
            k += 1
        else:
            s[k-1] += 1
            k -= 1
        if k == 0: break
        else:
            lista = []
            for j in range(1, k+1):
                lista.append(items[s[j]-1])
            yield lista

def combinações(items, n):
    if n==0: yield []
    else:
        for i in range(len(items)):
            for cc in combinações(items[:i]+items[i+1:],n-1):
                yield [items[i]]+cc
 
def permutações(items):
    return combinações(items, len(items))

 
main()



