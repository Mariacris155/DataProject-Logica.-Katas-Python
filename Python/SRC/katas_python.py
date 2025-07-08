'''1.Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias
de cada letra en la cadena. Los espacios no deben ser considerados.'''

def contar_frecuencias(cadena):
    frecuencias = {}
    for caracter in cadena:  #Bucle que recorre la cadena y por cada caracter mira si está en frecuencias y si no lo añade
        if caracter != ' ':
            caracter = caracter.lower() 
            if caracter in frecuencias:
                frecuencias[caracter] += 1
            else:
                frecuencias[caracter] = 1
    return frecuencias


'''2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()'''



def duplicar(num): #funcion a introducir en la funcion map que duplica numeros
    return num*2

lista_numeros1 = [1,2,3,4,5,6,7,8,9]
dobles = list(map(duplicar,lista_numeros1))
print (f'{dobles}')



'''3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe
devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.'''

def buscar_p_objetivo (lista_palabras, palabra_objetivo):
    lista_resultado3 = []

    for palabra in lista_palabras:  # Bucle que recorre la lista de palabras, si la palabra objetivo está en la palabra la mete a la lista
      if palabra_objetivo in palabra:
          lista_resultado3.append(palabra)
          return lista_resultado3
      
'''4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()'''

def diferencia (lista1, lista2):
    return list(map(restar, lista1, lista2))

def restar(a, b):
        return a - b

'''5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por
defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual
que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver
una tupla que contenga la media y el estado.'''

def media (lista_notas, nota_aprobado = 5):

    promedio = sum(lista_notas) / len(lista_notas)

    if promedio >= 5:
        estado = "aprobado"
    else:
        estado = "suspenso"
    
    return (promedio, estado)

'''6. Escribe una función que calcule el factorial de un número de manera recursiva.'''
def factorial(n):
     return n * factorial(n - 1)

'''7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()'''

def tuplas_a_strings(lista_tuplas):
    return list(map(str, lista_tuplas))

'''8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
indicando si la división fue exitosa o no.'''

try: 
    num1 = int(input('Ingrese un número'))
    num2 = int(input('Ingrese otro número'))

    resultado = round(num1/num2)

except ValueError:

        print("Por favor ingrese un número")
    
except ZeroDivisionError:
        print("Por favor ingrese un número distinto de 0")
    
else:
    print(f"El resultado de la división es:", {resultado})

'''9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
"Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()'''



def comprobar_mascotas (mascota):

    mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    '''funcion que verifica si la mascota está enla lista'''
    return mascota not in mascotas_prohibidas

def filtrar_mascotas(lista_mascotas): 
    '''funcion que filtra las listas'''
    return list(filter(comprobar_mascotas, lista_mascotas))

'''10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una
excepción personalizada y maneja el error adecuadamente.'''

class EmptyListError(Exception):
    '''creamos una excepcion personalizada que hereda la clase exception'''
def calcular_promedio (lista_numeros):
    '''si la lista está vacia llamamos al error'''
    if not lista_numeros:
        raise EmptyListError("Lo sentimos la lista no puede estar vacía")
    
    return sum(lista_numeros) / len(lista_numeros)

'''11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un
valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones
adecuadamente.'''

try:
    edad = int(input('Ingrese su edad'))

    
    if edad <0 or edad > 120:
        print("Edad fuera de rango, debe estar entre 0 y 120")
    else:
        print("Gracias por la información")
except ValueError:

    print("Debe ingresar un número válido")

'''12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()'''

def longitud(frase):
    return list(map(len,frase))

'''13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en
mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()'''

def convertir_mayus_minus(caracter): #primero una funcion para convertir a mayusculas y minusculas
    return (caracter.upper(), caracter.lower())

def mayus_minus_tuplas(caracteres):
    unicos = set(caracteres)   # eliminar duplicados porque en un set no pueden
    return list(map(convertir_mayus_minus, unicos))


'''14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la
función filter()'''

def filtrar_por_letra(palabras, letra):
    return list(filter(lambda palabra: palabra.startswith(letra), palabras))


'''15. Crea una función lambda que sume 3 a cada número de una lista dada.'''

