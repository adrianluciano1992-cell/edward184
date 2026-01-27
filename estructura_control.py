"""
operadores
la f es interporacion
"""

# operadores aritmeticos

print (f"suma: 10 + 3 = {10 + 3}")
print (f"resta: 10 - 3 = {10 - 3})
print (f " multiplicacion: 10 * 3 = {10 *3})
print (f " division: 10 / 3 = {10 / 3})
print (f" modulo: 10 % 3 = {10 % 3})
print(f"esponente: 10 ** 3 ={10 ** 3}")
print (f"division entera: 10 // 3 = {10 // 3}")

# operadores de comparacion (nos sirve para comparar valores de variables 
print(f"igualda: 10 == 3 = {10 == 3}")
print(f" desigualdad: 10 != 3 = {10 != 3})
print (f " mayor que : 10 > 3 = {10 > 3})
print (f " nenor que : 10 < 3 = {10 < 3})
print (f "mayor o igual: 10 >= 3 = {10 >= 3}")
print (f "menor o igual: 10 <= 3 = {10 <= 3})

# operadores logicos: son comunes a la gran mayoria de los otros lenguajes 
print (f"and && : 10 + 3 == 13 and 5 - 3 == 2 es {10 + 3 == 13 and 5 - 3 == 2}")

# or nos pide que aunque sea una verdadera uan de las condiciones  
print (f"OR || : 10 + 3 == 13 or 5 - 3 == 2 es {10 + 3 == 13 and 5 - 3 == 2}") 

# agregando el not no seria verdadero en caso de que lo que esta alli no se cumpliera 
print(f " NOT ! : not 10 + 3 == 14 es {not 10 + 3 == 14}")

"""
se usan en conjunto con el valor de las variable
operadores de asignacion
"""

my_number = 11 # asignacion

print(my_number)
my_number += 1 # suma y asignacion

print(my_number)
my_number -= 3 # resta y asignacion

print(my_number)
my_number /= 4 # division y asignacion

print(my_number)
my_number *= # multiplicacion y asignacion

print(my_number)
my_number %= 3 # modulo y asignacion

print(my_number)
my_number //= 4 # division entera y asignacion 

# operadores de identidad: nos sirven para comprar valores . valores de la posicion de memoria
my_new_number = my_number
print (f"my_number is my_new_number es {my_number is my_new_number}")

# operadores de pertenencia si algo le pertenese a algo

print ( f "'u' in 'mouredev' = {'u' in 'mouredev'})
print ( f " 'b' is not 'mouredev' = {'u ' is not 'mouredev'})

# operadores de bit casi no se usan pero igual tomar en cta 

a = 3 # 1010
b = 10 # 0011

print (f " AND: 10 & 3 = {10 & 3}") # 0010
print (f " OR: 10 | 3 = {10 | 3}) # 1011
print (f " XOR: 10 ^ 3 = {10 ^ 3}) # 1001 
print (f " NOT: ~ 10 = {~ 10}) 
print (f " desplazamiento a la derecha : 10 >> 2 {10 >> 2}) # 0010
print (f "desplazamiento a la izquierda: 10 << 2 { 10 << 2}) # 101000

"""
Estructura de 
control
"""

# condicionales 

my_string = mouredev

if(my_string == mouredev)
print(" El string si es mouredev")
elif my_string == "edward"
print("my_string es 'edward'")

else 
print(" El string no es mouredev")




















