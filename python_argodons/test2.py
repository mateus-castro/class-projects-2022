# estudo de lambda
def adding_10(arr):
    lmbd = lambda a : a + 10 # expresão aplicada para os índices do vetor
    resul=[]
    for x in arr:
        resul.append(lmbd(x))
    return resul

print(adding_10([1,2,3,4]))