def run():
    palindromo=lambda cadena: cadena==cadena[::-1]
    print(palindromo('ana'))
    
if __name__=="__main__":
    run()