import random
def leerArchivo():
    with open("./archivos txt/data.txt",mode="r", encoding="utf-8") as f:
        listPalabra=[palabra for palabra in f]
        posiPalabra=random.randint(0,170)
        palabra=listPalabra[posiPalabra] 
        palabraOculta=[]
        cadena=""
        contador=0
        print("La Palabra tienen "+str(len(palabra.strip()))+" letras")
        #print(palabra)
        palabraOculta=["_" for i in range(len(palabra)-1)]
        cadena="".join(palabraOculta)
        print(cadena)
        
        while palabra.strip()!=cadena:
            contador+=1
            letra=input("Ingresa Letra:")
            for e in range(len(palabra)-1):
                
                if palabra[e]==letra:
                    palabraOculta[e]=letra
            cadena="".join(palabraOculta)
            print(cadena==palabra)
            print(cadena) 
        print("Lo lograste en "+ str(contador)+ " Intentos")      



def run():
    leerArchivo()

if __name__=="__main__":
    run()
