## programa calculadora

def main():

    print( "Programa calculadora" )
    print ( """¿Que operacion desea realizar? 
           suma +
           resta -
           multiplicacion * 
           division / 
           salir 0""")
    def suma (a,b):
        total= a+b
        print(total)
    
    suma(5,2)

if __name__ == "__main__":
    main()