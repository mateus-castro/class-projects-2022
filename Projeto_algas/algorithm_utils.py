import sys

def size_sum_for(n):
    acumulador=0
    for i in range(0, n+1):
        acumulador += sys.getsizeof(i)
    return acumulador

def size_sum_while(n):
    acumulador=0
    i=0
    while (i in range(0, n+1)):
        acumulador += sys.getsizeof(i)
        i+=1
    return acumulador