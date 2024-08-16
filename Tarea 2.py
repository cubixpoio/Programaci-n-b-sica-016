#actividad 1  
print ("ingrese dos numeros")
num1=int(input())
num2=int(input())

def max_num(num1,num2):
    if num1>num2:
        return num1
    elif num2>num1:
        return num2

print(max_num(num1,num2))   

#actividad 2
num1 = (input("Ingresa el primer número: "))
num2 = (input("Ingresa el segundo número: "))
num3 = (input("Ingresa el tercer número: "))
def max_num(num1,num2,num3):
    if (num1 >= num2) and (num1 >= num3):
       return num1
    elif (num2 >= num1) and (num2 >= num3):
       return num2
    else:
       return num3
print(max_num(num1,num2,num3))

actividad 3
text = "oh y ahora que voy a escribit aqui?"

def count_txt(txt):
    count = 0
    for n in txt:
       count += 1
    return count

print(count_txt(text))

#act 4
def es_vocal(caracter):
    vocales = "aeiouAEIOU"
    if caracter in vocales:
        return True
    else:
        return False
letra = input("Ingresa un carácter: ")
if len(letra) == 1:
    if es_vocal(letra):
        print("True.")
    else:
        print( "False.")


#act 5
def sum_list():
    list_num = [int(input()) for _ in range(4)]
    sum_num = 0
    for n in list_num:
        sum_num += n
    return sum_num
suma_total = sum_list()
print(suma_total)

def multnum_list():
    list_num = [int(input()) for _ in range(4)]
    mult_num = 1
    for n in list_num:
         mult_num *= n
    return mult_num
multi_total = multnum_list
print(multi_total)

# act 6
def cadena(txt):
    if len(txt) == 0:
        return txt
    else:
        return cadena(txt[1:]) + txt[0]

txt = input("ingrese una texto")
print(cadena(txt))
 
# act 7
texto  = input ("la palabra:  ")
def es_palindromo(palabra):
    long = len(palabra)
    
    for n in range(long // 2):
        if palabra[n] != palabra [long -1 - n]:
          return False
    return True

resultado = es_palindromo(texto)
print(f"{texto}: {resultado}")


#act 8 
def superposicion(lista1, lista2):
    comunes = []
    for elemento1 in lista1:
        for elemento2 in lista2:
            if elemento1 == elemento2:
                comunes.append(elemento1)
    return comunes

def obtener_lista(mensaje):
    lista = []
    print(mensaje)
    while True:
        entrada = input("incetar un numero o deja en blanco para terminar: ")
        if entrada == "":
            break
        lista.append(entrada)
    return lista


print("Ingrese los números para la primera lista:")
lista1 = obtener_lista("Primera lista")
print("Ingrese los números para la segunda lista:")
lista2 = obtener_lista("Segunda lista")

comunes = superposicion(lista1, lista2)
if comunes:
    print("Los números en común son:", comunes)
else:
    print("No se encuentran números en común.")

#act 9
def generar_n_caracteres(n, caracter):
    return caracter * n
caracter = input("Ingrese un carácter: ")
n = int(input("Ingrese un número entero: "))

resultado = generar_n_caracteres(n, caracter)
print("Resultado:", resultado)


#act 10
def histograma(lista):
    for numero in lista:
        print('*' * numero)

entrada = input("Ingrese una lista de números enteros separados por espacios: ")
lista_numeros = [int(num) for num in entrada.split()]
print (histograma(lista_numeros))
