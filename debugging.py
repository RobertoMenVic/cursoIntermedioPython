def run():
    divisor= lambda num: [i for i in range(1,num+1) if num%i==0]
    print("Los numeros son:"+str(divisor(int(input("Ingresa un numero:")))))

if __name__=="__main__":
    run()
