#trabajo en clase teorica

l = [1, 2, 3]
l2 = l
x = l is l
print(x)

l4 = l.copy()
y = l4 == l
z = l4 is l
print(y, z)
#is es true cuando ambas cosas son exactamente lo mismo

def sq_list(lista :list) -> list:
    lista_2 = lista
    for i in range(len(lista_2)):
        lista_2[1] = lista[i] ** 2
    return lista_2

def generar_lista(n: int) -> list:
    return list(range(n))

def minmax(secuencia):
    minimo = min(secuencia)
    maximo = max(secuencia)
    return minimo, maximo

def swap(a, b):
    temp = a
    a = b
    b = temp
    return (a, b)

def probar_desempaquetado():
    meses = (("enero", 31), 
             ("febrero", 28), 
             ("noviembre", 30))
    for mes, dias in meses:
        print(mes, "tiene", dias, "dias.")
