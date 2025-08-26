
#punto 1

print ("Hola mundo")

#---Respuesta en consola---

#Hola mundo


#punto 2

nombre = input("Escribe tu nombre: ")
print( f"Hola {nombre}!" )

#---Respuesta en consola---

#Escribe tu nombre: santiago
#Hola santiago!



#punto 3

name = input("Escribe tu nombre: ")

last_name = input("Escribe tu apellido: ")

age = input("Escribe tu fecha de edad: ")

residence = input("Escribe tu lugar de residencia: ")

print (f"Soy {name} {last_name}, tengo {age} años y vivo en {residence}.")

#---Respuesta en consola---

#Escribe tu nombre: san
#Escribe tu apellido: ortiz
#Escribe tu fecha de edad: 23
#Escribe tu lugar de residencia: arg
#Soy san ortiz, tengo 23 años y vivo en arg.


#punto 4

radio = float(input("Ingrese el radio del círculo: "))

area = 3.1416 * radio ** 2

perimetro = 2 * 3.1416 * radio

print(f"El área del círculo es: {area} y el perímetro es: {perimetro}")

#---Respuesta en consola---

#Ingrese el radio del círculo: 5
#El área del círculo es: 78.53999999999999 y el perímetro es: 31.416


#punto 5

seconds = int(input("Ingrese el tiempo en segundos: "))

hours = seconds // 3600

print(f"El tiempo en horas es: {hours}")

#---Respuesta en consola---

#Ingrese el tiempo en segundos: 60000
#El tiempo en horas es: 16


#punto 6

num = int(input("ingrese un numero: "))

result = int()

for i in range(11):
    result = num * i
    print(f"{i} * {num} = {result}")

#---Respuesta en consola---

#ingrese un numero: 8
#0 * 8 = 0
#1 * 8 = 8
#2 * 8 = 16
#3 * 8 = 24
#4 * 8 = 32
#5 * 8 = 40
#6 * 8 = 48
#7 * 8 = 56
#8 * 8 = 64
#9 * 8 = 72
#10 * 8 = 80


#punto 7

print ("Coloque dos numero que sean distintos al cero")

num1 = int(input("Coloque un numero: "))

num2 = int(input("Coloque otro numero: "))


if num1 == 0 or num2 == 0 :

    print("Porfavor coloque un numero distinto al cero")

else:
    
    resultado = num1 + num2
    print ("la suma de los dos numero es: ", resultado)

    resultado = num1 - num2
    print ("la resta de los dos numero es: ", resultado)

    resultado = num1 * num2
    print ("la multiplicación de los dos numero es: ", resultado)

    resultado = num1 / num2
    print ("la división de los dos numero es: ", resultado)

#---Respuesta en consola---


#Coloque dos numero que sean distintos al cero
#Coloque un numero: 5
#Coloque otro numero: 4
#la suma de los dos numero es:  9
#la resta de los dos numero es:  1
#la multiplicación de los dos numero es:  20
#la división de los dos numero es:  1.25



#----- respuesta 2 ------


#Coloque dos numero que sean distintos al cero
#Coloque un numero: 4
#Coloque otro numero: 0
#Porfavor coloque un numero distinto al cero




#punto 8

weight= float(input("Coloque su peso: "))

height=float(input("Colque su altura: "))


imc = weight / (height**2)

print (f"Su IMC es: {imc}")

#---Respuesta en consola---


#Coloque su peso: 56
#Colque su altura: 1.70
#Su IMC es: 19.377162629757787


#punto 9

temp_celsius = float(input("Coloque la temperatura en Celsius: "))

temp_fahrenheit = ((9 / 5) * temp_celsius) + 32

print(f"la temperatura de {temp_celsius} ° celsius, pasadas a fahrenheit es de: {temp_fahrenheit}")

#---Respuesta en consola---

#Coloque la temperatura en Celsius: 30
#la temperatura de 30.0 ° celsius, pasadas a fahrenheit es de: 86.0



#punto 10

print("Coloque 3 numeros que desee calcular el promedio")

num1 = int(input("Coloque el 1° numero: "))
num2 = int(input("Coloque el 2° numero: "))
num3 = int(input("Coloque el 3° numero: "))

prom = (num1 + num2 + num3) / 3

print(f"El promedio de los tres numeros es: {prom}")

#---Respuesta en consola---


#Coloque 3 numeros que desee calcular el promedio
#Coloque el 1° numero: 2
#Coloque el 2° numero: 10
#Coloque el 3° numero: 10
#El promedio de los tres numeros es: 7.333333333333333