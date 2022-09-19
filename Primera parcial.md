# Fundamentos de programación 
## Actividades de clase primera parcial 

### Clase 1
```python
#CLASE 1


def suma(a,b):
    return a+b
    
def suma2(a:int,b:int):
    return a+b
      
def mensaje(mnsg:str,nombre:str):
    return mnsg + " " + nombre
     
def datos(nombre:str,edad:str):
    return"Hola " + nombre + " tienes " + edad + " años"
    
if __name__=='__main__':
    
    nombre="Paola"
    mnsg="Hola"
    edad="19"
    agea=2022
    ageb=2003
    x=10
    
    print(mensaje(mnsg,nombre))
    print(datos(nombre,edad))
    print(x,":",id(x))
    print(suma(2.5,2.5))
    print(suma2(2,2))
```

### Clase 2
```python
# CLASE 2 

#import sumar as s     #importar funciones de archivos individuales
#import restar as r
#import multiplicar as m 
#import dividir as d 
#import cuadrado as c
#from operaciones import *
#if __name__=="__main__":
   
   #print(sumar(5,5))
   #print(restar(10,2))
   #print(multiplicar(2,2))
   #print(dividir(8,5))
   #print(cuadrado(2))
       
import opc.operaciones as op   #importar funciones de un mismo archivo 

if __name__=="__main__":
    
    print(op.sumar(5,5))
    print(op.restar(10,2))
    print(op.multiplicar(2,2))
    print(op.dividir(8,5))
    print(op.cuadrado(2))
```

### Clase 3
```python
# CLASE 3

#n1=10
#msg="hola"

#print(n1,msg)
#print(str(n1)+msg)
#fstrings
#print(f"{n1} {msg}")

#Hacer una funcion que reciba el nombre de una persona 
#el año de nacimiento y el año actual, retornando el mensaje
#"hola <nombre>, tienes <edad> años"


#def mensaje1(age_a:int,age_b:int,name:str)->str:
#    edad = age_a - age_b
#    return f"Hola {name}, tienes {edad} años"
#   
#def mensaje2(age_a:int,age_b:int,name:str)->str:
#    return f"Hola {name}, tienes {age_a - age_b} años"
#
#def calcular_age(age_a:int,age_b:int)->int:
#    return age_a - age_b
#
#def mensaje3(age_a:int,age_b:int,name:str)->str:
#    return f"Hola {name}, tienes {calcular_age(age_a,age_b)} años"
#    
#    
#
#if __name__=="__main__":
#    
#    print(mensaje1(2022,2003,"Paola"))
#    print(mensaje2(2022,2003,"Kai"))
#    print(mensaje3(2022,2000,"Alex"))
    
#LISTAS 
#from traceback import print_tb
#
#
#alumnos = ["Alex", "Paola", "Sergio","Kai"]
#
#print(f"Alumnos: {alumnos}")
#
#for i in range(len(alumnos)):
#    print(f"Alumnos: {alumnos[i]}")
#
##TUPLAS
#alumnos = ("Alex", "Paola", "Sergio","Kai")
#
#print(f"Alumnos: {alumnos}")
#
#for i in range(len(alumnos)):
#    print(f"Alumnos {i+1}: {alumnos[i]}")
#
##SETS
#alumnos = {"Alex", "Paola", "Sergio","Kai"}
#
#print(f"Alumnos: {alumnos}")
#

#DICCIONARIOS
#alumnos = {"Nombre": "Paola", "Materia1":10, "Materia2":5}  #NO FUNCIONO 
#
#print(f"Alumnos: {alumnos}")
#print(f"Alumno: {alumnos['nombre']}")
#
#numeros_list = [1,2,5,7,1,2,5,4,7,5,1,5,7,2]
#numeros_set = {1,2,5,7,1,2,5,4,7,5,1,5,7,2}
#
#print(numeros_list)
#print(numeros_set)

e = ["Nombre", "Est Dt", "Prog Func", "Ingles"]
alumnos = ["Alex", "Paola", "Sergio","Kai"]
m_e_d = [8,7,5,9]
m_p_f = [5,10,9,7]
m_i = [6,5,9,10]

ancho = 12
print(f"{e[0]:^{ancho}}{e[1]:^{ancho}}{e[2]:^{ancho}}{e[3]:^{ancho}}")
for i in range(len(alumnos)):
    print(f"{alumnos[i]:^{ancho}}{m_e_d[i]:^{ancho}}{m_p_f[i]:^{ancho}}{m_i[i]:^{ancho}}")
```

