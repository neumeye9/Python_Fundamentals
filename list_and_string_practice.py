
#Find and replace
'''
words = "It's thanksgiving day. It's my birthday, too!"
val = 'day'
newval = 'month'

print words.find(val)

print words.replace(val, newval)
''' 

#Min and Max

'''
x = [2,54,-2,7,12,98]

def minAndMax(x):
    min = x[0];
    max = x[0];

    for i in range(0, len(x)):
        if x[i] > max:
            max = x[i]
        if x[i] < min:
            min = x[i] 
    print min, max

minAndMax(x)

'''
#First and Last - print first and last value in given array:

'''
x = ["hello",2,54,-2,7,12,98,"world"]

first = x[0]
last = x[len(x)-1]

print first,last
'''

#first and Last - creat new list containg the first and last value in the orginal list

'''
x = ["hello",2,54,-2,7,12,98,"world"]

first = x[0]
last = x[len(x)-1]

arrnew = [first,last]
print arrnew
'''

#New List - Sort given list

'''
x = [19,2,54,-2,7,12,98,32,10,-3,6]

x.sort()
print x
'''

#New List - split sorted list in half

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x

b = x[:len(x)/2]
c = x[len(x)/2:]

x = [[b], c]

print x


