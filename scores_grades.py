
def scoresAndGrades():

    print "Scores and Grades"
    for i in range(1,11):
        import random
        grade = random.randint(0,51)+50
        #print grade

        if(grade < 60):
            print "Score:" + str(grade) + "; You failed and must retake the exam!"
        elif(grade < 70):
            print "Score:" + str(grade) + "; Your grade is D."
        elif(grade < 80):
            print "Score:" + str(grade) + "; Your grade is C."
        elif(grade < 90):
            print "Score:" + str(grade) + "; Your grade is B."
        elif(grade <= 100):
            print "Score:" + str(grade) + "; Your grade is A."
    print "End of the program. Bye!"

scoresAndGrades()
