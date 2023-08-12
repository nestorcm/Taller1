## programa calculadora

def main():

    print( "Programa calculadora" )
    op= input( """¿Que operacion desea realizar? 
            suma +
            resta -
            multiplicacion * 
            division / 
            salir 0
            ingrese operacion :""")
    
    def suma(a,b):
        total= a+b
        print( "resultado: "+total)
    
    def resta(a,b):
        total= a-b
        print( "resultado: " + total)

    def multiplicacion(a,b):
        total= a*b
        print( "resultado: " + total)

    def division(a,b):
        total= a/b
        print( "resultado: " + total)
    
    while op !="0":
        a=int( input("Ingrese numero 1 :"))
        b=int( input("Ingrese el numero 2 :"))
        if op=="+":
            suma(a,b)
        elif op =="-":
            resta(a,b)
        elif op=="*":
            multiplicacion(a,b)
        elif op=="/":
            division(a,b)
        elif op=="0":
            break
        op= input( """¿Que operacion desea realizar? 
        suma +
        resta -
        multiplicacion * 
        division / 
        salir 0
        ingrese operacion :""")
    
if __name__ == "__main__":
    main()