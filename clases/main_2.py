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
