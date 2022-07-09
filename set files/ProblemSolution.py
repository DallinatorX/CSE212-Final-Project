"""
You are in charge of keeping track of 
who is in a building, each time that 
someone enters they select "check-in" 
and then type their name into a 
computer, and when they leave they 
select "check out" and then type their 
name. The problem is that sometimes 
people forget to check out and when 
they check in later they end up in the 
system twice, using a stet to keep 
track of who is in the building at any time. 
"""

def is_checked_in(set_of_people, person):
    """
    Check the set of people to see if the 
    person is currently checked in
    """
    if person in set_of_people: #Check if the person is checked in
        print("Is Checked in")
    else:
        print("is not Checked in")
    

def check_in(set_of_people, person):
    """
    Adds the person to a set to be marked as 
    checked-in
    """
    set_of_people.add(person)
    return set_of_people

def check_out(set_of_people, person):
    """
    Checkes out the person by removing them
    from a set
    """
    set_of_people.remove(person)
    return set_of_people

set_of_people = set()
keep_going = True
while(keep_going):
    option = input( "1: Check-in\n"
                    "2: Check-out\n"
                    "3: Is Checked in\n"
                    "4: Ouit\n"
                    "Select Option:")
    if option == "1":
        set_of_people = check_in(set_of_people, input("What is your name?: "))

    if option == "2":
        set_of_people = check_out(set_of_people, input("What is your name?: "))

    if option == "3":
        is_checked_in(set_of_people, input("What is your name?: "))

    if option == "4":
        keep_going = False
    print("\n\n\n")