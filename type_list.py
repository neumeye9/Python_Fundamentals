#Type List - given a list, test each item's data type. Concatenate string onto a new string.  If it's a number, add it to a running sum. 
# At the end of your program, print the string, the number, and an analysis of what the array contains.

l = ['magical unicorns',19,'hello',98.98,'world']

def typeList(l):
    count = 0
    streval = 'String:'
    sum = 0
    y = []

    for i in range(0,len(l)):
        if(isinstance(l[i],str) == True):
            streval = streval + " " +l[i]
            count += 1
            y.append('String Type')
        elif(isinstance(l[i],int) == True):
            sum += l[i]
            count +=1
            y.append('Integer Type')
        elif(isinstance(l[i],float) == True):
            sum+= l[i]
            count += 1
            y.append('Float Type')
        

    #print y
    print streval
    print sum

typeList(l)





        

    

