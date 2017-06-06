#Write a function that simulates tossing a coin 5,000 times. Print how many times the head/tail appears

import random

def coinToss(min,max):

    heads = 0
    tails = 0
    
    for i in range(min,max):
        chance = random.randint(1,2)
        print chance
        
        if(chance == 1):
            heads = heads + 1
            #print heads
            print "Attempt #" + str(i) +":" + " " + "Throwing a coin... It's a head!... Got" + " " + str(heads) + " " + "head(s) so far and" + " " + str(tails) + " " + "tail(s) so far."
        
        elif( chance == 2): 
            tails = tails + 1
            #print tails
            print "Attempt #" + str(i) +":" + " " + "Throwing a coin... It's a tail!... Got" + " " + str(heads) + " " + "head(s) so far and" + " " + str(tails) + " " + "tail(s) so far."

coinToss(1,5001)