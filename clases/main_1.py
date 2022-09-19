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