### Clase 4
```python
# CLASE 4

h = ["Nombre", "Est Dt", "Prog Func", "Ingles"]
al = ["Alex", "Paola", "Sergio","Kai"]
m1 = [8,7,5,9]
m2 = [5,10,9,7]
m3 = [6,5,9,10]

def reporte(fmt:int):
    print(f"{h[0]:^{fmt}}{h[1]:^{fmt}}{h[2]:^{fmt}}{h[3]:^{fmt}}")
    for i in range(len(al)):
        print(f"{al[i]:^{fmt}}{m1[i]:^{fmt}}{m2[i]:^{fmt}}{m3[i]:^{fmt}}")
        
if __name__=="__main__":
    reporte(12)

#separacion con comas 
numeroBig = 59568465574565416
print(f"{numeroBig:,d}")

#fijar cantidad de decimales 
numeroPI = 3.141592678547858965865
print(f"{numeroPI:.4f}")

#notacion cientifica
numeroPI2 = 314.292481548646
print(f"{numeroPI2:e}")
print(f"{numeroPI2:.2e}")

#porcentajes
numero_porciento = 0.96986318 #solo con numeros menores a cero 
print(f"{numero_porciento:%}")
print(f"{numero_porciento:.2%}")

#numeros binarios
print(f"{458:b}")

#unicodes
print(f"{65:c}")

##hexadecimal
print(f"{15:x}")

##octal
print(f"{255:o}")

def tabla_mul(n1,n2,fmt):
    for i in range(n2):
        print(f"{n1:^{fmt}}x{i+1:^{fmt}}= {n1*(i+1):^{fmt}}")
        
if __name__=="__main__":
    tabla_mul(1,5,5)
```

### Clase 5
```python
# CLASE 5

#lista1 = [1,2,3,4]
#print(lista1)
#lista2 = [1,3.14,"s",True,[4,5,7,4],(0,0,0),{8,9,"a",9.3}]
#print(lista2)
#
#print(len(lista1))
#print(len(lista2))
#print(lista2[6]) #recorrer la lista de izquierda a derecha por medio del indice positivo 
#
#lista_cal = []
#lista_cal.append(5)
#print(lista_cal)
#lista_cal.append(9)
#print(lista_cal)
#lista_cal.insert(0,3) #primer numero posicion, segundo elemento que se agrega 
#print(lista_cal)
#
##rellener una lista con los primeros numero del 1 al 10
#
#list_num = []
#for i in range(1,11):
#    list_num.append(i)
#    
#print(list_num)
#
#print(lista1[-2]) #recorrer la lista de derecha a izquierda por medio de los indices negativos 
#
##slices (rebanadas)
#lista1 = [1,2,3,4,5,6,7,8,9,10]
#print(lista1[:]) #imporpir de un punto a otro (inicio/fin) se puede especificar 
#print(lista1[3:10])
#print(lista1[int (len(lista1)/2):])
#print(lista1[:int (len(lista1)/2)])
#print(lista1[3:7]) #positivos
#print(lista1[-7:-3]) #negativos 

#lista1 = [1,"dos",3,"cuatro"]
#lista2 = lista1
#print("Modoficar una lista de forma incorrecta\n")
#print(f"lista 1: {lista1}")
#print(f"lista 2: {lista2}")
#lista1[1] = 2 #se destruye la copia de la lista 
#print("-----------------")
#print("Ambas se modifican y tienen la misma direccion de memoria\n")
#print(f"lista 1: {lista1}")
#print(f"lista 2: {lista2}")
#print(f"direccion 1: {id(lista1)}")
#print(f"direccion 2: {id(lista2)}")
#print("-----------------")
#
##forma correcta para que no se modifiquen ambas listas 
#print("\nForma correcta\n")
#lista1 = [1,"dos",3,"cuatro"]
#lista2 = lista1[:]
#print(f"lista 1: {lista1}")
#print(f"lista 2: {lista2}\n")
#lista2[1] = 2
#print("Lista 2 modificada, lista 1 sin cambios\n")
#print(f"lista 1: {lista1}")
#print(f"lista 2: {lista2}")
#print(f"direccion 1: {id(lista1)}")
#print(f"direccion 2: {id(lista2)}")

lista1 = [0,1,2,3,4]
lista2 = [5,6,7,8]
lista1[len(lista1):] = lista2
print("agregar varios elementos en una lista\n")
print(lista1)
print(lista2)
print("------------")
lista1[:0] = lista2
print(lista1)
lista1[:-5] = lista2
print(lista1)
print("\n----------------------")
lista1.append(lista2) #lista dentro de una lista
print(lista1)
#con append no se suman las listas, mejor usar extend
lista1.extend(lista2)
print(lista1)

#eliminar un elemento 
del(lista1[0])
print(lista1)
#borrar por slices
del(lista1[2:5]) #de la posicion inicial hasta n-1
print(lista1)
```

### Clase 6
```python
def suma(a=0,b=0,c=1): #se pueden inicializar las variables según sea 
    return (a+b)/c      #necesidad de la funcion 

print(suma(b=9))  #no afecta el orden o si no se colocan todos los parametros
```

## Archivos importados en la clase 2
### Suma
```python
def sumar(a:int|float,b:int|float):
    return a+b
```

### Resta
```python
def restar(a:int|float,b:int|float):
    return a-b
```

### Multiplicacion
```python
def multiplicar(a:int|float,b:int|float):
    return a*b
```

### Division
```python
def dividir(a:float,b:float):
    return a/b
```

### Cuadrado
```python
def cuadrado(a:int|float):
    return a*a
```

### Operaciones 
```python
def sumar(a:int|float,b:int|float):
    return a+b

def restar(a:int|float,b:int|float):
    return a-b

def multiplicar(a:int|float,b:int|float):
    return a*b

def dividir(a:float,b:float):
    return a/b

def cuadrado(a:int|float):
    return a*a
```
