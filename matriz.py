def inicio():
    print("--------------MENU--------------------")
    elegir=int(input("Ingrese las Opciones: \n 1--sumar \n 2--restar \n 3--multiplicar \n 4--warsall \n 5--transapuesta \n 0--Salir"))
    while elegir!=0:
        matriz(elegir)
        elegir=int(input("Ingrese las Opciones: \n 1--sumar \n 2--restar \n 3--multiplicar \n 4--warsall \n 5--transapuesta \n 0--Salir"))
def mostrarMatrices(row,cols,matriz):
    #print("-----------------------Matriz-------------------------------")
    for i in range(0,row):
        for j in range(0,cols):
            print(matriz[i][j],end=" ")
        print()
def inicializarMatriz(row,cols,matriz):
    for i in range(row):
        matriz.append(["-"]*cols)
    print("-----------Matriz1 inicilaizada------------")
    mostrarMatrices(row,cols,matriz)#imprime la matriz 1
    #inicializa la matriz2 con 0
def llenarMatriz(row,cols,matriz):
    for i in range(0,row): #bucle para pedir al usuario que llene la matriz1
        for j in range(0,cols):
            mostrarMatrices(row,cols,matriz)        
            matriz[i][j]=int(input("ingrese un elemento"))#el usuario ingresa un elemento de la matriz
            
    mostrarMatrices(row,cols,matriz)
        
def matriz(x):
    print("----------------Welcome--------------")
    matriz1=[]
    matriz2=[]
    matriz3=[]
    
    if x==1 or x==2 or x==3:
        row=int(input("ingrese la fila"))
        cols=int(input("ingrese las columna"))
        fila=int(input("ingrese las fila"))
        columna=int(input("ingrese las columna"))
    

        inicializarMatriz(row,cols,matriz1)
        inicializarMatriz(fila,columna,matriz2)
        inicializarMatriz(row,columna,matriz3)
        print("llene los elementos")
        print("---------Matriz1------------")
        llenarMatriz(row,cols,matriz1)
        print("---------matriz2------------")
        llenarMatriz(fila,columna,matriz2)
        if x==1:
            sumaMatrices(matriz1,matriz2,matriz3,row,cols)
        elif x==2:
            restaMatrices(matriz1,matriz2,matriz3,row,cols)
        elif x==3:
            print("multiplicaion")
            multiplicacionMatrices(matriz1,matriz2,matriz3,row,columna,fila)
    elif x==4 or x==5:
        row=int(input("ingrese la fila"))
        cols=int(input("ingrese las columna"))
        inicializarMatriz(row,cols,matriz1)
        print("llene los elementos")
        print("---------Matriz1------------")
        llenarMatriz(row,cols,matriz1)
        print("la matriz  de adiacencia es ")
        if x==4:
             warsall(matriz1,row,cols)
        elif x==5:
            transapuesta(matriz1,row,cols)
def sumaMatrices(matriz1,matriz2,matriz3,row,cols):
    for i in range(0,row):
        for j in range(0,cols):
            matriz3[i][j]=matriz1[i][j] + matriz2[i][j]
    print("-------------la suma es-------------------------------------")
    mostrarMatrices(row,cols,matriz3)
def restaMatrices(matriz1,matriz2,matriz3,row,cols):
    for i in range(0,row):
        for j in range(0,cols):
            matriz3[i][j]=matriz1[i][j] - matriz2[i][j]
    print("----------------------la  resta es-------------------------------------")
    mostrarMatrices(row,cols,matriz3)

'''       
def incializaMatriz(row,cols):   
    print("matrices boolenas ")
    matriz1=[]
    matriz2=[]
    matriz3=[]
    #inicializa la matriz 1 con 0
    for i in range(row):
        matriz1.append([0]*cols)
    print(matriz1)#imprime la matriz 1
    #inicializa la matriz2 con 0
    for i in range(row):
        matriz2.append([0]*cols)
    print(matriz2)#imprime la matriz 2
    for i in range(row):
        matriz3.append([0]*cols)
    print(matriz3)#imprime la matriz 3
def inicializar():
            print("A[",i,",",j,"]")#imprime la posicion
    for i in range(0,row): #bucle para pedir al usuario que llene la matriz1
        for j in range(0,cols):
            matriz1[i][j]=int(input("ingrese un elemento"))#el usuario ingresa un elemento de la matriz
            print(matriz1)
    print("--------------Matriz 2--------------------------------")
    for i in range(0,row):#bucle para pedir al usuario que llene la matriz2
        for j in range(0,cols):
            print("B[",i,",",j,"]")
            matriz2[i][j]=int(input("ingrese los elementos de la matriz"))
            print(matriz2)
 
'''
def multiplicacionMatrices(matriz1,matriz2,matriz3,row,columna,fila):
    for i in range(0,row):
        for j in range(0,columna):
            for k in range(0,row):
                matriz3[i][j]=matriz3[i][j] or (matriz1[i][k] and matriz2[k][j])
    mostrarMatrices(row,columna,matriz3)
def warsall(matriz1,row,cols):
    for i in range(0,row):
        for j in range(0,cols):
            for k in range(0,row):
                if matriz1[i][j] and matriz1[j][k]==1:
                    matriz1[i][k]=1
    mostrarMatrices(row,cols,matriz1)
def transapuesta(matriz1,row,cols):
    cont=0
    for i in range(0,row):
        for j in range(cont,cols):
            temporal=matriz1[i][j]
            matriz1[i][j]=matriz1[j][i]
            matriz1[j][i]=temporal
        cont+=1
inicio()