sumar3 = lambda num15: num15 + 3 #no se si tengo que aplicarla a una funcion map para que plique la funcion lambda a una lista, solo me pedia la lambda



'''16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de
todas las palabras que sean más largas que n. Usa la función filter()'''

def filtrar_cadena(palabra, n):  #funcion que usa un condicional que mide la longitud de la palabra si es mayor que n
    if len(palabra) > n:
        return True
    else:
        return False

def palabras_mas_largas(cadena, n):
    palabras = cadena.split()
    return list(filter(lambda p: filtrar_cadena(p, n), palabras))

'''17.Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2]
corresponde al número quinientos setenta y dos (572). Usa la función reduce()'''

from functools import reduce

def totales (total,digito):   #funcion que acumula el numero para luego usarlo en reduce
     return total * 10 + digito

def lista_digitos(digitos):  #funcion que aplica reduce y hace una lista con los totales

    return reduce(totales, digitos)

'''18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes
(nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a
90. Usa la función filter()'''

# Lista de estudiantes
estudiantes = [
    {"nombre": "Ana", "edad": 20, "calificacion": 85},
    {"nombre": "Luis", "edad": 21, "calificacion": 92},
    {"nombre": "Carla", "edad": 19, "calificacion": 95},
    {"nombre": "Pedro", "edad": 22, "calificacion": 78},
    {"nombre": "María", "edad": 20, "calificacion": 90}
]

# Función para filtrar estudiantes con calificación >= 90
def es_sobresaliente(estudiante):
    return estudiante["calificacion"] >= 90


estudiantes_sobresalientes = list(filter(es_sobresaliente, estudiantes)) # Aplicar filter

print(estudiantes_sobresalientes)


'''19.Crea una función lambda que filtre los números impares de una lista dada.'''

filtrar_impares = lambda lista:  [x for x in lista if x % 2 != 0]


'''20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función
filter()'''

lista = [1, 'hola', 3, 'mundo', 5, 6.7, 8]

lista_enteros = list(filter(lambda x: type(x) == int, lista)) #filtra los datos por el tipo de dato en este caso int

print(lista_enteros)





'''21. Crea una función que calcule el cubo de un número dado mediante una función lambda'''

cubo_numero = lambda x: x** 3 

print (cubo_numero)




'''22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() .'''

from functools import reduce

lista_numeros22 = [2,5,9,6,19,20]

def producto_total (lista):
    return  reduce (lambda x , y: x*y, lista) #la funcion lambda calcula el producto de los 2 primeros numeros y reduce va aplicando a los siguientes elementos





'''23. Concatena una lista de palabras.Usa la función reduce()'''

from functools import reduce

palabras = ["Hola", "mundo", "me", "llamo", "Python"]

def concatenar(palabra1, palabra2): #funcion que concatena las palabras en un string
    return palabra1 + " " + palabra2

resultado = reduce(concatenar, palabras) #aplica la funcion reduce a la funcion concatenar y a la ista de palabras

print(resultado)





'''24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() .'''

from functools import reduce

lista_numeros24 = [2,5,9,6,19,20]

def diferencia_total (lista):
    return  reduce (lambda x , y: x/y, lista)




'''25. Crea una función que cuente el número de caracteres en una cadena de texto dada.'''

cadena_texto = "Hola, mundo, mi, nombre, es, Python"

def contar_caracteres(cadena):

    return len(cadena)




'''26. Crea una función lambda que calcule el resto de la división entre dos números dados.'''

lambda x , y: x%y





'''27. Crea una función que calcule el promedio de una lista de números.'''

def promedio (lista):

     return sum(lista) / len(lista)




'''28.Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.'''
    
def primer_duplicado(lista):
    listado_duplicados = set()
    for elemento in lista: #por cada elemento en la lista
        if elemento in listado_duplicados:  
            return elemento  #como en los sets no pueden ir elementos duplicados cuando encuentra uno lo devuelve
        else:
            listado_duplicados.add(elemento)  #al recorrerlo si el elemento no está duplicado lo añade al set
    return None  # si no hay duplicados





