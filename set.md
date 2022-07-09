# Set
##  Introduction
I was trying to think of some analogy of how the term set makes sense, but while the stack guy gets an A for naming Stacks, the guy who came up with sets gets like a C for the name. It's fine, but not near as clear as a set. 

Anyways, a set is a way to store data(surprise surprise) unlike other data structures that you may know you can not store duplicate items. Understanding why requires knowing how a set works. Think of a room full of people, if you want to find someone named James, you could go about it in two different ways. If you are thinking in terms of a list, you would go to each person and ask if they are James. In terms of a set, you would just loudly ask for James. 
## Adding and removing from the Set
Adding data to a set works a bit differently than in other data structures. When a value is added the set creates a unique hash for that value. This is an address in memory. If the same value is entered again, the same hash will be given and only one copy will be stored.  When removing, the same hash is calculated, the data is found and then the data is deleted.  

Let's look at an example of a list and a set. 

<u>List:</u>

|Memory Location:|0|1|2|3|4|5|6|7|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|Data:| | | || | |||

list.append(A)

|0|1|2|3|4|5|6|7|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|A | | || | |||

list.append(F)

|0|1|2|3|4|5|6|7|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|A |F | || | |||

list.append(C)

|0|1|2|3|4|5|6|7|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|A |F |C || | |||

list.append(G)

|0|1|2|3|4|5|6|7|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|A |F |C |G| | |||

list.append(F)

|0|1|2|3|4|5|6|7|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|A |F |C |G|F | |||

list.remove(C)
|0|1|2|3|4|5|6|7|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|A |F |G|F | ||||

See [Stack](./stack.md) to better understend ineffecentcies of this command.

Now when working with a set it will hash the value and find a location for the value and then put it there. Let's use a very simple hash, it will just give each letter the location of how far down it is in the alphabet. 

<u>Set</u>

|Memory Location:|0|1|2|3|4|5|6|7|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|Data:| | | || | |

set.add(A)

|0|1|2|3|4|5|6|7|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|A | | || | |||

set.add(F)

|0|1|2|3|4|5|6|7|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|A | | || |F |||

set.add(C)

|0|1|2|3|4|5|6|7|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|A | |C || |F |||

set.add(G)

|0|1|2|3|4|5|6|7|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|A | |C || |F |G||

set.add(F)

|0|1|2|3|4|5|6|7|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|A | |C || |F |G||

set.remove(C)

|0|1|2|3|4|5|6|7|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|A | | || |F |G||

## Performance
One of the major advantages of using a set is that finding a value will only take one operation. The value is hashed and the code only has to look in that one spot. In a list, the given value would be compared to the first value in the list, and then the second and the third. This would keep going until the value is found or it reaches the end of the list. This works fine for smaller amounts of data, but as it grows larger and larger this will take more and more time. In a set the number of entries does not matter, it will only take one operation to find if the value is in the set.

To see this let's look at the end of the last example.

if (G in list)

|0|1|2|3|4|5|6|7|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|A==G |F |G|F | ||||
|A |F==G |G|F | ||||
|A |F |G == G|F | ||||

True

This would take even longer if it was not in the list, this is because it would have to check every value. This is much faster in a set. 
if (G in set)

The code when then hash G and come up with the value 6.

|0|1|2|3|4|5|6|7|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|A | | || |F |G==G||

True

## Other Commands
|Name|Opration|Python Command|Performance|
|:---:|:---:|:---:|:---:|
|add|It adds the given value to the set|my_set.add(value)|O(1)|
|remove|It removes the given value from the set|my_set.remove(value)|O(1)|
|member|Returns if the given value is in the set|(value in set)|O(1)|
|size|Returns the number of values in the set|len(my_set)|O(1)|
## Example
You are an avid stamp collector, however, you live in a small one-room apartment that has no space and even one extra stamp can not be afforded. To keep it clean you decide to wright a program to see if you have any duplicates.

```python
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
```

[Link to the File](./set%20files/example.py)

## Problem to Solve
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

Here is what you have come up with so far. Finish the code using a set. 
```python
def is_checked_in(set_of_people, person):
    """
    Check the set of people to see if the 
    person is currently checked in
    """
    pass

def check_in(set_of_people, person):
    """
    Adds the person to a set to be marked as 
    checked-in
    """
    return set_of_people

def check_out(set_of_people, person):
    """
    Checkes out the person by removing them
    from a set
    """
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
```
[Link to Problem](./set%20files/Problem.py)

[Link to Solution](./set%20files/ProblemSolution.py)

[Return To Outline](./outline.md)