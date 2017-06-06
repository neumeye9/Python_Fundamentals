
list_one = ['celery','celery','celery']
list_two = ['celery','celery','celery']

if (list_one == list_two):
    print "The lists are the same"
elif (list_one != list_two):
    print "The lists are not the same"
    
#if the lists need to be place in order first then compared

list_one=[1,3,1,1]
list_two=[3,1,1,1]

list1 = list_one.sort()
list2 = list_two.sort()

if(list1 == list2):
    print "The lists are the same"
elif (list1 != list2):
    print "The lists are not the same"
