# ------------------------------------------------------
#        Name: (Rabab Radalla)
#       Peers: (add any collaborators)
#  References: (anything you checked to solve this)
# ------------------------------------------------------
import sys

secret_word = "food"

# Task 1
def check_text():
    """ Checks whether the secret word("food") or "Dog" or "dog" are found in the user's input. """
    global secret_word
    while True:
        x = input("Give me a sentence: ") #Takes the input from the user.
        if secret_word in x:
            print("You used the secret word!")
            break #Stops the code and executes the next step.
        elif "Dog" in x or "dog" in x:
            print("You used the word \"dog\" or the word \"Dog\"!")
            break 
        else:
            print("Try again")
            
# Task 2
def check_greater():
    """ Prints which integer is greater from the two user-input integers. """
    while True:
        y = int(input("Give me a first integer: ")) #Takes the input from the user.
        z = int(input("Give me a second integer: ")) 
        if y > z: #Checks if y is greater than z.
            print("First is Greater")
            break
        elif y < z: #Checks if y is less than z.
            print("Second is Greater")
            break
        else:
            print("Try again")
    
# Task 3
def get_special_numbers():
    """ Prints the numbers between 1 and 40 that are not even, not divisible by 5, and divisible by 3"""
    for element in range (1,40):
        if element % 2 == 0: #Checks if the integer is even.
            continue #Immediately jumps to the next iteration of the loop.
        if element % 3 != 0:
            continue
        if element % 5 == 0: #Checks if the integer is divisible by five.
            continue
        else:
            print(element)

# Task 4.a
def my_for_loop():
    """ Checks the input string's length and spaces, then prints if each letter is a vowel or a consonant """
    str_ing = input("Give me a string: ")
    
    if len(str_ing) not in range (2,6) or " " in str_ing: #Checks the spaces and the string's length.
        print("bad word")
        return
    
    vowels = "aeiouAEIOU" #Assigns the letters to the variable "vowels"
    
    for let in str_ing:
        if let in vowels: # Checks if the letter is a vowel
            print(f"{let} is a vowel")
        else: # Checks if the letter is a consonant
            print(f"{let} is a consonant") 
        

# Task 4.b
def my_while_loop():
    """ Repeats the prompt to the user and executes based on the choice """
    while True:
        s = input("Choose one option: a, b, or c: ") #Takes the input from the user.
        
        if s == "a":
            continue
        elif s == "b":
            print("Goodbye")
            return #Exits the function
        elif s == "c":
            exit() #Terminates the entire process.
        else:
            print("try again")
      
    

# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():

    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

if __name__ == "__main__":
    main()
    print("The End")
