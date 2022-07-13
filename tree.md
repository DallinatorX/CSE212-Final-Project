# Trees

##  Introduction

Trees, while I still don't think that they are well named as stacks, they do beat sets. I will give the name tree a B+. 

The easiest comparison to the tree data structure is a Family tree. If you think about it, family trees have a different organization system than most things we use in life. They are not alphabetical or by age. When you want to find your great-great-grandmother you would work your way up the tree, first, you would ask if she is on your mother's or father's side of the tree. Let's say father's. You would then ask if she is on his mother's or father's side of the tree. This process would continue until she is found. Trees work in the same way.

## Adding to the Tree

When a Binary Seach Tree (BST) is created the first value is called the Root. Each time that a new value is added it goes through tests. It is first asked if it is larger or smaller than the root. If larger it goes down one side if smaller then it goes down the other side. At the next value (node) the same question is asked. This process continues until the value finds a spot that is empty and the data is stored there. 

Let's look at an example of this. We will start a tree with a value of 5.

![Tree with 5](./tree%20files/Photo1.png)

Then add a 3.

![Tree with 3,5](./tree%20files/Photo2.png)

Then add a 2

![Tree with 2,3,5](./tree%20files/Photo3.png)

Then add a 7

![Tree with 2,3,5,7](./tree%20files/Photo4.png)

Then add a 4.

![Tree with 2,3,4,5,7](./tree%20files/Photo5.png)

As you can see, each time that a value is added to the tree, the tree expands. 

## Performance

Using a BST can often lead to performance gains. Rather than having to look through every value in a list, it can just search left and right in the same manner that you would add data to the Tree. Now because you are such a smarty pants, you have probably already thought of a problem. What if you add values in order. For example, 3,4,5,6,7,8,9.

![Unblanced Tree](./tree%20files/Photo6.png)

At that point, there is no performance gain over a list. In this case, the tree will need to be balanced. This is a rather simple process, you just have to find the node that has the same number of nodes on either side of it and then divide the tree there. Repeat this over and over until the tree is balanced. 

![Unblanced Tree stage 2](./tree%20files/Photo7.png)
![Unblanced Tree stage 3](./tree%20files/Photo8.png)



## Other Commands

Python does not have a built-in Tree class, so one will be provided for you to use. Because of this, the Python commands listed are not official, but the ones used for this class.

|Name|Opration|Python Command|Performance|
|:---:|:---:|:---:|:---:|
|insert|Adds a value to the Tree|my_tree.insert|O(log n)|
|remove|Removes a value from the Tree|Not Present|O(log n)|
|contains| Determines if the given value is in the Tree|Value in my_tree|O(log n)|
|traverse forward|Lists all values from smallest to largest|for i in forward(my_tree)|O(n)|
|traverse reverse|Lists all values from largest to smallest |for i in reversed(my_tree)|O(n)|
|height|Returns how many nodes down in a Tree a Value is|my_tree.get_height()|O(n)|
|size|Returns the number of values in a Tree|Not Present|O(1)|
|empty|Returns if a Tree is empty|Not Present|O(1)|

## Example

You have a large collection of sheet music and you want to have it all organized. You decided that a tree is good for this. The example will use the length of the song as the value in the tree. This way we know how to find it based on the length of the song.

```python
Songs = BST() #Create the Tree

keep_going = True
#Keep going until quit
while(keep_going): #Keep going until quit
    again = input ("Add a song (Y/N): ")
    if again == "Y": #If yes
        name = input("What is the Name: ")
        length = int(input("How long is the song in Seconds: "))
        Songs.insert(length, name) #Add the song to the tree
        print("\n\n")
    if again == "N": #Quit if no
        keep_going = False
for x in Songs: #Return the songs in order
    print(x)
```

[Link to the File](./tree%20files/example.py)

## Problem to Solve

Expand the Tree class to find songs that are between a certain time. Let's say you wanted all songs between 90 and 300 seconds. You could call the function with those 2 inputs and it would return all of the songs in that time. Use the example as a starting templet. 

```python
```
[Link to Problem](./tree%20files/Problem.py)

[Link to Solution](./tree%20files/ProblemSolution.py)

[Return To Outline](./outline.md)