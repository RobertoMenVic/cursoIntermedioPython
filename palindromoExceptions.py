def run(string):
    try:
        if len(string)<=0:
            raise ValueError("No puedes agregar una cadena vacía")

        return string==string[::-1]
    except ValueError as ve:
        print(ve)
        return False
        
        

if __name__=="__main__":
    try:
        print(run(''))
    except TypeError as te:
        print("Debes ingresar una cadena o palabra")
        print(te)




    
    """print("Evaluar si la palabra es palindromo o no")
    msj=str(input("Ingresa la palabra:"))
    if msj.isalpha():
        print(run(msj))
    else:
        print("El dato no es alfabetico")"""