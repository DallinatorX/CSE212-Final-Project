"""
The user will input any string of tests that they want, 
and each space will add it to the stack, 
after that, each time that they hit enter it will 
return the last word. 
In this case, it will return them backward.
"""

def add_words(words):
    """
    Adds the words to a stack
    """
    words_stack = words.split(" ") #Break at each space
    return words_stack    

words = input("Type a list of words here:")
stack_of_words = add_words(words)
while(len(stack_of_words)): #Check if the stack is empty
    input()
    print(stack_of_words.pop()) #Pop the last word of the stack


