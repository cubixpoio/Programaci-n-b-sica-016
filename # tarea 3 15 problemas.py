# tarea 3
  #act 1
 # solicita nom y edad y imprimir m
print("ingrse su nombre")  
name =input()
print("ingrese su edad")
edad =input()
print("benvenido",name, "tu edad es",edad) 
    
#act 2
num1 = int(input("ingrese su primer numero entero: "))
num2 = int(input ("ingrese su segundo numero entero:  "))

suma = num1 + num2
print("la suma es:" ,suma )
resta = num1 - num2
print("la resta es:", resta)
multi = num1 * num2
print("la multiplicacion es:", multi)
div = num1 // num2
print("su division es:", div)

#act 3
frase = input("ingrese una frase: ")
print (frase.lower())
print (frase.upper())
print (frase.title())

#act 4
from datetime import datetime

fecha_nacimiento = input("Ingresa tu fecha de nacimiento (dd/mm/yyyy): ")
fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
fecha_actual = datetime.now()
diferencia_dias = (fecha_actual - fecha_nacimiento).days
print(f"Han pasado {diferencia_dias} días desde que naciste.")


#act 5
numero = float(input("Ingresa un número flotante: "))
numero_redondeado = round(numero, 2)
print(f"El número redondeado a dos decimales es: {numero_redondeado}")

#act 6


#act 7
list_num = input("ingrese una lista de numeros separados por comas: ")
num= list_num.split(',')
suma= 0
for n in num:
 suma += int(n)
print("la suma de los numeros es: ",suma)

#act 8
cadena1= input("ingrese su primera  cadena de texto: ")
cadena2= input ("ingrese su segunda cadena de texto: ")

union = cadena1 + cadena2
print(union)

#act 9
def cadena(txt):
    if len(txt) == 0:
        return txt
    else:
        return cadena(txt[1:]) + txt[0]

txt = input("ingrese su nombre")
print(cadena(txt))

#act 10
calificacion1 = float(input("Escribe la primera calificación: "))
calificacion2 = float(input("Escribe la segunda calificación: "))
calificacion3 = float(input("Escribe la tercera calificación: "))

promedio = (calificacion1 + calificacion2 + calificacion3) / 3

print("El promedio de las calificaciones es:", promedio)

#act 11
peso = float(input("Ingresa tu peso en kilogramos: "))

altura = float(input("Ingresa tu altura en metros: "))


imc = peso / (altura ** 2)

if imc < 18.5:
    rango = "Bajo peso"
elif 18.5 <= imc < 24.9:
    rango = "Peso normal"
elif 25 <= imc < 29.9:
    rango = "Sobrepeso"
else:
    rango = "Obesidad"

print("Tu índice de masa corporal (IMC) es:", round(imc, 2))
print("Esto se encuentra en el rango de:", rango)
#act 12
import random
numero_secreto = random.randint(1, 100)

intento = 0

while intento != numero_secreto:
    intento = int(input("Adivina el número entre 1 y 100: "))
    
    if intento < numero_secreto:
        print("El número es mayor.")
    elif intento > numero_secreto:
        print("El número es menor.")
print("¡Adivinaste el número!")

#act 13
nombres = input("Escribe los nombres separados por comas: ")
lista_nombres = nombres.split(',')
lista_nombres.sort()

print("Nombres ordenados por inicial:")
for nombre in lista_nombres:
    print(nombre.strip())

#act 14

numero = int(input("Ingresa un número para mostrar su tabla de multiplicar: "))

print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

#act 15
text = input("Escribe una oración: ")

def count_words(txt):
    words = txt.split()
  
    count = len(words)
    return count

print("Número de palabras en la oración:", count_words(text))
