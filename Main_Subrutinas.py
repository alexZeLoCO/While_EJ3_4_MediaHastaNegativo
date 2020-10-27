suma = 0        #SUMATORIO DE VALORES           (NUMERADOR)
contador = 0        #CONTADOR DE VUELTAS        (DENOMINADOR)

#NOTA:
#   AL UTILIZAR SUBRUTINAS, NOS PODEMOS PERMITIR USAR SÓLO DOS VARIABLES.
#   UNA PARA LA SUMA Y OTRA PARA EL CONTADOR. PORQUE LAS VARIABLES DENTRO DE UNA SUBRUTINA
#   EXISTEN SÓLAMENTE EN ESA SUBRUTINA.

#   ESTO ES, CON SÓLO DOS VARIABLES Y TRES SUBRUTINAS, PODEMOS ALMACENAR 6 VALORES:
#       SUBRUTINA 1: SUMA Y CONTADOR
#       SUBRUTINA 2: SUMA Y CONTADOR
#       SUBRUTINA 3: SUMA Y CONTADOR

#   COMO CADA VARIABLE ES DIFERENTE EN CADA SUBRUTINA,
#   DEBEREMOS DAR EL RESULTADO DESDE DENTRO DE LA SUBRUTINA.

#SUBRUTINA 1 = SOLUCIÓN EJERCICIO 3
def MediaTotal (suma, n , contador):        #PARÁMETROS SUMA, N Y CONTADOR
    if n>0:     #SI N ES NEGATIVO (FIN DE BUCLE)
        suma = suma + n  # ACTUALIZAR SUMATORIO
        contador = contador + 1  # ACTUALIZAR CONTADOR DE VUELTAS
    else:       #SI NO (EVALUANDO SUMA)
        contador = Check(contador)
        return suma / contador  # IMPRIMIR MEDIA

#SUBRUTINAS 2 Y 3 = SOLUCION EJERCICIO 4
def MediaPares (suma, n , contador):        #PARÁMETROS SUMA, N Y CONTADOR
    if n<0:        #SI N ES NEGATIVO (FIN DE BUCLE)
        contador = Check(contador)
        return suma/contador     #IMPRIMIR MEDIA DE PARES
    else:       #SI NO (EVALUANDO SUMA)
        suma = suma + n     #ACTUALIZAR SUMATORIO PARES
        contador = contador + 1     #ACTUALIZAR CONTADOR DE VUELTAS PARES

def MediaImpares (suma, n, contador):       #PARÁMETROS SUMA, N Y CONTADOR
    if n<0:     #SI N ES NEGATIVO (FIN DE BUCLE)
        contador = Check(contador)
        return suma/contador       #IMPRIMIR MEDIA DE IMPARES
    else:       #SI NO (EVALUANDO SUMA)
        suma = suma + n     #ACTUALIZAR SUMATORIO DE IMPARES
        contador = contador + 1     #ACTUALIZAR CONTADOR DE VUELTAS IMPARES

def Check (contador):
    if contador == 0:
        coontador = 1
    return contador


n = int(input ("Introduzca el primer valor: "))     #SOLICITA PRIMER VALOR
if n < 0:       #SI EL PRIMER VALOR ES NEGATIVO
    print ("El primer valor ya es negativo, no existe media positiva.")     #OUTPUT
else:       #SI NO ==> PROGRAMA PRINCIPAL
    while n>=0:     #MIENTRAS N SEA POSITIVO
        n = int (input("Introduzca el siguiente valor: "))
        MediaTotal(suma, n, contador)          #EN CADA VUELTA SE EVALÚA EL VALOR N     (LLAMAMOS SUBRUTINA 1)
        if n%2==0:      #EN CADA VUELTA EN LA QUE N SEA PAR
            MediaPares(suma,n,contador)     #SE EVALÚA EL VALOR PAR                     (LLAMAMOS SUBRUTINA 2)
        else:           #SI NO ES PAR, ES IMPAR
            MediaImpares(suma,n,contador)   #SE EVALÚA EL VALOR IMPAR                   (LLAMAMOS SUBRUTINA 3)

    print("La media de todos es:",MediaTotal(suma,n,contador))              #OUTPUT
    print("La media de los pares es:",MediaPares(suma,n,contador))          #OUTPUT
    print("La media de los impares es:",MediaImpares(suma,n,contador))      #OUTPUT