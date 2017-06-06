#Pat I - create a program that outputs the students' first and last names

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def studentNames(dict):
    for i in range(0,len(students)):
        print students[i]['first_name'], students[i]['last_name']

studentNames(students)

#Part II - given the dictionary users, create a program that prints in a format where the list is numbered at the front of the line
#and the number of characters in their first and last name is at the end of the line

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

for user in users:
    #print user
    #print users[user]
    count = 0
    for thing in users[user]:
        #print thing
        #will show all objects in a list
        count += 1
        number = len(thing['first_name']) + len(thing['last_name'])
        #print thing['first_name']
        print '{} - {} {} - {}'.format(count,thing['first_name'].upper(),thing['last_name'].upper(), number)