'''29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el
carácter '#', excepto los últimos cuatro.'''

def enmascarar_variable(valor):
    cadena = str(valor)  # convertir a string por si pasan números
    if len(cadena) <= 4:
        return cadena  # si es menor o igual a 4, no enmascara nada
    else:
        return '#' * (len(cadena) - 4) + cadena[-4:] #multiplica # pr la longitud de la cadena menos 4 para ocultar los caracteres y luego se le suman caracteres faltantes con metodo start





'''30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras
pero en diferente orden.'''

def son_anagramas(palabra1, palabra2): #funcion que verifica si 2 palabras son anagramas


#pasamos a minusculas
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()


    if len(palabra1) != len(palabra2):  #condicional que mide la longitud, si es distinta no son anagramas
     return False

    return sorted(palabra1) == sorted(palabra2)  #sorted ordena las letras de la palabra


'''31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se
lanza una excepción.'''


def buscar_nombre():
    try:
        lista_entrada = str(input('Ingrese varios nombres separados por comas:'))

        lista_nombres = [nombre.strip() for nombre in lista_entrada.split(",")]

     #  Ahora pedimos el nombre que se desea buscar
        nombre_buscar = input("Ingrese el nombre a buscar: ").strip()
        
        # Verificamos si está en la lista
        if nombre_buscar in lista_nombres:
                    print(f"El nombre '{nombre_buscar}' fue encontrado en la lista.")
        else:
                    # si no está, lanzamos excepción
                    raise ValueError(f"El nombre '{nombre_buscar}' no está en la lista.")

    except ValueError:

         print("Debe ingresar un nombre valido")


'''32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona
no trabaja aquí.'''

def buscar_empleado(nombre,empleados): #busca el nombre de los empleados

    
        if nombre in empleados:
            print(f"{nombre}")
        
        else:
            print("Esa persona no trabaja aqui")


'''33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.'''

lambda x , y: x+y

'''34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:
crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para
manipular la estructura del árbol.'''

class arbol:

    def __init__(self,tronco,ramas):

        self.tronco = tronco
        self.ramas = ramas

    def info_arbol(self):
        print(f"tronco:{self.tronco}, ramas{self.ramas}")

    def crecer_tronco(self, crecimiento):
        self.tronco += crecimiento
        print(f"El tronco ahora mide {self.tronco}")

    def nueva_rama(self, rama):
        self.ramas.append(rama)
        print(f"Ahora hay {self.ramas} ramas")
    
    def crecer_ramas(self, crecimiento):
        self.ramas = [rama + crecimiento for rama in self.ramas]
        print(f"Las ramas ahora miden {self.ramas}")

    def quitar_rama(self, rama):
        self.ramas.pop(rama)
        print(f"Ahora hay estas ramas:  {self.ramas}")







'''35.No hay enunciado de 35'''





'''36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta
corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y
agregar dinero al saldo.'''


class UsuarioBanco:

    def __init__(self, nombre, saldo, cuenta= True ):

            """
        Inicializa el usuario con su nombre, saldo y si tiene cuenta corriente (por defecto True)
        """
            self.nombre = nombre
            self.saldo = saldo
            self.cuenta = cuenta

    def retirar_dinero(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser positiva.")
        
        elif cantidad > self.saldo:
            raise ValueError("Saldo insuficiente")
        
        else:
            self.saldo -= cantidad
            print("Le queda {self.saldo}")
    
    def agregar_dinero(self, cantidad):

         if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva.")
        
         else:
            self.saldo += cantidad
            print("Tiene {self.saldo}")

    def Transferir_dinero(self, otro_usuario, cantidad):
        
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva.")
        
        if cantidad > otro_usuario.saldo:
            raise ValueError(f"{otro_usuario.nombre} no tiene saldo suficiente para transferir.")
        
        else:
            otro_usuario.saldo -= cantidad
            self.saldo += cantidad
            print(f"{otro_usuario.nombre} transfirió {cantidad}€ a {self.nombre}.")
            print(f"Saldo de {otro_usuario.nombre}: {otro_usuario.saldo}€")
            print(f"Saldo de {self.nombre}: {self.saldo}€")

'''37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras ,
reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro
de la función procesar_texto .'''

def contar_palabras(texto):

    palabras = texto.split()
# funcion que cuenta las palabras de un texto y las pasa a un diccionario, si se repiten suma 1
    contadas = {}

    for palabra in palabras:
        palabra = palabra.lower()
        contadas[palabra] = contadas.get(palabra, 0) + 1
    return contadas

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)
#reemplaza una palabra del dicionario por otra
def eliminar_palabra(texto, palabra_eliminar):
#elimina una palabra del diccionario
    return texto.remove(palabra_eliminar)

