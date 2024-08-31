
#Ejercicio 8 encontrar el mayor y menor en una lista
lista=[]
for i in range(5):
    valor=int(input("ingrese el valor:"))
    lista.append(valor)
mayor=lista[0]
for i in lista:
    if i>mayor:
        mayor=i
print("El numero mayor es:", mayor)
menor=lista[0]
for i in lista:
    if i<menor:
        menor=i
print("El numero menor es:", menor)
