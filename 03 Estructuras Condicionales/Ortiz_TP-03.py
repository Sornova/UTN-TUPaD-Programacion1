
import random
from statistics import mode, median, mean

#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.


edad_minima = 18
edad = int(input("coloque su edad: "))

if edad >= edad_minima:
    print("Es mayor de edad")

else:
    print("Es menor de edad")



#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.


nota = int(input("Coloque la nota del usuario: "))

if nota >= 6:
    print("Aprobado")

else:
    print("Desaprobado")


#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.


num_user = int(input("Coloque un numero: "))

num_par = num_user % 2 

if num_par == 0:
    print("Ha ingresado un número par")

else:
    print("Por favor, ingrese un número par")


#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 as y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 año.#


edad = int(input("coloque su edad: "))

if edad < 12:
    print("Niño/a")

elif (edad >= 12) and (edad < 18):
    print("Adolescente")

elif (edad >= 18) and (edad < 30):
    print("Adulto/a joven")

elif edad >= 30:
    print("Adulto/a")




#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, impri#mir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprim#ir por#
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: invest#igue e#l us#o
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iter#able t#al#
#como una lista o un string


while True:
        
    password =input("Coloque una contraseña: ")
    
    long_pass = len(password)

    if not((long_pass >= 8) and (long_pass <= 14)):
        print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

    else:
    
        print("Ha ingresado una contraseña correcta")
        break




#6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
# y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el siguiente: ...


#Variables
num_aleatorios = [random.randint(1, 100) for i in range(50) ]
media = mean(num_aleatorios)
mediana = median(num_aleatorios)
moda = mode(num_aleatorios)


#lista de numeros aleatorios
print(num_aleatorios)
print("La media es:", media)
print("La mediana es:", mediana)
print("La moda es:", moda)

sesgo_pos_right = (media > mediana) and (mediana > moda)

sesgo_neg_left = (media < mediana) and (mediana < moda)

sin_sesgo = (media == moda) and (media == mediana)

if sesgo_pos_right:
    print("Sesgo positivo o a la derecha")
elif sesgo_neg_left:
    print("Sesgo negativo o a la izquierda")
elif sin_sesgo:
    print("Sin sesgo")
else:
    print("No se puede determinar el sesgo")



#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.



name = input("Coloque su nombre \n ")
option = input("""Coloque la opcion que desea: \n 1. Si quiere su nombre en mayúsculas \n 2. Si quiere su nombre en minúsculas \n 3. Si quiere su nombre con la primera letra mayúscula. \n """)

name = name.lower()

if option == 1:
    print(name.upper())

elif option == 2:
    print(name.lower())

elif option == 3:
    print(name.title())

else:
    print("numero invalido")



#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
#por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).


mag = int(input("Coloque la magnitud del terremoto: \n "))

if mag < 3:
    mag_result = """ "Muy leve" (imperceptible). """

elif (mag >= 3) and (mag < 4):
    mag_result = """ "Leve" (ligeramente perceptible). """

elif (mag >= 4) and (mag < 5):
    mag_result = """ "Moderado" (sentido por personas, perogeneralmente no causa daños). """

elif (mag >= 5) and (mag < 6):
        mag_result = """ "Fuerte" (puede causar daños en estructuras débiles). """

elif (mag >= 6) and (mag < 7):
        mag_result = """ "Muy Fuerte" (puede causar daños significativos). """

elif mag >= 7:
        mag_result = """ "Extremo" (puede causar graves daños a gran escala). """

print(mag_result)




#10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año

#                                         (tabla)

#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.



# Inputs

hemisferio = input(""" Escriba una de las dos opciones, dependiendo donde se encuntre: \n "S" = Emisferio Sur \n "N" = Emisferio Norte. \n """)

mes = int(input("Coloque un mes: \n"))

dia = int(input("Coloque un dia: \n"))



# Validaciones
hemisferio = hemisferio.lower()


#Tupla
fecha = (mes, dia)


#Clasificacion

invierno_n = ( (12,21) <= fecha <= (12,31) ) or ( (1,1) <= fecha <= (3,20) )

primavera_n = ( (3,21)  <= fecha <= (6,20) )

verano_n = ( (6,21)  <= fecha <= (9,20) )

otono_n = ( (9,21)  <= fecha <= (12,20) )




if hemisferio == "n":

    if invierno_n:  
        estacion = "Invierno"

    elif primavera_n: 
        estacion = "Primavera"

    elif verano_n: 
        estacion = "Verano"

    else:
        estacion = "Otoño"

else:

    if invierno_n:  
        estacion = "Verano"

    elif primavera_n: 
        estacion = "Otoño"

    elif verano_n: 
        estacion = "Invierno"

    else:       
        estacion = "Primavera"

print(estacion)