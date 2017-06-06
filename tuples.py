#Write a function that takes in a dictionary and returns a list of tuples where the first tuple item is the key and the second is the value. 

# function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
#function output
[("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]

dictionary2 = []

for user in my_dict:
    #print (user, my_dict[user])
    dictionary2.append((user, my_dict[user]))

print dictionary2

    