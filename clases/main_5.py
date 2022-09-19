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