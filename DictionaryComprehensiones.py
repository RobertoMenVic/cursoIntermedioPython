import math
def run ():
    myDictionary={i:i**3 for i in range(1,100) if i%3!=0}
    myDicti2={i:round(math.sqrt(i),2) for i in range(1,1001)}
    #print(myDictionary)
    print(myDicti2)
    #myDictionary={}
    #dictionaryAlCuadrado(myDictionary)

#def dictionaryAlCuadrado(dictionary):
    
#   for i in range(1,100):
#      dictionary[i]=i**2
#    print(dictionary)


if __name__=="__main__":
    run()