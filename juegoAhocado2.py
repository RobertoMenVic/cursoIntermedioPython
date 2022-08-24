import random
import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def leerArchivo(nivel):
    try:
        with open("./archivos txt/data.txt",mode="r", encoding="utf-8") as f:
            listPalabra=[palabra for palabra in f]
            juego(listPalabra,nivel)
    finally:
        f.close()       

def juego(lista,nivel):
    palabra=lista[random.randint(0,170)] 
    print(palabra)
    palabraOculta=["_" for i in range(len(palabra)-1)]
    palabOcultaEnCadena="".join(palabraOculta)
    oportu=0
    
    if nivel==1:
        oportu=len(palabra)+10000
        msjNivel="################ Nivel 1 ##############"
    if nivel==2:
        oportu=len(palabra)+10
        msjNivel="################ Nivel 2 ##############"
    if nivel==3:
        oportu=len(palabra)+5
        msjNivel="################ Nivel 3 ##############"
    
    while palabra.strip()!=palabOcultaEnCadena and not oportu==0:
            print(msjNivel)
            oportuEtiqueta=oportu
            print("Tienes "+str(oportuEtiqueta)+" oportunidades")
            print("La Palabra tienen "+str(len(palabra.strip()))+" letras")
            print(palabOcultaEnCadena)
            oportu-=1
            try:
                letra=input("Ingresa Letra:")
                if letra.isdigit():
                    raise ValueError("Debes agregar una letra")
                for e in range(len(palabra)-1):  
                    if palabra[e]==letra:
                        palabraOculta[e]=letra
                palabOcultaEnCadena="".join(palabraOculta)
                clearConsole()
            except ValueError as ve:
                print(ve)
    if oportu==0:
        print("No lo lograste suerte para la proxima!!!!")
        print("La palabra era:"+ palabra ) 
        mensaje(2)
    if palabra.strip()==palabOcultaEnCadena:
        print("La palabra es: ¡"+palabra.strip()+"!!!!")    
        print("Lo lograste en "+ str(oportu)+ " Intentos") 
        mensaje(3)
def mensaje(valor):
    template = """
**  **    ***    **   **  *******   **      **    ***    **   **  
**  **   ** **   ***  **  **        ***    ***   ** **   ***  **  
******   *****   **** **  **  ***   ****  ****   *****   **** **  
**  **  **   **  ** ****  **   **   ** **** **  **   **  ** ****  
**  **  **   **  **  ***  *******   **  **  **  **   **  **  ***  
        ||===================
        ||                            
        ||                            
        ||                            
        ||                            
        ||                            
        ||                            
        ||                            
        ||                            
        ||                            
        ||                            
        ||                            
        ==========@          ======== 
        ||                         || 
        ||                         || 
        ||                         || 
        """
    template2 = """
**  **    ***    **   **  *******   **      **    ***    **   **  
**  **   ** **   ***  **  **        ***    ***   ** **   ***  **  
******   *****   **** **  **  ***   ****  ****   *****   **** **  
**  **  **   **  ** ****  **   **   ** **** **  **   **  ** ****  
**  **  **   **  **  ***  *******   **  **  **  **   **  **  ***  
        ||===================
        ||                |                         
        ||                |          
        ||                |          
        ||                |          
        ||               ( )          
        ||                |          
        ||               /|\          
        ||              / | \         
        ||                |          
        ||               / \         
        ||              /   \        
        ==========@           ======= 
        ||                         || 
        ||                         || 
        ||                         || 
        """
    template3 = """
**  **    ***    **   **  *******   **      **    ***    **   **  
**  **   ** **   ***  **  **        ***    ***   ** **   ***  **  
******   *****   **** **  **  ***   ****  ****   *****   **** **  
**  **  **   **  ** ****  **   **   ** **** **  **   **  ** ****  
**  **  **   **  **  ***  *******   **  **  **  **   **  **  ***  
        ||===================
        ||                                         
        ||                          
        ||                          
        ||                          
        ||                      ( )          
        ||                     \ | /        
        ||                      \|/          
        ||                       |          
        ||                       |          
        ||                      / \         
        ||                     /   \        
        ==========@           ======= 
        ||                         || 
        ||                         || 
        ||                         || 
        """
    if valor==1:    
        print(template)
    if valor==2:
        print(template2)
    if valor==3:
        print(template3)

def menu():
    mensaje(1)
    mensajeInici="""
        Selecciona el nivel de Juego.
        Preciona 1-----Facíl
        Preciona 2-----Medio
        Preciona 3-----Difícil
    """
    print(mensajeInici)
    nivel=int(input("Ingresa una opción:"))
    leerArchivo(nivel)

def run():
    menu()

if __name__=="__main__":
    run()
