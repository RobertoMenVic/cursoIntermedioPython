import json
def run ():
    my_list=[1,"Hello",True,4.5]
    my_Dic={"firname":"Roberto", "lastname":"Mendoza"}

    super_list=[
        {"firname":"Jose", "lastname":"Mendoza"},
        {"firname":"Mario", "lastname":"Mendez"},
        {"firname":"Fermin", "lastname":"flores"},
    ]

    super_dic={
        "natural_nums":[1,2,3,4,5],
        "integer_nums":[-2,-1,0,1,2],
        "floating_nums":[2.0,3.3,4.3,5.9]
    }

    for key,value in super_dic.items():
        print(key," - ", value)

    for value in super_list:
        print(json.dumps(value, sort_keys=False, indent=1))


def addNumsNaturalAlCuadra():
    list_nums=[]
    list_numAlCuadra=[]

    for a in range(1,101,1):
        numAlCuadra=a*a
        list_nums.append(a)
        list_numAlCuadra.append(numAlCuadra)
    
    print("Lista de numero naturales al 100")
    print(list_nums)
    print("Lista de numero naturales al cuadrado de los primeros 100 numeros")
    print(list_numAlCuadra)

    addNumsQueNoSeanDivisiblesEntre3(list_numAlCuadra)

def addNumsQueNoSeanDivisiblesEntre3(lista):
    listaDiviEntre3=[]
    for a in lista:
        if a%3!=0:
            listaDiviEntre3.append(a)
    
    print("Lista con numeros que no son divisibles entre tres")
    print(listaDiviEntre3)


def listaMultiplos():
    listaDeMulti=[i for i in range(1,99999) if i%4==0 and i%6==0 and i%9==0]

    print("Lista de multiplos")
    print(listaDeMulti)


if __name__=="__main__":
    run()
    addNumsNaturalAlCuadra()
    listaMultiplos()