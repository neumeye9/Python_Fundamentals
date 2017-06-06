word_list = ['hello','world','my','name','is','Anna']
sub = '0' #just change value of sub to whatever you want to find in each string, can be a letter or another string

new_list = [s for s in word_list if sub in s]
print new_list
