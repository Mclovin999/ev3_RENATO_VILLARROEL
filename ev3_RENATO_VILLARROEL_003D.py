import time as t
import os 
import random as r

cliente=[]

def limpia_pantalla():
    t.sleep(1)
    print("ESPERE")
    os.system("cls")

def menu():
    print("_________________________________")
    print("1. Registrar de los client@.")
    print("2. Buscar cliente por rut.")
    print("3. Reporte segun renta.")  
    print("4. SALIR.") 
    print("_________________________________")
    opcion=int(input["Seleccione"])
    

def lista_cliente():
    for lista in cliente:
        for cliente in lista:
            print (cliente)

def regisrar():
    while True:
        rut_cliente=input("Ingrese rut del cliente:")
        if (len(rut_cliente)==0) and (len(rut_cliente)<=9) and rut_cliente.isdigit():
            break
        else:
            print("Ingrese un rut valido :(")
    
    while True:

        nom_cliente=input("Ingrese Nombre cliente:\t")
        if (len(nom_cliente)<):
                print("Ingrese nombre(PASO OBLIGATORIO)")
        else:
                break

        proyecto=input("Que proyecto desea ingresar (Vive Santiago = VS, Vive La Florida= VF, Vive nunoa= VN)")
        if proyecto==1:
            nom_proyecto = "VS"
            print("Proyecto Vive Santiago")
            break
            
        elif proyecto==2:
            nom_proyecto= "VF"
            print("Proyecto Vive La Florida")
            break

        elif proyecto==3: 
            nombre_proyecto= "VN"
            print("Proyecto vive Nunoa")
            break
        

        renta_men = r.randrange(400000,99999999)
        cliente[rut,nom_cliente,nom_proyecto,renta_men]
        cliente.append(cliente)
        print("Registro completado.")
        limpia_pantalla
        
        
def buscar(rut_cliente):
    i=1
    for lista in cliente:
        if lista[0] == rut_cliente:
            print(f"Rut: {lista[0]}")
            print(f"Nombre del cliente: {lista[1]}")
            print(f"Proyecto: {lista[2]}")
            print(f"Renta M: {lista[3]}")
            i=0
    
    if==1:
        print("ERROR DE DATOS")
        limpia_pantalla
    print("presione ENTER para continuar")
    m.getch()
    limpia_pantalla


def reporte_ren():
    cont=0
    print("Reporte Renta:")
    for lista in cliente:
        if lista[3]>=900000:
            cont+=1
            print(f"Rut: {lista[0]}")
            print(f"Nombre del Cliente: {lista[1]}")
            print(f"Renta M: {lista[3]}")
            print(f"Proyecto: {lista[2]}")
            
os.system("cls")

#MAIN PROGRAM

while True:
    try:
        opcion=menu()
        
        if opcion==1:
            registrar()
        elif opcion==2:
            while True:
                rut_cliente=input("Ingrese rut:")
                if(len(rut_cliente)==10) and rut_cliente.isdigit():
                    buscar(rut_cliente)
                    break
                else:print("Ingrese un rut valido :(")
                
        elif opcion==3:
            reporte_ren()
            
        elif opcion == 4:
            for i in range(5,0,-1):
                print(f"saliendo")
                limpia_pantalla()
                
            
            