#Multiple:Part 1 - code that prints all the odd numbers from 1 to 1000.

def oddNumbers1to1000():
    for i in range (1, 1000):
        if i % 2 == 1:
            print i

oddNumbers1to1000()

#Multiples:Part 2 - print multiples of 5 from 5 to 1,000,000

def printMultiplesOfFive():
    for i in range(5,1000000):
        if i % 5 == 0:
            print i

printMultiplesOfFive()

#Sum List - prints the sum of all values in a list

a = [1,2,5,10,255,3]

def printSum(a):
    sum = 0
    for i in range(0,len(a)):
        sum += a[i]
    print sum

printSum(a)

#Average List - prints the average of the values in a list

a = [1,2,5,10,255,3]

def printAverage(a):
    sum = 0
    for i in range(0,len(a)):
        sum = sum + a[i]
    print sum / len(a)

printAverage(a)