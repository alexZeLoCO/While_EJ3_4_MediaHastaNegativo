#INICIALIZA SUMA            (NUMERADOR) EJERCICIO 3
suma = 0
#INICIALIZA SUMA PARES      (NUMERADOR) EJERCICIO 4
sumapares = 0
#INICIALIZA SUMA IMPARES    (NUMERADOR) EJERCICIO 4
sumaimpares = 0
#INICIALIZA CONTADOR        (DENOMINADOR)   EJERCICIO 3
contador = 0
#INICIALIZA CONTADOR PARES  (DENOMINADOR)     EJERCICIO 4
contadorpares = 0
#INICIALIZA CONTADOR IMPARES (DENOMINADOR)  EJERCICIO 4
contadorimpares = 0

n=int (input("Introduzca el primer valor: "))       #SOLICITA PRIMER VALOR

while n>=0:     #MIENTRAS N SEA MAYOR QUE 0

    contador = contador + 1  # ACTUALIZAR CONTADOR
    suma = suma + n  # ACTUALIZAR SUMA

    if n%2==0:      #SI ES PAR
        contadorpares = contadorpares + 1  # ACTUALIZAR CONTADOR
        sumapares=sumapares+n       #ACTUALIZAR SUMA

    if n%2!=0:      #SI ES IMPAR
        contadorimpares = contadorimpares + 1  # ACTUALIZAR CONTADOR
        sumaimpares=sumaimpares+n   #ACTUALIZAR SUMA

    n = float(input("Introduzca el siguiente valor: "))  # SOLICITA SIGUIENTE VALOR


#DEBEMOS REVISAR SI SE HAN INTRODUCIDO VALORE DE TODOS LOS TIPOS.
#SI NO, DIVIDIRÍAMOS ENTRE 0. DAREMOS VALOR 1 EN SU LUGAR.
if suma == 0:       #SI SUMA TOTAL ES 0
    contador = 1    #CONTADOR 1
    suma = 1        #SUMA 1
if sumapares == 0:      #SI SUMA PARES ES 0
    contadorpares = 1   #CONTADOR PARES 1
    sumapares = 1       #SUMA PARES 1
if sumaimpares == 0:        #SI SUMA IMPARES ES 0
    contadorimpares = 1     #CONTADOR IMPARES 1
    sumaimpares = 1         #CONTADOR IMPARES 1

print("La media de los números introducidos es:", suma/contador)  # OUTPUT
print("La media de los números pares introducidos es:", sumapares/contadorpares)  # OUTPUT
print("La media de los números impares introducidos es:", sumaimpares/contadorimpares)  # OUTPUT
