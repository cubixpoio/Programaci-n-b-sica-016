#act 1 

def max_in_list(numbers):
    if len(numbers) == 0:
        return None  # Maneja el caso donde la lista está vacía
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

numeros = input("Ingresa una lista de números separados por comas: ")

numeros = [int(x) for x in numeros.split(",")]
print("El número más grande es:", max_in_list(numeros))

#act 2
def mas_larga(palabras):
    palabra_mas_larga = ""
    for palabra in palabras:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra
    return palabra_mas_larga
    
palabras = input("Ingresa palabras separadas por espacios: ").split()
print("La palabra más larga es:", mas_larga(palabras))


#act 3
def filtrar_palabras(palabras, n):
    return [palabra for palabra in palabras if len(palabra) > n]
entrada_palabras = input("Ingresa palabras separadas por espacios: ")
palabras = entrada_palabras.split()

n = int(input("Ingresa el número n: "))

palabras_filtradas = filtrar_palabras(palabras, n)
print("Palabras con más de", n, "caracteres:", palabras_filtradas)


#act 4
def contar_mayusculas(cadena):
    count = 0
    for char in cadena:
        if char.isupper():
            count += 1
    return count

cadena = input("Ingresa una palabra o frase: ")

cantidad_mayusculas = contar_mayusculas(cadena)

print("La cadena tiene", cantidad_mayusculas, "letras mayúsculas.")

#act 5
def binario_a_entero(binario):
    numero_entero = 0
    for digito in binario:
        numero_entero = numero_entero * 2 + int(digito)
    return numero_entero

numero_binario = input("Ingresa un número binario: ")

numero_entero = binario_a_entero(numero_binario)

print("El número entero es:", numero_entero)

#act 6
año_curso = int(input("Ingresa el año de curso: "))

for i in range(3):
    nombre = input("Ingresa el nombre: ")
    año_nacimiento = int(input("Ingresa el año de nacimiento: "))
    edad = año_curso - año_nacimiento
    print(f"{nombre} cumplirá {edad} años en {año_curso}.")

#act 7
edades = [int(input("Ingrese una edad: ")) for _ in range(10)]

edades_tupla = tuple(edades)

cantidad_superior_a_20 = sum(edad > 20 for edad in edades_tupla)

print("Cantidad de personas con edades superiores a 20:", cantidad_superior_a_20)

#act 8
nombres = ["Miguel", "Pedro", "Alberto", "María", "Susana", "Laura", "Ana María"]

cantidad_comienza_con_a = 0
for nombre in nombres:
    if nombre[0].lower() == 'a':
        cantidad_comienza_con_a += 1


print("Cantidad de nombres que comienzan con la letra 'a':", cantidad_comienza_con_a)

#act 9
def contar_vocales(palabra):
    conteos = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    for letra in palabra.lower():
        if letra in conteos:
            conteos[letra] += 1
    
    return conteos

palabra = input("Ingresa una palabra: ")
conteos = contar_vocales(palabra)

print("Conteo de vocales:")
for vocal, cantidad in conteos.items():
    print(f"{vocal}: {cantidad}")


#act10
def es_bisiesto(año):

    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else:
        return False

año = int(input("Ingresa un año: "))
if es_bisiesto(año):
    print(f"El año {año} es bisiesto.")
else:
    print(f"El año {año} no es bisiesto.")
