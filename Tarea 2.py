#actividad 1  
#print ("ingrese dos numeros")
#num1=int(input())
#num2=int(input())

#def max_num(num1,num2):
    #if num1>num2:
        #return num1
    #elif num2>num1:
        #return num2

#print(max_num(num1,num2))   

#actividad 2
#num1 = (input("Ingresa el primer número: "))
#num2 = (input("Ingresa el segundo número: "))
#num3 = (input("Ingresa el tercer número: "))
#def max_num(num1,num2,num3):
    #if (num1 >= num2) and (num1 >= num3):
       #return num1
    #elif (num2 >= num1) and (num2 >= num3):
       #return num2
    #else:
       #return num3
#print(max_num(num1,num2,num3))

#actividad 3
#text = "oh y ahora que voy a escribit aqui?"

#def count_txt(txt):
    #count = 0
    #for n in txt:
       #count += 1
    #return count

#print(count_txt(text))

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

