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

#act 10

#act 11

#act 12

#act 13

#act 14

#act 15
