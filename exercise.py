"""
    Módulo Python para ejercicio de comprensión de programas
"""
def insercion(A):
    """
        Entrada: lista de valores
        Salida: lista de valores ordenados
    """
    for i in range(len(A)):
        for j in range(i,0,-1):
            if(A[j-1] > A[j]):
                aux=A[j]
                A[j]=A[j-1]
                A[j-1]=aux
def main():
    """
        Programa principal
    """
    A=[6,5,3,1,8,7,2,4]
    print(A)

    insercion(A)
    print(A)

if __name__ == '__main__':
    main()