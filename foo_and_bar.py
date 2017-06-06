def primeIsFoo(min,max):
   
    for i in range(min,max):
        if(max % i) == 0:
            continue
        else:
            print (i,"foo")

primeIsFoo(10,100)