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