import timeit
#criar uma lista com 1000 elementos (do 0 ao 999)
def crialista(n):
    lista = []
    for i in range(n):
        lista.append(i)
    return lista

def crialista2(n):
    return list(range(n))
    
temp_start = timeit.default_timer()
crialista(1000)
temp_final = timeit.default_timer()
print("1- Tempo de execução: ", temp_final - temp_start)

temp_start = timeit.default_timer()
a = crialista2(1000)
temp_final = timeit.default_timer()
print("2- Tempo de execução: ", temp_final - temp_start)
