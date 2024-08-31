#Ejercicio 11 suma de digitos
N=int(input("ingrese numero de 3 digitos: "))
suma=0
if N > 0:
    c=N%10
    N=N//10
    b=N %10
    a=N//10
    suma=a+b+c
print("la suma de los digitos es: ", suma)