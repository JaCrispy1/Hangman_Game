# Coding Challenge 3, hangman.py
# Name:Gaurav Thapaliya
# Student No:2059614
# Hangman Game

import random
import string
import os

WORDLIST_FILENAME = "words.txt"

#=========Responses to in-game events===============
#=========Use the format function to fill in the spaces=========
responses = [
    "I am thinking of a word that is {0} letters long",
    "Congratulations, you won!",
    "Your total score for this game is: {0}",
    "Sorry, you ran out of guesses. The word was: {0}",
    "You have {0} guesses left.",
    "Available letters: {0}",
    "Good guess: {0}",
    "Oops! That letter is not in my word: {0}",
    "Oops! You've already guessed that letter: {0}",
]

#======Choosing a random word from those available in the wordlist and returning them====
def choose_random_word(all_words):
    
    
    return random.choice(all_words)



#========Generate a list of valid words and retrns a list of valid words==============
def load_words():
   
    inFile=open(WORDLIST_FILENAME,"r")
    all_words=inFile.read().split()
    inFile.close()
    
    return all_words
    

#=========Load the list of words into the variable wordlist==========
# ========Accessible from anywhere in the program===================
# ========you have implemented the load_words() function============
def is_word_guessed(word, letters_guessed):
    """
    Determine whether the word has been guessed

    Args:
        word (str): the word the user is guessing
        letters_guessed (list): the letters guessed so far
    
    Returns: 
        boolean, True if all the letters of word are in letters_guessed; False otherwise
    """
    
    if letters_guessed in word:
        used_letters.append(letters_guessed)
        get_remaining_letters(used_letters)
        return True
    else:
        used_letters.append(letters_guessed)
        get_remaining_letters(used_letters)
        return False



def get_guessed_word(word, letters_guessed):
    """
    Determines the current guessed word, with underscores

    Args:
        word (str): the word the user is guessing
        letters_guessed (list): which letters have been guessed so far
    
    Returns: 
        string, comprised of letters, underscores (_), and spaces that represents which letters have been guessed so far.
    """

    if len(text)==0:
        for char in word:
            if letters_guessed==char:
                text.append(letters_guessed)
            else:
                text.append("_")

    else:
        i=0
        for m in word:
            if letters_guessed==m:
                text[i]=m
            i+=1
            
    return text


def get_remaining_letters(letters_guessed):
    """
    Determine the letters that have not been guessed
    
    Args:
        letters_guessed: list (of strings), which letters have been guessed
    
    Returns: 
        String, comprised of letters that haven't been guessed yet.
    """
    all_chars = list('abcdefghijgklmnopqrstuvwxyz')
    
   
    
    remaining_letters = sorted(list(set( all_chars ) - set( letters_guessed )))
    

  
    return remaining_letters



#=============Getting score and returning rank==============
def get_score():
    
    rank={}

    if not os.path.isfile("scores.txt"):
        display="Score does not exists"
        return display
        
    else:
        point=open("scores.txt","r")
        for lines in point:
            ln=lines.strip("\n").split(" ")
            score=ln[0]
            name=ln[1]
            rank.update({name:score})
        return rank
    



#==========Saving score in a file=========================
def save_score(name, score):
    lst=[]
    while True:
        if os.path.isfile("scores.txt")==True:
            if not os.stat("scores.txt").st_size == 0:
                file=open("scores.txt","r")
                lines=file.readlines()
                for line in lines:
                    stripped=line.strip("\n")
                    previous_score,previous_name=stripped.split(" ")
                    if name==previous_name:
                        if score>=int(x_score):
                            rev=str(score)+" "+name
                            lst.append(re)
                    else:
                        striped=line.strip("\n")
                        lst.append(striped)
                        re=str(score)+" "+name  
                        if re not in lst:
                            re=str(score)+" "+name    
                            lst.append(re)
            else:
                file=open("scores.txt","w")
                re=str(score)+" "+name
                file.write(re)
                file.write("\n")
                lst.append(re)
                
                
            break
        else:
            file=open("scores.txt","w")
            re=str(score)+" "+name
            file.write(re)
            file.write("\n")
            lst.append(re)
            
    file=open("scores.txt","w")
    for m in lst:
        file.write(m)
        file.write("\n")
        
    file.close()

        
wordlist = load_words()
print("Loading words..")
print(len(wordlist))
print("Welcome to Hangman Ultimate Edition")



empty_word=[]
text=[]
used_letters=[]
rounds=[0]
random_letters=[]



#====================Interactive game of Hangman========================
def hangman(word):
    
    hang_m=False
    attempts=6
   
