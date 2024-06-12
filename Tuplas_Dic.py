import time
    
tupla = tuple()

tupla = (1)

tuple = (1,)

tupla = 1, 2, 3

print(tupla)

print(tupla[1])

# tupla[0] = 100 #Erro pois não é possivel alterar uma tupla

#Manipulando dicionarios:
dic = {"semMundial":"Palmeiras",
"1mundial":"Corithians",
"2mundiais":"São Paulo"}

print(dic["semMundial"])

notas = {"mat":5, "lp":10, "ef":8}

# print(notas)
# print(notas["lp"])

# print(notas["bio"])

print(dir(notas))

print(notas.values())

print(notas.keys())

print(len(notas))

for disciplina in notas.keys():
    print(disciplina)

time.sleep(3)