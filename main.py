import random
import os

##Line break for questions file code
q_file = open("questionsfile.txt")
question = q_file.readlines()
theq = []

for i in question:
    theq.append(i)

new_theq = [x[:-1] for x in theq]

##Line break/whatever you call this for the new code

txt_file = open("revised.txt")
all_the_lines = txt_file.readlines()
empty = []

for i in all_the_lines:
    empty.append(i)

new_empty = [x[:-1] for x in empty]
##newempty is the list essentially, does it work?

queued = "?"

bullet = "\n"
## This here lays the foundation for the sentence
## Make another deff function and have it turned into a question

def foundation():
	return random.choice(new_theq) + " " + random.choice(new_empty)

def questiond():
    return foundation() + queued

def linedup():
    return questiond() + bullet

def main():
    number = int(input("Enter the number of sentences: "))
    sampl = open('tes.txt', 'w')
    for count in range(number):
        print(linedup(), file=sampl)





## I have zero idea what this does

if __name__ == "__main__":
    main()