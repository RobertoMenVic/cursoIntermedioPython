from csv import excel


def run(num):
    """divisor= lambda num: [i for i in range(1,num+1) if num%i==0]
    print("Los numeros son:"+str(divisor(int(input("Ingresa un numero:")))))"""
    divisor=[i for i in range(1,num+1) if num%i==0]
    return divisor

def validarDatoIngresado():
    flag=True
    while flag:
        try:            
            num=int(input("Ingresa un numero:"))
            try: 
                if num<=0:
                    raise ValueError("No puedes agregar un numero negativo")
                print(run(num))
                flag=False
            except ValueError as ve:
                print(ve)
                flag=True

        except ValueError:
            print("Debes de ingresar un numero")
            flag=True

if __name__=="__main__":
    validarDatoIngresado()
        
        