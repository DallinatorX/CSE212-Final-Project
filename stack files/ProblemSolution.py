"""
Now how is this fair, I have to write
the code for example and the problem

Well here it is. 

This code lets the user keep track of dice rolls
"""

the_stack = [] #Create the Stack
print("You get 3 options:\n 1. Add Roll"
      " \n 2. Undo Last Roll \n 3. quit")
keep_going = True
while(keep_going): #keep going until the user quits
    choise = input("Choose 1, 2 , or 3: ")
    if (choise == "1"): #Add input to the stack
        string = input("Give me the roll: ")
        the_stack.append(string) 
    else: 
        if (choise == "2"): #Print the last item in the stack
            if (len(the_stack)): #Make sure the stack is not empty
                print("You just removed this roll:", 
                the_stack.pop())
            else: #If empty
                print("All gone!")
        else:
            if(choise == "3"): #They quit, what a Lame-o
                print("Goodbye :(")
                keep_going = False
            else: #Invalid input
                print("That's not a choice")
    