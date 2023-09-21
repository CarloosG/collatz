#CODIGO 2202148

def collatz(N):
    suma = 0
    for i in range (N):
        num = int(input("Ingrese un numero "))
        suma = num+ suma
    prom = suma/11
    print("Secuencia de collatz del numero " + str(prom))
    while prom != 1 : 
        if prom%2 == 0:
            prom = prom/2
            print(prom) 
        else:
            prom = prom*3 + 1
            print(prom)
    print(prom)

if "__main__" == __name__:
    collatz(11)