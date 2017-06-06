#Part I

def drawStars(arr):
    print arr
    arrnew = []

    for i in range(0,len(arr)):
        num = arr[i]/1
        print num


def multiplyforStars(arr,num):
    for i in range(len(arr)):
        arr[i] = arr[i] / num
    return arr

multiplyforStars([2,4,10,16], 1)

def drawStars(arr):
    print arr
    new_array = []
    for x in arr:
        val_arr = []
        for i in range(0,x): 
            val_arr.append('*')
        new_array.append(val_arr) #puts list val_arr inside new_array []
    return new_array

x = drawStars(multiplyforStars([2,4,10,16],1))
print x #Runs the Multiply function to get a new arr = i.e. [6,2,15]



#Part II - Allow list containing integers and strings to be passed to the drawStars function. A string display the first letter of the string.

def multiplyforStarsTwo(arr):
    for i in range(len(arr)):
        if(isinstance(arr[i],str) == True):
           print (arr[i][0] * (len(arr[i]))).lower() 
            
        elif(isinstance(arr[i],int) == True):
            print arr[i]*('*')
       
multiplyforStarsTwo([4,"Tom",1,"Michael",5,7,"Jimmy Smith"])


