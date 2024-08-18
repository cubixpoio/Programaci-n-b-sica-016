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
