
# ejercicio 3 numeros primos
def esprimo(n):
 if n<=1:
    return False
 elif n==2:
    return True
 else:
    for i in range(2,n):
        if n%i==0:
            return False
    return True
for i in range (-1,10):
    print(i, " ", esprimo (i))