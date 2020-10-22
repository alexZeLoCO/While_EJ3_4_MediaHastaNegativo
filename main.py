n=int (input("Introduzca el primer valor: "))       #SOLICITA PRIMER VALOR
suma = 0        #INICIALIZA SUMA        (NUMERADOR)
contador = 0    #INICIALIZA CONTADOR    (DENOMINADOR)

while n>=0:     #MIENTRAS N SEA MAYOR QUE 0
    suma = suma + n     #ACTUALIZAR SUMA
    contador = contador + 1     #ACTUALIZAR CONTADOR
    n = float (input("Introduzca el siguiente valor: "))        #SOLICITA SIGUIENTE VALOR

if suma == 0:       #SI EL PRIMER VALOR ES NEGATIVO, EL DENOMINADOR SERÍA 0
                    #(NO SE ENTRÓ EN EL WHILE ==> CONTADOR = 0)

    contador = 1    #VALOR DE CONTADOR = 1

print ("La media de los números introducidos es:",suma/contador)        #OUTPUT