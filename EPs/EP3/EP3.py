matriz = '''010
111
000
101'''

row = matriz.split('\n')  # splits matriz


def merge(groups):
    for p in groups:
        for i in range(len(groups)):
            flag = False
            for j in range(len(groups[i])):
                for m in range(len(groups)):
                    if groups[i] != groups[m]:
                        if groups[i][j] in groups[m]:
                            for elementos in groups[m]:
                                groups[i].append(elementos)
                            groups[m] = []
                            flag = True
            if flag:
                break
    return groups


def removeDuplicated(groups):
    array = []
    for j in range(len(groups)):
        if groups[j] != []:
            groups[j].sort()
            temp = [groups[j][i] for i in range(
                len(groups[j])) if i == 0 or groups[j][i] != groups[j][i-1]]
            array.append(temp)
    return array


def printsMatriz(row, array):
    for i in range(len(row)):
        for j in range(len(row[i])):
            flag = False
            for x in range(len(array)):
                if [i, j] in array[x]:
                    print(x+1, end='')
                    flag = True
                    break
            if flag == False:
                print(row[i][j], end='')
        print('\n', end='')

# function that generate the lists


def generateLists(row):
    group = []
    groups = []
    for i in range(len(row)):
        for num in range(len(row[i])):  # runs through each number in row's
            if row[i][num] == '1':
                group.append([i, num])
                try:
                    if row[i][num-1] == '1':
                        group.append([i, num-1])
                    if row[i-1][num] == '1':
                        group.append([i-1, num])
                    groups.append(group)
                    group = []
                except IndexError:
                    break
    return groups


def main(row):
    groups = generateLists(row)
    orderedGroups = merge(groups)
    orderedGroups = removeDuplicated(orderedGroups)
    printsMatriz(row, orderedGroups)


main(row)
