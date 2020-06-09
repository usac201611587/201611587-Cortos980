
def collatz(n): # Funcion para determinar la secuencia collatz
    while(n>1): # verifica si no se ha llegado a la unidad ya que esa es la muestra que se termino la secuencia de collatz
        if(n%2==0):# verificamos que el numero si es par
            n //= 2 # como es par dividimos en 2
        else: # como no es par quiere decir que es impar 
            n = (n*3)+1 # multiplicamos por 3 y luego le sumamos 1
        lista.append(n) # luego lo agregamos a la lista


fileName='collatz.txt'  # Aqui le damos el nombre al archivo que queres escribir
archivo = open(fileName,'w') # lo abrimos y le decimos que en modo escritura

Carnefinal=587 # final de mi carne 201611587

lista = [] # una lista para ir guardando los datos
for i in range(2,(Carnefinal+1)): # este ciclo nos sirve para recorrer desde el numero 2 hasta el 587
    lista.append(i)# Agregamos a la lista el numero que se le va a sacar la secuencia
    collatz(i) # le mandamos a la funcion collatz el numero para iniciar la secuencia
    print(lista) # Cuando regresa de la funcion imprimimos la lista para verificar en consola
    archivo.write(str(lista)+'\n') # luego escribimos linea por linea y le mandamos la lista con los valores
    del lista[:]# limpiamos la lista
archivo.close() # cuando se cumple el ciclo for hemos terminado el programa asi que cerramos el archivo


