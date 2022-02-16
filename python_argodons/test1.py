# separando todos os caracteres de uma string e adicionando em um array

def string_split(str):
    arr=[]
    for index in str:
        arr.append(index)
    return arr

print(string_split('teste'))