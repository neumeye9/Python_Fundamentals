# Create a function that counts from 1 to 2000 and as you loop, print that number and whether it is even or odd

'''
def oddEven(min,max):


    for i in range(min,max):

        if(i%2 == 1):
            print ( "Number is " + " " + str(i) + ". " + "This is an odd number.")
        elif(i % 2 == 0):
            print ( "Number is" + " " + str(i) + ". " + "This is an even number.")

oddEven(1,2001)
'''

# Multiply - iterate through each value in a list and return a list where each value has been multiplied by 5

a = [2,4,10,16]

def multiply(arr,num):
    for i in range(len(arr)):
        arr[i] *= num
    return arr

multiply([2,4,10,16], 5)


#Hacker Challenge - write a function that takes the multiply function (above) call as an argument. New function should return the 
# multiplied list as a two-dimensional list. Each internal list should containg the number of 1's as the number in the original list

def layered_multiples(arr):
    print arr
    new_array = []
    for x in arr:
        val_arr = []
        for i in range(0,x): 
            val_arr.append(1)
        new_array.append(val_arr) #puts list val_arr inside new_array []
    return new_array

x = layered_multiples(multiply([2,4,5],3))
print x #Runs the Multiply function to get a new arr = i.e. [6,2,15]
