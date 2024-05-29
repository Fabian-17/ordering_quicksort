def quicksort(lista, inicio, fin):
    if inicio < fin: # mietnras el inicio sea menor al final de la lista se ejecuta el algoritmo
        p = particion(lista, inicio, fin) # se obtiene el pivote
        quicksort(lista, inicio, p - 1) # se ordena la lista de inicio al pivote
        quicksort(lista, p + 1, fin) # se ordena la lista del pivote al final

def particion(lista, inicio, fin):
    pivot = lista[fin] # se toma el ultimo elemento de la lista como pivote
    i = inicio # se toma el inicio de la lista como indice
    for j in range(inicio, fin): # se recorre la lista de inicio a fin
        if lista[j] <= pivot: # si el elemento de la lista es menor o igual al pivote se intercambian los elementos
            lista[i], lista[j] = lista[j], lista[i] 
            i += 1 # se incrementa el indice
    lista[i], lista[fin] = lista[fin], lista[i] 
    return i

lista = [5, 2, 1, 3, 6, 4, 7, 8, 9, 0]
quicksort(lista, 0, len(lista) - 1)
print(lista)