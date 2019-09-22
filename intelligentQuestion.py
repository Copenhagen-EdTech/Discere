### This script takes a string that defines the subject, 
### and prompts back a question for the user to explain.

from random import randint
#from X import X as subject

# ## Defining vocabularies
# vocab = "abcdefghijklmnopqrstuvwxuz"
# vowls = "aeiouy"
# consonants = "bcdfghjklmnpqrstvwxz"

## Defining predetirmined questions in dictionary
QD ={1:"Can you elaborate on _?_",
     2:"Please explain _?_",
     3:"What do you mean by _?_",
     4:"could you further describe _?_"}

#S = "the spanish inquisition"

## Function that takes a given string input, checks for 
def firstQuestionMaker(subject):
    Q = QD[randint(1,len(QD))] # Selects one of the questions at random
    question = Q.replace("_?_", subject)
    
    return question
