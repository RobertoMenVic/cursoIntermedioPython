from functools import reduce 
def run():
    lista=[2,3,6,8,9,12,23,45,67]
    newList=list(filter(lambda x:x%2==0,lista))
    print(lista)
    print(newList)

def listAlCuadrado_Map():
    myList=[1,2,3,4,5]
    print(myList)
    #myList=[i*i for i in myList]
    myList=list(map(lambda x:x*x,myList))
    print(myList)

def pultiNumerosDeLaList_reduce():
    lista=[2,2,2,2,2,2]
    multiNumeList=reduce(lambda a,b:a*b,lista)
    print(multiNumeList)

def quitarDuplicados():
    lista=[1,2,3,4,3,1,'a','a','b','c','d','c']
    listaSinDuplicado=[i for i in lista if lista.count(i)==1]
    listaSinDupliSet=list(set([i for i in lista if lista.count(i)>1]))
    NewListaSinDuplicados=listaSinDuplicado+listaSinDupliSet
    print(lista)
    print(listaSinDuplicado)
    print(listaSinDupliSet)
    print(NewListaSinDuplicados)

if __name__=="__main__":
    quitarDuplicados()