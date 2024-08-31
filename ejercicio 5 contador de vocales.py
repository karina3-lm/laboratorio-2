
#Ejercicio 5 contar vocales
texto=input("ingrese una frase: " )
vocales="aeioAEIOU"
contador=0
for i in texto:
    if i in vocales:
        contador=contador +1
print("la cantidad de vocales es: ", contador )

    