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
 