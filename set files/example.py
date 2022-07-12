"""
You are an avid stamp collector, however, 
you live in a small one-room apartment 
that has no space and even one extra 
stamp can not be afforded. To keep it 
clean you decide to wright a program to 
see if you have any duplicates. Each time 
that you add a stamp it is tested if it is 
in the set it returns that it is in the 
set, if not it adds it to the set.
"""


def check_for_duplicates(the_set, check_value):
    """
    This is given a set of years and an entry 
    to check if it is in the set. If not it adds 
    it to the Set
    """
    if check_value in the_set: #Check if the value is in the set
        print ("You already have that Year")
    the_set.add(check_value) #Adds the Value to the set
    return the_set

keep_going = True
years = set() # Make the Set
while(keep_going):
    year = input("What year is the Stamp(Press Q to quit)?: ")
    if (year == "q") or (year == "Q"):
        keep_going = False
    else:
        years = check_for_duplicates(years, year)