def procesar_texto(texto, opcion, *args):  #da a elegir una de las 3 opciones
    funciones = {
        "contar": (contar_palabras, 0),
        "reemplazar": (reemplazar_palabras, 2),
        "eliminar": (eliminar_palabra, 1)
    }

    if opcion not in funciones:
        raise ValueError("Opción no reconocida. Use: 'contar', 'reemplazar' o 'eliminar'.")

    func, num_args = funciones[opcion]
    if len(args) != num_args:
        raise ValueError(f"La opción '{opcion}' requiere {num_args} argumentos.")

    return func(texto, *args)


'''38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.''' 

hora_entrada = input("Introduce una hora (0-23): ")


hora = int(hora_entrada)

if hora < 0 or hora > 23:
        print("La hora debe estar entre 0 y 23.")
elif 6 <= hora < 12:
        print("Es por la mañana")
elif 12 <= hora < 20:
        print("Es por la tarde")
else:
        print("Es de noche")


'''39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
Las reglas de calificación son:
- 0 - 69 insuficiente
- 70 - 79 bien
- 80 - 89 muy bien
- 90 - 100 excelente'''


nota = input("Introduce una nota (0-100): ")


nota = int(nota)

if nota < 0 or hora > 100:
        print("La nota debe estar entre 0 y 100") 
elif 0 <= hora < 69:  
        print("Es insuficiente")
elif 70 <= hora < 79:
        print("Está bien")
elif 80 <= hora < 89:
        print("Está muy bien")
else:
        print("Es excelente")

'''40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o
"triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).'''


def calcular_area(figura, datos):

    '''funcion que calcula el area de la figura dada
    
        ponemos las figuras en un condicional y una tupla con los datos de formula del area    
    '''
    if figura == "rectangulo":
        (base, altura) = datos  
        return base * altura

    elif figura == "triangulo":
        (base, altura) = datos  
        return (base * altura) / 2

    elif figura == "circulo":
        (radio,) = datos     
        return 3.1416 * (radio ** 2)

    else:
        return "Figura no válida"
    
    '''41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el
monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo
siguiente: 1. Solicita al usuario que ingrese el precio original de un artículo.
2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor
a cero). Por ejemplo, descuento de 15€.
5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu
programa de Python.'''

def calcular_precio_final():
    try:
        precio_original = float(input("Ingrese el precio original del artículo (€): "))

        if precio_original <= 0:
            print("El precio debe ser mayor a 0.")
            return

        tiene_cupon = input("¿Tiene un cupón de descuento? (sí o no): ").strip().lower()

        if tiene_cupon == "sí" or tiene_cupon == "si":
            valor_cupon = float(input("Ingrese el valor del cupón de descuento (€): "))

            if valor_cupon > 0:
                precio_final = precio_original - valor_cupon
                if precio_final < 0:
                    precio_final = 0  # No puede quedar negativo
                print(f"Descuento aplicado: {valor_cupon} €")
                print(f"Precio final: {precio_final:.2f} €")
            else:
                print("El valor del cupón debe ser mayor que 0. No se aplicará descuento.")
                print(f"Precio final: {precio_original:.2f} €")
        
        elif tiene_cupon == "no":
            print("No se aplicará ningún descuento.")
            print(f"Precio final: {precio_original:.2f} €")
        
        else:
            print("Respuesta inválida. Debe responder 'sí' o 'no'.")

    except ValueError:
        print("Por favor, introduzca valores numéricos válidos.")


calcular_precio_final()

