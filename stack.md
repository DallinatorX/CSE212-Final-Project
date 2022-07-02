# Stacks
##  Introduction
Can I just give a hand to the Guy that came up with the term stack in coding, it has such a straightforward name that it makes my job easy. Think about when you have to clean your room, because you are not very good at it you end up with a stack of crap in the middle, each time that you add something to it you know that you'll just have to deal with it later. To make matters worse, you have to clean it up in the backward order. The last thing that you put in it is the first that you have to take out. You can't just pull from the bottom. 

Stacks are the same(well not as messy, you should probably clean more often) the last piece of data that you put on the stack is the first that you will have to remove. 
## Adding and removing from the Stack
Stacks start empty.
```python
my_stack = []
```
Unsurprisingly, an empty stack is not that useful. However, we can add to the stack by pushing new data on. In Python, you can use the append command. 
```python
my_stack.append(data)
```
This will take whatever data you have and add it to the end of the stack. 

However, even the ability to add to a stack is not useful if we can not read the data. This is where the pop command comes into play. 
```python
new_data = my_stack.pop()
```
The pop command is a little different than the normal commands that you have used with lists before. It returns the piece of data that was most recently added to the stack and then it removes that data from the stack. This can be useful in many ways, one way that you are likely most familiar with is with the undo command. A stack makes this very simple, each time that you make a change the program records that by pushing it to a stack, when you hit Ctrl Z it just has to pop that data off. 

Even then you may wonder how a stack is any better than a list. The answer is that it depends. In many use cases, you will have to use a list, but when a stack will work it should be used, this is because of its better performance. 

## Performance
For this to make any sense at all we are going to have to dive into how a list works. Below is a table that is pretending to be memory (Don't tell him "he's not", let him live how he wants to live)

| Memory Locations: | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| | A | B | C | D | E | F | G |

If you wanted to remove the letter G from the list that would be easy

| 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| A | B | C | D | E | F | [empty] |

However, now let's say that you wanted to remove the letter C. This could not be done in one step.
Remove:

| 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| A | B | [empty] | D | E | F |  |

Move D

| 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| A | B | D | [empty] | E | F |  |

Move E

| 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| A | B | D | E | [empty] | F |  |

Move F

| 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| A | B | D | E | F | [empty] |  |

Wow. Now wasn't that a pain, something that only took one line of code took that computer 4 commands to do. This will get bigger and bigger as the list grows. Just by only touching the beginning and the end, it is much easier for the stack to grow and shrink. 

## Other Commands
There are a few other commands that you ought to know about stacks, the great thing about all of these commands is that they are not hiding any extra commands under the hood, unlike the remove command that we just learned about. 

| Name | Description | Command |
|:-----:|:-----:|:-----:|
|Size of | This will return the number of items in the stack | len(my_stack) |
| Is empty | Returns if there is anything in the stack | if ( len( my_stack) == 0) |
| push | adds the data to the end of the stack | my_stack.append(data) |
| pop | removes the last pushed data and returns it | the_data = my_stack.pop() |

## Example

Even though I am an amazing teacher I am sure that you will still want an example of how this works. Well, I'm not going to do it.

...

...did you call my bluff? FINE, I'll give you an example, this means that you will have to do one too, it's only fair. 

This is going to be a very simple program, the user will input any string of tests that they want, and each space will add it to the stack, after that, each time that they hit enter it will return the last word.  In this case, it will return them backward.

```python
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
```
[Link to file](./stack%20files/Example.py)

## Problem to Solve

Ha! Now it's your turn. What could I have you do? I know. Write a program that will let the user build their own stack, it needs to have 2 options for the user. They must be able to push and pop you need to add protection to make sure that the list is not empty and give them an option to quit the program at any time.  

[Solution](./stack%20files/ProblemSolution.py)

[Back to Outline Page](outline.md)

