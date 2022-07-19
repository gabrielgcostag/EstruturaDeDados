def bubble_sort(lista):
    elementos = len(lista)-1
    ordenado = False
    count = 0
    while not ordenado:
        ordenado = True
        for i in range(elementos):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1],lista[i]
                ordenado = False        
                count += 1
    return count

n = int(input())
lista = [int(i) for i in input().split()]

print(bubble_sort(lista))