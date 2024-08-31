
#Ejercicio 20: Determinacion del tipo de triangulo
print(" ingresa los 3 lados del triangulo: ")
x=float(input( ))
y=float(input( ))
z=float(input( ))
if x==y and y==z:
    print("El triangulo es equilatero ")
elif x!=y and x!=z and y!=z:
        print("El triangulo es escaleno ")
else:
    (x==y and x!=z) or (x==z and x != y)
    print("El triangulo es isoceles ")