#==============Choose to play, view the leaderboard or quit===============
    while True:
        ask=str(input("Do you want to Play (p) view the leaderboard (l) or quit (q):").lower())

        if ask!="p" and ask!="l" and ask!="q":
            print("Invalid Input.Please check again !")
        else:
            break

#=====================User name and checking valid inputs===================
    if ask=="p":
        print("------------")
        print("Please provide your full name:")
        while True:
            user_name=str(input("What is your name?").lower())
            if user_name=="":
                print("Invalid Input.Please check again !")
            else:
                break
        print( "I am thinking of a word that is {0} letters long".format(len(word)))
        print("------------")


#=================Game User Interface==============================
        while not hang_m:
            print("You have {0} guesses left.".format(attempts))
            print("Available letters: {0}".format(get_remaining_letters(used_letters)))
            while True:
                guessed_letter=str(input("Please guess a letter:").lower())
                if len(guessed_letter)>1 or guessed_letter==" " or guessed_letter=="":
                    print("This is Invalid")
                else:
                    break
                
            if guessed_letter not in used_letters:
                if is_word_guessed(word, guessed_letter)==True:
                    get_guessed_word(word, guessed_letter)
                    print("Good guess: {0}".format(" ".join(text)))
                    print("------------")
                    


#======================When player wins the game===========================
                    if "".join(text)==word:
                        print("Congratulations, you won!")
                        score=len(word)*attempts
                        print("Your total score for this game is:{}".format(score))
                        random_letters.append(word)
                        hang_m=True
                        rounds[0]+=1
                        if rounds[0]>0:
                            empty_word.clear()
                            text.clear()
                            used_letters.clear()
        
                        loop=True
                        while loop:
                            end_input=str(input("Would you like to save your score(y/n):").lower())
                            if end_input !="y" and end_input !="n":
                                print("Invalid Input.Please check again !")
                            else:
                                loop=False
                            if end_input=="y":
                                save_score(user_name,score)
                                print("------------")
                                choose=str(input("Would you like to restart?(y/n)").lower())
                                if choose=="y":
                                    word = choose_random_word(wordlist)
                                    hangman(word)
                                else:
                                    print("Thanks for playing, goodbye!")
                            else:
                                choose=str(input("Would you like to restart?(y/n)").lower())
                                if choose=="y":
                                    word = choose_random_word(wordlist)
                                    hangman(word)
                                else:
                                    print("Thanks for playing, goodbye!")
                                
                        
                       
# ============================If the player guesses wrong ================== 
                else:
                    if not text:
                        print("Oops! That letter is not in my word: {0}".format(" ".join(empty_word)))
                        print("------------")
                    else:
                        print("Oops! That letter is not in my word: {0}".format(" ".join(text)))
                        print("------------")
                    vowels="a e i o u"
                    if guessed_letter in vowels:
                        attempts-=2
                    else:
                        attempts-=1  

# ===========================If the player repeats the guess===============
            else:
                print("Oops! You've already guessed that letter: {0}".format(" ".join(text)))
                print("------------")
                


# ======================When the player loses the game====================
            if attempts<=0:
                random_letters.append(word)
                print("Sorry, you ran out of guesses. The word was:{0}".format(word))
                hang_m=True
                rounds[0]+=1
                if rounds[0]>0:
                    empty_word.clear()
                    text.clear()
                    used_letters.clear()
                choose=str(input("Would you like to restart?(y/any other key)").lower())
                if choose=="y":
                    word = choose_random_word(wordlist)
                    hangman(word)
                else:
                    print("Thanks for playing, goodbye!")
                    
    elif ask=="l":
        
        ranks=get_score()
        
        if len(ranks)==0:
            print("------------------------")
           
            choose=str(input("Would you like to restart?(y/n)").lower())
            if choose=="y":
                word = choose_random_word(wordlist)
                hangman(word)
            else:
                print("Thanks for playing, goodbye!")
            
        else:   
            ranks=get_score()
            sort= sorted(ranks.items(), key=lambda t:t[1], reverse=True)
            print("{:<15}{:<15}".format("Score","Names"))
            print("--------------------")
            for i in range(0,len(sort)):
                print("{:<15}{:<15}".format(sort[i][1],sort[i][0]))
            print("--------------------")
            choose=str(input("Would you like to proceed or quit?(p/q)").lower())
            if choose=="p":
                word = choose_random_word(wordlist)
                hangman(word)
            else:
                print("Thanks for playing, goodbye!")
        
    else:
        print("Thanks for playing, goodbye!")
       
       
            


# =======================Driver function for the program=====================
if __name__ == "__main__":
    word = choose_random_word(wordlist)
    
    hangman(word)
    
  
    


    
