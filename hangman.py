#importing modules
import os                   # module OS
import random               # module random

# define hangman
hg1 = [" ","+","-","-","+"] #  +--+
hg2 = [" ","0"," "," ","|"] #  0  |
hg3 = ["-","|","-"," ","|"] # -|- |
hg4 = ["["," ","]"," ","|"] # [ ] |
hg5 = ["#","#","#","#","#"] # #####

man = ["0","|","-","-","[","]"]

# define program variables
word = ""                   # secret world
temp = []                   # temporal list word
msg = ""                    # screen messages
attempt = 0                 # number of turns

# get countries of the world
f = open("countries.txt","r")
l = []
for line in f:
    line = line.strip() # delete return from end line
    l.append(line)
f.close()

# random a country from the list
word = random.choice(l)

# set underscore in temporal world
# if a space char is found, it is not replace
for c in word:
    if c == " ":
        temp.append(c)
    else:
        temp.append("_")

# clean hangman
hg2[1] = " "
hg3[0] = " "
hg3[1] = " "
hg3[2] = " "
hg4[0] = " "
hg4[2] = " "

# main while loop
while True:
    os.system('clear')      # For Linux/OS X

    # print hangman (list to string)
    print (''.join(hg1))
    print (''.join(hg2))
    print (''.join(hg3))
    print (''.join(hg4))
    print (''.join(hg5))

    # print temporal world
    print("\n" + str(temp) + "\n")
    print(msg)

    # convert temp list to string and verfy word
    s = ''.join(temp)
    if s == word:
        print ("You won")
        break

    # verify attempts
    if attempt == len(man):
        print ("You loose, the secret word was " + word)
        break

    char = input("Choose a character:")
    if len(char) > 1:
        msg = "Please, choose only one character."
    else:
        found = False;      # temporal boolean for messages
        i = 0               # index word
        for c in word:
            if c == char or c == char.title(): # title() for capitalize first letter only
                temp[i] = c
                found = True
            i+=1            # index + 1
        if found:
            msg = "Yeah! good job, go head."
        else:
            # add to hangman
            attempt+=1
            if attempt == 1:
                hg2[1] = man[attempt-1] # print 0
            elif attempt == 2:
                hg3[1] = man[attempt-1] # print |
            elif attempt == 3:
                hg3[0] = man[attempt-1] # print -
            elif attempt == 4:
                hg3[2] = man[attempt-1] # print -
            elif attempt == 5:
                hg4[0] = man[attempt-1] # print [
            elif attempt == 6:
                hg4[2] = man[attempt-1] # print ]

            msg = "Oops, the character " + char + " is not in the word."
